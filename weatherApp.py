import requests
import json

city = input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=d282bb4b6c184c6b8e0101539241305&q={city}"

r = requests.get(url)
# print(r.text)
wthdict = json.loads(r.text)
print("Current Temprature in", city ,"is", wthdict["current"]["temp_c"])