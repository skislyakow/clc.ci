import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


API_URL = 'https://clc.li/api/url/add'


def shorten_link(token, url):
    payload = {
        'url': url,
    }   
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    response = response.json()
    if 'shorturl' not in response:
        raise ValueError(f"API не вернул короткую ссылку для {url}")
    parsed = urlparse(response['shorturl'])    
    return f"{parsed.netloc}{parsed.path}"


def count_clics(token, link):
    response = requests.get(list_link_api_url, headers=headers)
    response.status_code
    clicks = response.json()['data']['clicks']
    return clicks


def is_bitlink(url):
    response = requests.get(list_link_api_url, headers=headers)
    response.raise_for_status()
    if response.json()['error'] == 0:
        return True
    else:
        return False


if __name__ == '__main__': 
    load_dotenv()

    token_clcli = os.environ['TOKEN_CLCLI']
    
    headers = {
        'User-Agent': 'curl',
        'Authorization': f'Bearer {os.environ['TOKEN_CLCLI']}',
        'Content-Type': 'application/json'
    }
    
    url = input()

    list_link_api_url = f'https://clc.li/api/urls?short={url}'
    
    try:
        if is_bitlink(url):
            print('Количество кликов:', count_clics(token_clcli, url))  
        else:
            print('Короткая ссылка', shorten_link(token_clcli, url))
    except (requests.exceptions.HTTPError, KeyError):
        raise SystemExit("Произошла ошибка при работе с API или ответом сервера")
