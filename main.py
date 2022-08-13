from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
connect = MongoClient(os.getenv('MONGODB_URL'))

db = connect['db']
table = db['db_table']

#insert data into mongodb
@app.put("/insert/{id}")
async def insert(id: int,item_title: str):
    try:
        table.insert_one(
                {
                    '_id': id,
                    'item_title': item_title,
                }
            )
        return {"message": "item inserted"}
    except Exception as e:
        return {"message": "item not inserted"}

#update data into mongodb
@app.put("/update/{id}")
async def update(id: int, new_item_title: str):
    try:
        data: dict = table.find_one_and_update({'_id': id}, {'$set': {'item_title': new_item_title}})
        if data:
            return {"message": "item updated"}
        return {"message": "item not found"}
    except Exception as e:
        return {"error": str(e)}

#delete data from mongodb
@app.delete("/delete/{id}")
async def delete(id: int):
    try:
        data: dict = table.find_one_and_delete({'_id': id})
        if data:
            return {"message": "item deleted"}
        return {"message": "item not found"}
    except Exception as e:
        return {"error": str(e)}

#get data from mongodb
@app.get("/get/{id}")
async def get(id: int):
    try:
        data: dict = table.find_one({'_id': id})
        if data:
            return {"id": data['_id'], "item_title": data['item_title']}
        return {"message": "item not found"}
    except Exception as e:
        return {"error": str(e)}


