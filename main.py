import requests
import json
import time

import pandas as pd

columns = [
    "Wallet address",
    "Token",
    "Price",
    "Amount",
    "USD value"
]
df = pd.DataFrame(columns=columns)

from fp.fp import FreeProxy

from fake_useragent import UserAgent
ua = UserAgent()

id_s = [
'0xcbd2b3850aa5cb66f81b413b479d5c509499dcb9','0xd65448affe1475f101378a744a62c00f04cf50d6','0x3675f6a9beb9587f5844c9e2793c0cc47118a2f9','0x1fcc1bf0addab2a2b14a49e230462939c008a51f','0xdad101e6379102dc88df690112c97ad55ab73192',
'0x656de1c3894b9b6dd43ef6270420c8e83afe5a68','0x99488e13dcef45df3090a39552a44e92744d87e0','0xb617670bc253283c2ecc21f22767237d2b4b19aa','0x2c08a2507e7ffa0df52f99903462308ac8858be5','0xdc4029acb3ea434b856d86d5be310ef8c883c788',
'0x19dcc90b972ceab00fe4c130c3d139f7844eb7bb','0x381bc31bca4b81dcc72376a04f66b3d56d0ef5f3','0x30bfbfea929bba222f03aed04888db48d26f16ce','0x2e2448f5d38a4033a9be580b937b130d30ff8042','0xe023f93a82699d3478fbbe380cf94004681244c4',
'0x0400a38944d0c790c746a842561a0197b4b6dd6f','0xaf8ae5bd9a1cc676c727d75b79bf9d0685499a4b','0x0f5786426bca984e58474dcb94b107da32c2b021','0x3e52e8563ebcfc92570cf077f7c99b54381dc4f6','0x1bf26e5b175df55b8d8a4dd1606ea775b72fdf02',
'0xb13e9c4078c878ae39d8f2e34bb840448a137f8d','0x256430906356f2ab2c136dec63cd25e44ccbdb95','0xcb9d228cde40631126d9be9315e2fda53b28db4b','0x11745ab208ff5876ba23d3160b65d963c4ba9460','0xeeef2aa134abefc7406c50ccf9cf562740c6ce15',
'0x4f91e50566120e53309dff2e0c3fcbe36e2f3a4a','0xa83e9e7e5835f445256e5077ff2051330ccedd12','0x885bb7c0fc016657043b7f54c803fb326c8d3101','0xee266e648a43de488e4efdf82f38e78cf940d290','0xcd9024addf87e7bf8dcc516aec0b619900f7ed4c',
'0xc404cd920f3de1436709eb04097cb646ec897114','0x31f9c67a447bec49ed06b7ea4f3b2276346f4f5f','0x40dc917c8278cc113a44c50c3b67744ac960957b','0xa84ed271eca96d03ba4b19c5b894e7b61900bcb6','0x7f4a28bfaf7361cfe8d01617d643b44610ae8ebe',
'0xcf9b5c03a128bbe3430c6abdb63369928cb40f7b','0xb1350e0ed2ff70276b6a4caba4c890c1a755740a','0x8c675c3ac2da0adbf819deda402b88e33ea0820a','0x95227e65f4cbb5eb445d3864e00ad1451105aea2','0x42d4b1fcea9250e1d51024f7bb5c16ffd13895b3',
'0x001bb580d85b465754730af8b1b21020c731430c','0x3964d43493469ba9d6e7f0f053e7a4e74f559bfa','0x527e5d756d550e433a45be4a62cca2658f422dd2','0x12d966c301cad3bb529b42db2460d0b22b455674','0x92e031eb9afa13ce8318b944f42ec88b2b7d7cb5',
'0x59c501d96cfe034a87d12aeaa6ef6405ab4bb31f','0x1caa3fd2f5f8a229af56e73b9d5e2ed6a43136bf','0x670ca7b2ef18c1924619307abef647620cfbe627','0x0d6b42168d713e0f8592ff378ec2e36f007d97c2','0x8e029305a4f769bab3692a883b5e33339e9905e5',
'0x4a68c9b861a1e96d01785c9fd6ee983dbd1ab4d6','0x50ccf967904386b07bc7a3c8fa7df81354fdc5a0','0x8131bf786701bae90a0db06e636f32178e90b608','0x23abb0ca2e2caea09c23bda3c0a9b25232c36c2a','0x2421bf3721fea876ca0f76b685e0eeee5eec2631',
'0x1e91b7b4001476f9a24ec5a180f8aaaaa50cdf83','0xf67b953cf0e1a37bad20043dcb8a7fce3b48c091','0xa4f6cc46b5060553f005874bf4b3cdb3f838a381','0xc3bd32f2a5a30ab2bf8c1fdb2838bec35c8cb78d','0x172081575a69cfda6c6d977dd522005f4a74c882',
'0x3e4af5089778000fe2b6284a891f8df41ac3c826','0xea037026362722683b1e920b19002a72ddb3980b','0x3d84bd9a4f31928beab33beef45abf2ec931578a','0x53a165f0988999286aab4582b2ebec30b04a5c47','0xe69e5adf5bff675028ba5ecc4969df1f7c93682b',
'0xd79917b4a71e98ee858396e6d53e3388eb6ee367','0x59c3796f4115293786f02421b9274e5d7198ed66','0xfd080f293fb0b4d6bcef06520b1f220af0deea3c','0xe601ed2399f94848484fc7cde255e53609e9ef1b','0x36cc20bd602b861372a23bfe0e558c09e78e67d8',
'0xfbf44d51bce83510f32db1c3f2f1a6effcb4eb7a','0x75f08be00a3661ad2f39a844858b1a2fbc5457dc','0x42f5fc8c0279de3e2a69635d7eb165dad249d67e','0x5cc84d56a4cc81764f8b34e147c29b854654ddd4','0x5fa69da3b54792df8e0fec7b42b5dca5603a76b7',
'0xd6a2fbcebb12d93621e25e3f6092f60536b9a999','0x17c4a75c97255fdd48a295b406fc5d5bbfb37e5e','0x20c9fd37fc04b24882d751d1c106f2e3dac6fe65','0x6cc6f0dcc903a5f9bd2dbcdceff92c80c943295b','0xda279db3e4bccfadb136d379824a7590311158f1',
'0xe7a0d36cc3e85af03127dde2f7bbfa2c4207c22e','0x66fb59ec293baa024d82f4215681f5abcbeca0b7','0xdc6eebce8ce2c9f5b49d4fac9ba9d907cf1470e3'
]


for id_ in id_s:

    print(f'\n\tID: {id_}')
    ua_ = ua.random

    new_rows_ = []

    headers = {
        'authority': 'api.debank.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
        'account': '{"random_at":1683180435653,"random_id":"5cdbdb163c1a4272353545b4f8ebd97db6a544","user_addr":null}',
        'origin': 'https://debank.com',
        'referer': 'https://debank.com/',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'source': 'web',
        'user-agent': f'{ua_}',
        'x-api-nonce': 'n_GEOUS13sfMUA4zp4Ha2nSh4hmHyE29mX1B07Feyd',
        'x-api-sign': '3e7c28ee5db8a2a1252dbc087c88e16044bd6642bacbfd7b9d27133822da64a7',
        'x-api-ts': '1683180657',
        'x-api-ver': 'v2',
    }

    params = {
        'user_addr': f'{id_}',
    }

    while True:
        time.sleep(1)
        status_code = ''
        proxy = FreeProxy(rand=True).get()
        print(f'PROXY: {proxy}')
        proxy_servers = {
            'http': f'{proxy}',
            'https': f'{proxy}',
        }

        try:
            response = requests.get('https://api.debank.com/token/cache_balance_list',
                                    params=params,
                                    headers=headers,
                                    proxies=proxy_servers)
            status_code = response.status_code
        except:
            pass

        if status_code == 200:
            data = json.loads(response.text)

            for i, item in enumerate(data['data']):
                token = item["optimized_symbol"]
                price = item["price"]
                amount = int(item["raw_amount"]) / 1000000000000000000
                usd_value = price * amount

                new_rows_.append(
                    {
                        "Wallet address": id_,
                        "Token": token,
                        "Price": price,
                        "Amount": amount,
                        "USD value": usd_value
                    }
                )

                df = pd.concat([df, pd.DataFrame(new_rows_, index=[0])], ignore_index=True)
                print(df.to_string(index=False))

                breakpoint()

            print('\n============================================================================\n')
            breakpoint()
            break
        else:
            print(f"ERROR!!! --->>> {response}")
