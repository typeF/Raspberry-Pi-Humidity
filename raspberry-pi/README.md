## Setup

Add .env file with db connection string (w/ write access)

```
MONGODB_URI=YOUR_CONNECTION_STRING
```

## Dependencies

Dotenv

```
pip3 install -U python-dotenv
```

dnspython

```
pip3 install pymongo[srv]
```

PyMongo

```
pip3 install pymongo
```

SI2071 Circuit Python Library

```
pip3 install adafruit-circuitpython-si7021
```

## IC2 & SPI Setup

https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi

## Running app with PM2

```
pm2 start monitor.py --interpreter python3 --interpreter-args -u
```

## Sensor docs

https://learn.adafruit.com/adafruit-si7021-temperature-plus-humidity-sensor/circuitpython-code
