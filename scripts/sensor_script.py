import os
import time
import random as rn
from datetime import datetime

while True :
    sensor_type = os.getenv("Sensor_type")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    distance_value = rn.randint(20,400)
    print(f"My sensor type is {sensor_type} , the distance equal {distance_value} and the time now is {timestamp} ")
    time.sleep(3)
