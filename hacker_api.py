import time

import requests

top_id = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty').json()
print(top_id)

for id in top_id:
    results = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty').json()
    time.sleep(2)
    print(results)
