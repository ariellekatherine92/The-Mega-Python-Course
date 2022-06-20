import pandas
import time
import os


while True:
    if os.path.exists("practice/temps_today.csv"):
        data = pandas.read_csv("practice/temps_today.csv")
        print(data.mean())
    else:
        print("File does not exist.")
    time.sleep(10)

