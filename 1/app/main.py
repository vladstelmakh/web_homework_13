# app/main.py

from fastapi import FastAPI, Depends
from app.auth import verify_token, create_access_token, register_user, login_user, send_verification_email
from app.crud import create_contact, get_contacts, get_contact_by_id, update_contact, delete_contact
from app.database import SessionLocal, engine
from app.models import Base
from app.schemas import ContactCreate, Contact, UserCreate, User
from sqlalchemy.orm import Session

app = FastAPI()

# Додайте CORS, ліміти, та інші налаштування тут

@app.post("/register", response_model=User)
def register_new_user(user: UserCreate, db: Session = Depends(SessionLocal)):
    return register_user(db, user)

@app.post("/login")
def login(email: str, password: str, db: Session = Depends(SessionLocal)):
    return login_user(email, password, db)

@app.post("/contacts/", response_model=Contact)
def create_new_contact(contact: ContactCreate, db: Session = Depends(SessionLocal)):
    return create_contact(db, contact)

@app.get("/contacts/", response_model=list[Contact])
def get_all_contacts(skip: int = 0, limit: int = 10, db: Session = Depends(SessionLocal)):
    return get_contacts(db, skip, limit)

@app.get("/contacts/{contact_id}", response_model=Contact)
def get_single_contact(contact_id: int, db: Session = Depends(SessionLocal)):
    return get_contact_by_id(db, contact_id)

@app.put("/contacts/{contact_id}", response_model=Contact)
def update_single_contact(contact_id: int, contact: ContactCreate, db: Session = Depends(SessionLocal)):
    return update_contact(db, contact_id, contact)

@app.delete("/contacts/{contact_id}", response_model=Contact)
def delete_single_contact(contact_id: int, db: Session = Depends(SessionLocal)):
    return delete_contact(db, contact_id)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
