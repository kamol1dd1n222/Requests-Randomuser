import requests
import csv

users = requests.get("https://randomuser.me/api/?results=10").json()
users = users['results']

with open("data/users.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Full name", "Gender", "Email", "Phone", "Country"])
    
    for user in users:
        writer.writerow([
            f"{user['name']['first']} {user['name']['last']}",
            user['gender'],
            user['email'],
            user['phone'],
            user['location']['country']
        ])
