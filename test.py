import requests

url = 'https://clc.li/api/account'
responce = requests.get(url)
print(responce)
print(responce.status_code)
print(responce.raise_for_status)
print(responce.encoding)
print(responce.url)
print(responce.is_redirect)
print(responce.text)
print(responce.json())
print('----------------------------')
headers = {
    'User-Agent': 'curl',
    'Authorization': 'Bearer api_key_tut',
    'Content-Type': 'application/json'
}
responce = requests.get(url, headers=headers)
print(responce.raise_for_status)
print(responce.json())
print('----------------------------')
url = 'https://clc.li/api/url/add'
post_headers = {
    'User-Agent': 'curl',
    'Authorization': 'Bearer api_key_tut',
}
payload = {
    'url': 'https://ya.ru',
}
responce = requests.post(url, headers=post_headers, json=payload,)
print(responce.raise_for_status)
print(responce.json())