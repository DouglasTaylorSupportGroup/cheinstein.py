import requests
import re
    
def requestWebsite(url, cookie, userAgent):
    headers = {
        'Host': 'www.chegg.com',
        'authority': 'www.chegg.com',
        "Accept-Encoding": "gzip, deflate, br",
        'accept-language': 'en-US,en;q=0.5',
        'cookie': cookie,
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'user-agent': userAgent,
        'referer': 'https://www.google.com/'
    }
    response = requests.get(url=url, headers=headers)
    return response.text
    
def requestChapter(url, cookie, userAgent, html):
    headers = {
        'Host': 'www.chegg.com',
        'authority': 'www.chegg.com',
        "Accept-Encoding": "gzip, deflate, br",
        'accept-language': 'en-US,en;q=0.5',
        'cookie': cookie,
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'user-agent': userAgent,
        'referer': 'https://www.google.com/'
    }
    token = re.search(r'"token":"(.+?)"', html).group(1)
    chapter_id = str(re.search(r'\?id=(\d+).*?isbn', html).group(1))
    isbn13 = str(re.search(r'"isbn13":"(\d+)"', html).group(1))
    problemId = str(re.search(r'"problemId":"(\d+)"', html).group(1))
    query = {
        "query": {
            "operationName": "getSolutionDetails",
            "variables": {
                "isbn13": isbn13,
                "chapterId": chapter_id,
                "problemId": problemId
            }
        },
        "token": token
    }
    url = 'https://www.chegg.com/study/_ajax/persistquerygraphql'
    response = requests.post(url=url, headers=headers, json=query, data=None)
    return response.json()