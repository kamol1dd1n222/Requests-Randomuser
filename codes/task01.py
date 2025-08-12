import requests 
import json

url = 'https://randomuser.me/api/'
data = requests.get(url).json()    #json() malumotni json qilib beradi
                                    # bu esa loads qilib o'qish shart emas
content = data['results'][0]
print(content)

user  = {
    'first_name':content['name']['first'],
    'last_name' :content['name']['last'],
    'gender':content['gender'],
    'email':content['email'],
    'phone':content['phone'],
    'address':{
        'street':str(content['location']['street']['number']) + ' ' + content['location']['street']['name'],
        'city':content['location']['city'],
        'country':content['location']['country']
    }
}
with open("data/user.json",'w') as file:
    json.dump(user,file,indent=4)
