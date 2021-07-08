from fastapi import FastAPI
from schema.contact import Contact

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/")
def create_contact(contact: Contact):
    return {"item": contact}
