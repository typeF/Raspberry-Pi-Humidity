from dotenv import load_dotenv
load_dotenv()
import os
mongo_db_connection = os.environ.get('MONGODB_URI')
import board
import busio
import adafruit_si7021
from pymongo import MongoClient
from pprint import pprint
from datetime import datetime
from time import sleep
from random import randint

client = MongoClient(mongo_db_connection)
db = client.db

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_si7021.SI7021(i2c)

while True:
    now = datetime.now().strftime('%H:%M:%S')
    temperature = sensor.temperature
    humidity = sensor.relative_humidity

    reading = {
        'time': now,
        'humidity': humidity,
        'temperature': temperature,
    }

    result = db.humidity.insert_one(reading)
#     print("\nTemperature: %0.1f C" % sensor.temperature)
#     print("Humidity: %0.1f %%" % sensor.relative_humidity)
    sleep(60)
