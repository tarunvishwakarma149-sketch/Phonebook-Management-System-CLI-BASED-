from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional, Dict, Any
from pydantic import BaseModel

import sys
import os

# Ensure project root is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.phonebook import Phonebook, DuplicateContactError, ContactNotFoundError
from storage.database import DatabaseStorage
from core.contact import Contact

app = FastAPI(title="PhonebookPro API", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Core
storage = DatabaseStorage()
book = Phonebook(storage)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Mount static folder
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Pydantic models for API
class ContactCreate(BaseModel):
    name: str
    phone: str
    email: Optional[str] = None
    address: Optional[str] = None
    group: Optional[str] = "Other"
    notes: Optional[str] = None
    favorite: Optional[bool] = False
    tags: Optional[List[str]] = []
    alternate_phones: Optional[List[str]] = []

class ContactUpdate(BaseModel):
    new_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    group: Optional[str] = None
    notes: Optional[str] = None
    favorite: Optional[bool] = None
    tags: Optional[List[str]] = None
    alternate_phones: Optional[List[str]] = None

@app.get("/", response_class=HTMLResponse)
async def read_index():
    index_path = os.path.join(BASE_DIR, "static", "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/api/contacts")
async def get_contacts(search: Optional[str] = None, group: Optional[str] = None, tag: Optional[str] = None, favorites: Optional[bool] = False):
    if search:
        contacts = book.search(search)
    elif group:
        contacts = book.filter_by_group(group)
    elif tag:
        contacts = book.filter_by_tag(tag)
    elif favorites:
        contacts = book.get_favorites()
    else:
        contacts = book.get_all()
    
    return [c.to_dict() for c in contacts]

@app.post("/api/contacts")
async def create_contact(contact: ContactCreate):
    try:
        new_contact = book.add_contact(**contact.model_dump())
        return new_contact.to_dict()
    except DuplicateContactError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/contacts/{name}")
async def get_contact(name: str):
    contact = book.get_contact(name)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact.to_dict()

@app.put("/api/contacts/{name}")
async def update_contact(name: str, updates: ContactUpdate):
    try:
        # Filter out None values to only update provided fields
        update_data = {k: v for k, v in updates.model_dump().items() if v is not None}
        contact = book.update_contact(name, **update_data)
        return contact.to_dict()
    except ContactNotFoundError:
        raise HTTPException(status_code=404, detail="Contact not found")
    except DuplicateContactError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/api/contacts/{name}")
async def delete_contact(name: str):
    try:
        contact = book.delete_contact(name)
        return {"message": f"Contact {name} deleted"}
    except ContactNotFoundError:
        raise HTTPException(status_code=404, detail="Contact not found")

@app.post("/api/contacts/{name}/call")
async def log_call(name: str):
    try:
        book.log_call(name)
        return {"message": f"Call logged for {name}"}
    except ContactNotFoundError:
        raise HTTPException(status_code=404, detail="Contact not found")

@app.get("/api/stats")
async def get_stats():
    return book.get_statistics()
