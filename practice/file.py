import time
import os
import pandas

while True:
    if os.path.exists("practice/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(data.mean())
        with open("practice/veggies.txt") as file:
            print(file.read())
    else:
        print("File does not exist.")
    time.sleep(10)

