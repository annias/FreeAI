import requests
import fake_useragent

ua = fake_useragent.UserAgent(browsers=['chrome', "firefox", "opera", "safari", "edge", "internet explorer"])
def ask(question):
    headers = {
        'origin': 'https://chat.jinshutuan.com',
        'referer': 'https://chat.jinshutuan.com/',
        'user-agent': ua.random,
    }

    json_data = {
        'prompt': 'You are to act as ChatGPT. A large language model trained by OpenAI. You will only speak in english. ' + question, # overrides default chinese prompt.
        'system': '',
        'withoutContext': True,
        'stream': False,
    }

    response = requests.post('https://api.binjie.fun/api/generateStream', headers=headers, json=json_data)

    return (response.text)