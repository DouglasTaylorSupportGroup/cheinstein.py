from cheinsteinpy.requestPage import requestWebsite
from cheinsteinpy.parsers import cookieParser, pageParser, answerParser
from cheinsteinpy import requestPage
import asyncio
import time

def answer(url, cookie, userAgent):
    cookieStr = cookieParser.parseCookie(cookie)
    isChapter = pageParser.checkLink(url)["isChapter"]
    htmlData = requestPage.requestWebsite(url, cookieStr, userAgent)
    if isChapter:
        time.sleep(8)
        htmlRaw = requestPage.requestChapter(url, cookieStr, userAgent, htmlData)
    else:
        htmlRaw = htmlData
    dataRaw = pageParser.parsePage(htmlRaw, isChapter)
    if isChapter:
        data = dataRaw
    else:
        data = dataRaw[1]
    parsedAnswer = answerParser.getAnswer(data, isChapter)
    if isChapter:
        answer = parsedAnswer[0]
    else:
        answer = parsedAnswer
    return answer
    


