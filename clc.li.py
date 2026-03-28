import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


API_URL = 'https://clc.li/api/url/add'
LIST_LINK_API_URL = 'https://clc.li/api/urls'


def shorten_link(token, url):
    payload = {
        'url': url,
    }   
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    response = response.json()
    if 'shorturl' not in response:
        raise ValueError(f"API не вернул короткую ссылку для {url}")
    shorturl = urlparse(response['shorturl'])    
    return f"{shorturl.netloc}{shorturl.path}"


def count_clics(token, link):
    params = {'short': link}
    response = requests.get(LIST_LINK_API_URL, headers=headers, params=params)
    response.raise_for_status()
    clicks = response.json()['data']['clicks']
    return clicks


def is_bitlink(url):
    params = {'short': url}
    response = requests.get(LIST_LINK_API_URL, headers=headers, params=params)
    response.raise_for_status()
    if not response.json()['error']:
        return True
    return False


if __name__ == '__main__': 
    load_dotenv()

    clcli_token = os.environ['CLCLI_TOKEN']
    
    headers = {
        'User-Agent': 'curl',
        'Authorization': f'Bearer {clcli_token}',
        'Content-Type': 'application/json'
    }
    
    url = input()
    
    try:
        if is_bitlink(url):
            print('Количество кликов:', count_clics(clcli_token, url))  
        else:
            print('Короткая ссылка', shorten_link(clcli_token, url))
    except requests.exceptions.HTTPError as error:
        exit(f"Ошибка сети или API: {error}")
    except ValueError as error:
        exit(f"Ошибка данных: {error}")
    except KeyError:
        exit("API вернул неожиданный формат данных")
        