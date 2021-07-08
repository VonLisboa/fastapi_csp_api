import asyncio
import uvicorn
import json
from aiokafka import AIOKafkaProducer
from fastapi import FastAPI
from schema.contact import Contact

app = FastAPI()
producer = None


@app.on_event("startup")
async def startup_event():
    global producer
    producer = AIOKafkaProducer(
        bootstrap_servers=['172.30.0.3:9092'])
    await producer.start()

@app.on_event("shutdown")
async def shutdown_event():
    await producer.stop()

@app.post("/")
def create_contact(contact: Contact):
    return {"item": contact}
