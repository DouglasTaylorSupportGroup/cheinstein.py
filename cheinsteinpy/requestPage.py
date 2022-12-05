import requests
import re
    
def requestWebsite(url, cookie, userAgent):
    headers = {
        'Host': 'www.chegg.com',
        "Accept-Encoding": "gzip, deflate, br",
        'Accept-Language': 'en-US,en;q=0.5',
        'cookie': cookie,
        'upgrade-insecure-requests': '1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'Upgrade-Insecure-Requests': '1',
        'TE': 'trailers',
        'user-agent': userAgent,
        'referer': 'https://www.google.com/'
    }
    response = requests.get(url=url, headers=headers)
    return response.text
    
def requestChapter(url, cookie, userAgent, html):
    headers = {
        'Host': 'www.chegg.com',
        "Accept-Encoding": "gzip, deflate, br",
        'Accept-Language': 'en-US,en;q=0.5',
        'cookie': cookie,
        'upgrade-insecure-requests': '1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'Upgrade-Insecure-Requests': '1',
        'TE': 'trailers',
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

def requestGraphQl(cookie, userAgent, data):
    headers = {
        'apollographql-client-name': 'chegg-web',
        'apollographql-client-version': 'main-474a3766-3331951797',
        'content-type': 'application/json',
        "Accept-Encoding": "gzip, deflate, br",
        'Accept-Language': 'en-US,en;q=0.5',
        'authorization': 'Basic TnNZS3dJMGxMdVhBQWQwenFTMHFlak5UVXAwb1l1WDY6R09JZVdFRnVvNndRRFZ4Ug==',
        'cookie': cookie,
        'upgrade-insecure-requests': '1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'Upgrade-Insecure-Requests': '1',
        'user-agent': userAgent,
    }
    url = "https://gateway.chegg.com/one-graph/graphql"
    response = requests.post(url=url, headers=headers, json=data, data=None)
    return response.json()

def requestEnhancedAnswer(url, cookie, userAgent, html):
    headers = {
        'Host': 'www.chegg.com',
        "Accept-Encoding": "gzip, deflate, br",
        'Accept-Language': 'en-US,en;q=0.5',
        'cookie': cookie,
        'upgrade-insecure-requests': '1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'Upgrade-Insecure-Requests': '1',
        'TE': 'trailers',
        'user-agent': userAgent,
        'referer': 'https://www.google.com/'
    }
    