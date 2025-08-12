import requests
import os

users = requests.get("https://randomuser.me/api/?results=5").json()['results']


for i, u in enumerate(users, start=1):
    img_url = u["picture"]["large"]
    img_data = requests.get(img_url).content
    with open(f"images/user{i}.jpg", "wb") as img_file:
        img_file.write(img_data)