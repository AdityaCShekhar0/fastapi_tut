from fastapi import APIRouter
from models.note import Note
from schemas.note import NotesEntity, NoteEntity
from config.db import conn


