import errno
import json
import os
import shutil
from time import sleep

import requests

search = "고양이"

headers = {'Content-Type': 'application/json; charset=utf-8', 'X-Naver-Client-Id': 'RuFoLfsTtI8AaT_9bWNn',
           'X-Naver-Client-Secret': 'kpOxKkLdiK'}
try:
    if not (os.path.isdir(search)):
        os.makedirs(os.path.join(search))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise

for i in range(10):
    temp = (1 + i * 100)
    URL = 'https://openapi.naver.com/v1/search/image?query=' + search + '&display=100&start=' + str(
        temp) + '&sort=sim'
    res = requests.get(URL, headers=headers)
    var = json.loads(res.text)
    print(URL)
    with open(search + '/data' + str(i) + '.json', 'w', encoding="utf-8") as outfile:
        json.dump(var, outfile, ensure_ascii=False)
    sleep(1)
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
