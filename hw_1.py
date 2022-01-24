import requests
import json

user = 'antony-sa'
uri = f'https://api.github.com/users/{user}/repos'

r = requests.get(uri).json()
with open('response.json', 'w', encoding='utf-8') as f:
    json.dump(r, f, indent=4)