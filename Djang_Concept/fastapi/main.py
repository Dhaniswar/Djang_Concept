from fastapi import FastAPI, Body
import schemas

fakeDatabase = {
    1: {'task': 'Clean car'},
    2: {'task': 'Clean car'},
    3: {'task': 'Clean car'},
}

app = FastAPI()


@app.get("/")
async def getDetails():
    return fakeDatabase


@app.post("/")
async def addItem(item: schemas.Item):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {"task":item.task}
    return fakeDatabase

@app.put("/")
async def updateItem(item: schemas.Item):
    return fakeDatabase

@app.delete("/")
async def deleteItem(item: schemas.Item):
    return fakeDatabase

UrlR = '/^(?:([A-Za-z]+):)?(\/{0,3})([0-9.\-A-Za-z]+)(?::(\d+))?(?:\/([^?#]*))?(?:\?([^#]*))?(?:#(.*))?$/'