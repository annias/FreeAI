import requests
def ask(question):
    headers = {
        'authority': 'c.aigc.it',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://c.aigc.it',
        'path': '/v1/chat/completions',
        'referer': 'https://c.aigc.it/',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
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
    }

    response = requests.post('https://c.aigc.it/api/chat-stream', headers=headers, json=json_data)
    
    return response.text
