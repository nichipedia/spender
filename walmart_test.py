from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.walmart.com/browse/electronics/3944'

url1 = 'https://www.walmart.com/cp/clothing/5438'

url2 = 'https://www.walmart.com/m/deals/christmas-gifts/electronics'

url3 = 'https://cors-anywhere.herokuapp.com/https://www.walmart.com/browse/womens-clothing/5438_133162?povid=Fashion_LHN_Womens_Clothing'

hdr = {'User-Agent': 'Mozilla/5.0', "content-type": "text", 'Origin': 'null', 'accept': '*/*'}
response = requests.get(url3, headers=hdr)
soup = BeautifulSoup(response.text, 'html.parser')

def search_key(prep, desired):
    queue = [prep]

    while queue:
        node = queue.pop(0)
        if type(node) == list:
            for item in node:
                if type(item) == dict or type(item) == list:
                    queue.append(item)
        else:
            keys = node.keys()
            for key in keys:
                if type(node[key]) == dict:
                    queue.append(node[key])
                if type(node[key]) == list:
                    for item in node[key]:
                        if type(item) == dict or type(item) == list:
                            queue.append(item)
                if key == desired:
                    return node[key]
    return None


scriptTags = soup.findAll('script', {'type': 'application/json'})



for tag in scriptTags:
    itemDict = json.loads(tag.contents[0])
    result = search_key(itemDict, 'items')
    if result is None:
        print(f'no bueno')
    else:
        print(f'bueno!')


#items = itemDict['category']['presoData']['modules']['center'][0]['configs']['items']

# for item in items:
#     print(item['title'])

#pressdata modules top[2] center configs