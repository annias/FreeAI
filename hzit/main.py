import requests
def ask(question):
    headers = {
            'authority': 'chargpt.hz-it-dev.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://chatgpt.hz-it-dev.com',
            'referer': 'https://chatgpt.hz-it-dev.com/',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'x-nonce': '500009',
            'x-signature': 'a1a053f90cd02848e4f6acc52d866b71f2c8244f1a68829a8f7f318ffec70758',
            'x-timestamp': '1682897706438',
        }

    json_data = {
            'messages': [
                {
                    'role': 'user',
                    'content': question,
                },
            ],
            'stream': True,
            'model': 'gpt-3.5-turbo',
            'temperature': 1,
            'presence_penalty': 0,
            'text': question,
        }

    response = requests.post('https://chargpt.hz-it-dev.com/send2', headers=headers, json=json_data)

    return response.json()["data"]

