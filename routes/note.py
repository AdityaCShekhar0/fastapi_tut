from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config.db import conn

note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.test.test.find({})
    newDocs = []

    # Convert MongoDB documents to JSON-friendly format
    for doc in docs:
        print(doc)
        newDocs.append({
            "_id": str(doc["_id"]),  # Convert ObjectId to string
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"]
        })

    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})

@note.get("/test", response_class=HTMLResponse)
async def test_template(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@note.post("/")
async def add_note(request: Request):
    form = await request.form()
    formDict = dict(form)


    formDict["important"] = True if formDict.get("important") == "on" else False


    result = conn.test.test.insert_one(formDict)

    return {"Success": True, "Inserted_ID": str(result.inserted_id)}
