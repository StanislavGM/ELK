from typing import List
from fastapi import FastAPI
from elasticsearch import AsyncElasticsearch
from datetime import datetime
from contextlib import asynccontextmanager

es = AsyncElasticsearch(
    'https://172.31.31.246:9200',
    basic_auth=('developer', 'passwd123'),
    ca_certs="../certs/http_ca.crt"
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await es.close()

app = FastAPI(lifespan=lifespan)

@app.get("/todo")
async def read_todos():
    try:
        data = await es.search(index="advertising", body={"query":{"match":{"TV": 230.1}}})
        hits = data['hits']['hits']
    except:
        hits=[]
    return hits

@app.get("/todo/{id}")
async def read_detail_todo(id:str):
    data = await es.get(index="advertising", id=id)
    item = data['_source']
    return item

@app.post("/todo")
async def create_todo(id:str,TV:float, Newspaper:float, Sales:float, Radio:float):
    doc = {
        'TV': TV,
        'Newspaper': Newspaper,
        'Sales': Sales,
        'Radio': Radio,
    }
    response = await es.index(index="advertising",id=id,document=doc)
    item = response['result']
    return item

@app.delete("/todo/{id}")
async def delete_account(id:str):
    response = await es.delete(index="advertising", id=id)
    item = response['result']
    return item
#To run the script 1) Copy http_ca.crt actual dir to this script 2) Activate venv . bin/activate 3) Execute: uvicorn swagger:app --reload --host 0.0.0.0
