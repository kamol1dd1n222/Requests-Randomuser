import requests
import json
 
data = requests.get("https://randomuser.me/api/?results=20").json()
users = data['results']
young_people = []


for user in users:
    if int(user['dob']['date'][:4]) > 1990:
         i = ({
        'name': user['name']['first'] + " " + user['name']['last'],
        'birth_year':int(user['dob']['date'][0:4:1]),
        'email': user['email']
         })
         young_people.append(i)
    
        
with open('data/young_users.json','w') as file:
    json.dump(young_people,file,indent=4)