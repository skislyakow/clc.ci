import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


load_dotenv()


API_URL = 'https://clc.li/api/url/add'
LIST_LINK_API_URL = 'https://clc.li/api/urls?short='
TOKEN = os.environ['TOKEN']


url = input()


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
        response = requests.post(API_URL, headers=headers, json=payload)
        response.status_code
    except requests.exceptions.HTTPError:
        return f'Ошибка сокрашения: {url}'
    try:
        full_url = response.json()['shorturl']
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
    try:
        response = requests.get(LIST_LINK_API_URL + url, headers=headers)
        response.status_code
    except requests.exceptions.HTTPError:
        return f'Ошибка получения данных: {link}'
    try:
        clicks = response.json()['data']['clicks']
    except KeyError:
        raise SystemExit('Неверная короткая ссылка!')
    return clicks


def is_bitlink(url):
    headers = {
        'User-Agent': 'curl',
        'Authorization': 'Bearer ' + TOKEN,
        'Content-Type': 'application/json'
    }
    try:
        response = requests.get(LIST_LINK_API_URL + url, headers=headers)
        if response.json()['error'] == 0:
            return True
    except requests.exceptions.HTTPError:
        return False


if __name__ == '__main__':    
    if is_bitlink(url):
        print('Количество кликов:', count_clics(TOKEN, url))  
    else:
        print('Короткая ссылка', shorten_link(TOKEN, url))
