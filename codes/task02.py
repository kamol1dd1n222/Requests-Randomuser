import requests
import json
 
data = requests.get("https://randomuser.me/api/?results=10").json()
users = data['results']
people = []


for user in users:
    i = ({
        'full_name': user['name']['first'] + " " + user['name']['last'],
        'email': user['email'],
        'gender':user['gender'],
        'country':user['location']['country']
    })
    people.append(i)
        
with open('data/users.json','w') as file:
    json.dump(people,file,indent=4)