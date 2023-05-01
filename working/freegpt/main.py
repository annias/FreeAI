import requests
def ask(question):

    headers = {
        'authority': 'chatgptfree.ai',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary2AFtjRX8LNRWGlnU',
        # 'cookie': '_lscache_vary=be06cbe133225fce257c7b6b5e79cc4e; _ga_3R435T3MT7=GS1.1.1682895046.1.0.1682895046.0.0.0; _gid=GA1.2.973686322.1682895047; _gat_gtag_UA_262620842_1=1; fpestid=YRZNCvEeChAsvkHB6pZv2yAvhLUsK7ULA2fzf-BbsVdEWiYtTMhTNJYRNlphvO2IO1FirA; _ga_T5L0Q6G8YV=GS1.1.1682895046.1.0.1682895046.0.0.0; _ga=GA1.1.1989775373.1682895047; __gads=ID=21620a2a2774cb6b-2221d8d37adf0082:T=1682895047:RT=1682895047:S=ALNI_MbGF6f3G64Azo1YAzq5139alJBrgg; __gpi=UID=00000be6ce26bd31:T=1682895047:RT=1682895047:S=ALNI_Mb19uEdMo-7n7gCw3XiGio8Um1iYg',
        'origin': 'https://chatgptfree.ai',
        'referer': 'https://chatgptfree.ai/',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }

    data = f'------WebKitFormBoundary2AFtjRX8LNRWGlnU\r\nContent-Disposition: form-data; name="_wpnonce"\r\n\r\n01fad7b07c\r\n------WebKitFormBoundary2AFtjRX8LNRWGlnU\r\nContent-Disposition: form-data; name="post_id"\r\n\r\n6\r\n------WebKitFormBoundary2AFtjRX8LNRWGlnU\r\nContent-Disposition: form-data; name="url"\r\n\r\nhttps://chatgptfree.ai\r\n------WebKitFormBoundary2AFtjRX8LNRWGlnU\r\nContent-Disposition: form-data; name="action"\r\n\r\nwpaicg_chat_shortcode_message\r\n------WebKitFormBoundary2AFtjRX8LNRWGlnU\r\nContent-Disposition: form-data; name="message"\r\n\r\n{question}\r\n------WebKitFormBoundary2AFtjRX8LNRWGlnU\r\nContent-Disposition: form-data; name="bot_id"\r\n\r\n0\r\n------WebKitFormBoundary2AFtjRX8LNRWGlnU--\r\n'

    response = requests.post('https://chatgptfree.ai/wp-admin/admin-ajax.php', headers=headers, data=data)

    return response.json()["data"]