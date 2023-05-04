import requests
import json

id_ = '0x19dcc90b972ceab00fe4c130c3d139f7844eb7bb'

headers = {
    'authority': 'api.debank.com',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
    'account': '{"random_at":1683180652,"random_id":"4cdbdb163c1a4272b4f8ebd97db6a544","user_addr":null}',
    'origin': 'https://debank.com',
    'referer': 'https://debank.com/',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'source': 'web',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'x-api-nonce': 'n_GEOUS13sfMUA4zp4Ha2nSh4hmHyE29mX1B07Feyd',
    'x-api-sign': '3e7c28ee5db8a2a1252dbc087c88e16044bd6642bacbfd7b9d27133822da64a7',
    'x-api-ts': '1683180657',
    'x-api-ver': 'v2',
}

params = {
    'user_addr': f'{id_}',
}

response = requests.get('https://api.debank.com/token/cache_balance_list', params=params, headers=headers)

aaa = json.loads(response.text)

print(aaa['data'][0]['id'])

for i, item in enumerate(aaa['data']):
    print(f'\n{i} Token: {item["optimized_symbol"]}')
    price_ = item["price"]
    print(f'\t--->>> Price: {price_}')
    amount_ = int(item["raw_amount"]) / 1000000000000000000     # !!!!!! >>> raw_amount <<< !!!!!!
    print(f'\t--->>> Amount: {amount_}')
    print(f'\t--->>> USD Value: {price_ * amount_}')
