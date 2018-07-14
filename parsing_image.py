import json
import shutil

import requests

search = "고양이"
# basic funciton to get id list
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/63.0.3239.132 Safari/537.36'}
for i in range(10):
    with open(search + '/data' + str(i) + '.json', 'r', encoding='utf-8') as f:
        array = json.load(f)
        for j in range(100):
            url = array['items'][j]['link']
            response = requests.get(url, stream=True, headers=headers)
            print(j)
            if response.status_code == 200:
                with open(search + '/img' + str(i) + '_' + str(j) + '.png', 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
            del response

    print("complete!!" + str(i))
print("Perfect complete!!")
