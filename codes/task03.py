import requests
import json
 
data = requests.get("https://randomuser.me/api/?results=10&gender=female").json()
users = data['results']
females = []


for user in users:
    i = ({
        'full_name': user['name']['first'] + " " + user['name']['last'],
        'email': user['email'],
        'phone':user['phone'],
        'country':user['location']['country']
    })
    females.append(i)
        
with open('data/females.json','w') as file:
    json.dump(females,file,indent=4)