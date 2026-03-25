import requests

from urllib.parse import urlparse


API_URL = 'https://clc.li/api/url/add'
LIST_LINK_API_URL = 'https://clc.li/api/urls?short='

token='api_key_tut'

#url = 'https://ya.ru'
#url = input()
link = 'clc.li/tYGho'

def shorten_link(token, url):
    payload = {
        'url': url,
    }
    headers = {
        'User-Agent': 'curl',
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    try:
        responce = requests.post(API_URL, headers=headers, json=payload)
        responce.status_code
    except requests.exceptions.HTTPError:
        return f'Ошибка сокрашения: {url}'
    #print(responce.raise_for_status)
    try:
        full_url = responce.json()['shorturl']
    except KeyError:
        raise SystemExit(f'Ошибка! Ввели неправильный URL - {url} ')
    parsed = urlparse(full_url)
    return f"{parsed.netloc}{parsed.path}"


def count_clics(token, link):
    headers = {
        'User-Agent': 'curl',
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    #try:
    responce = requests.get(LIST_LINK_API_URL + link, headers=headers)
    print(responce.status_code)
    print(responce.text)
    '''
    except requests.exceptions.HTTPError:
        return f'Ошибка сокрашения: {url}'
    #print(responce.raise_for_status)
    try:
        full_url = responce.json()['shorturl']
    except KeyError:
        raise SystemExit(f'Ошибка! Ввели неправильный URL - {url} ')
    parsed = urlparse(full_url)
    return f"{parsed.netloc}{parsed.path}"
    '''

#shorten_link(token, url)

#print('Короткая ссылка', shorten_link(token, url))
print('Чтототам', count_clics(token, link))

