import requests
import json

users = requests.get('https://randomuser.me/api/?results=10').json()['results']

users_list = []
for user in users:
    data_user = {
        'name':user['name']['first'] + ' ' + user['name']['last'],
        'email':user['email'],
        'image_url':user['picture']['large']
    }
    users_list.append(data_user)
with open('data/users_with_images.json','w') as file:
    json.dump(users_list,file,indent=4)
        
