import requests
import re
import os

def ask(question):
    headers = {
        'authority': 'chatgpt.skybyte.me',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://chatgpt.skybyte.me',
        'referer': 'https://chatgpt.skybyte.me/',
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
    }

    response = requests.post('https://chatgpt.skybyte.me/api/chat-process', headers=headers, json=json_data)
    with open("temp.txt", 'w') as f:
        f.write(response.text)
    
    with open('temp.txt', 'r') as f:
        last_line = f.readlines()[-1]

    e = re.findall('"([^"]*)"', last_line)
    e[9] = e[9].replace("\\n", " ")
    os.remove('temp.txt')
    return e[9]

