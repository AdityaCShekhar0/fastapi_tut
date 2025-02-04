from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

conn=MongoClient("mongodb://localhost:27017/")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs=conn.test.test.find({})
    newDocs=[]
    for doc in docs:
        print(doc)
        newDocs.append({
            "_id":doc["_id"],
            "note":doc["note"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})
