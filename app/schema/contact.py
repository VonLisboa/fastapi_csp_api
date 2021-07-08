from pydantic import BaseModel

class Contact(BaseModel):
    nome: str
    canal: str
    valor: str
    obs: str