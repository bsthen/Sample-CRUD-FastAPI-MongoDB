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
@app.put("/insert/{item_id}")
async def insert(item_id: str,item_title: str):
    try:
        table.insert_one(
                {
                    'item_id': item_id,
                    'item_title': item_title,
                }
            )
        return {"message": "item inserted"}
    except Exception as e:
        return {"message": "item not inserted"}

#update data into mongodb
@app.put("/update/{item_id}")
async def update(item_id: int, new_item_title: str):
    try:
        data: dict = table.find_one_and_update({'item_id': item_id}, {'$set': {'item_title': new_item_title}})
        if data:
            return {"message": "item updated"}
        return {"message": "item not found"}
    except Exception as e:
        return {"error": str(e)}

#delete data from mongodb
@app.delete("/delete/{item_id}")
async def delete(item_id: int):
    try:
        data: dict = table.find_one_and_delete({'item_id': item_id})
        if data:
            return {"message": "item deleted"}
        return {"message": "item not found"}
    except Exception as e:
        return {"error": str(e)}

#get data from mongodb
@app.get("/get/{item_id}")
async def get(item_id: int):
    try:
        data: dict = table.find_one({'item_id': item_id})
        if data:
            return {"video_id": data['item_id'], "item_title": data['item_title']}
        return {"message": "item not found"}
    except Exception as e:
        return {"error": str(e)}


