from dotenv import load_dotenv
load_dotenv()
import os
mongo_db_connection = os.environ.get('mongo_db_connection')
from pymongo import MongoClient
from pprint import pprint
from datetime import datetime
from random import randint

client = MongoClient(mongo_db_connection)
db = client.db
# serverStatusResult = db.command("serverStatus")
# pprint(serverStatusResult)

now = datetime.now().strftime('%H:%M:%S')

humidity = {
        'time': now,
        'humidity': randint(1,100)
        }

result = db.humidity.insert_one(humidity)

pprint(result.inserted_id)
