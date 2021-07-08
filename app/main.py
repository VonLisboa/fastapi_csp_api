import asyncio
import uvicorn
import json
from aiokafka import AIOKafkaProducer
from aiokafka.errors import KafkaError
from fastapi import FastAPI, HTTPException
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
async def create_contact(contact: Contact):
    try:
        result = await producer.send_and_wait("contact_topic", contact)
        return { "timestamp": result.timestamp }
    except KafkaError as err:
        raise HTTPException(status_code=500, detail=err)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8082)