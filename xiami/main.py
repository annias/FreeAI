import requests
import re

def ask(question):
    headers = {
        'authority': 'smart-chat.xiami.one',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://smart-chat.xiami.one',
        'referer': 'https://smart-chat.xiami.one/',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }

    json_data = {
        'prompt': question,
        'options': {},
        'systemMessage': "You are ChatGPT, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown.",
        'temperature': 0.8,
        'top_p': 1,
    }



    response = requests.post('https://smart-chat.xiami.one/api/chat-process', headers=headers, json=json_data)
    last_line = response.text.splitlines()[-1]

    e = re.findall('"([^"]*)"', last_line)
    e[7] = e[7].replace("\\n", " ")
    return e[7]
