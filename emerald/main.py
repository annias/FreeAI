import requests


def ask(question):


    headers = {
        'authority': 'delusionz.xyz',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://delusionz.xyz',
        'referer': 'https://delusionz.xyz/gpt/',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"112.0.5615.138"',
        'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.138", "Google Chrome";v="112.0.5615.138", "Not:A-Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }

    json_data = {
        'messages': '[{"role":"system","content":"You are EmeraldGPT. A highly advanced AI model trained on everything."},{"role":"user","content":"' + question + '"}]',
    }

    response = requests.post('https://delusionz.xyz/api/generate/', headers=headers, json=json_data)

    return response.json()["result"]

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"messages":"[{\\"role\\":\\"system\\",\\"content\\":\\"You are EmeraldGPT. A highly advanced AI model trained on everything.\\"},{\\"role\\":\\"user\\",\\"content\\":\\"hi\\"}]"}'
#response = requests.post('https://delusionz.xyz/api/generate/', cookies=cookies, headers=headers, data=data)