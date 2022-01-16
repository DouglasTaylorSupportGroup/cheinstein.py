from cheinsteinpy.parsers import questionParser
from .parsers import cookieParser, pageParser, answerParser
from . import requestPage
import time
import asyncio

def checkLink(url):
    """
    Checks if the url is a chapter or not.

    Parameters
    ----------
    url : str
        The url to check.

    Returns
    -------
    isChapter : bool
        True if chapter type solution, False if not.
    """
    return pageParser.checkLink(url)["isChapter"]

async def answer(url, cookie, userAgent):
    """
    Gets answer data from Chegg.

    Parameters 
    ----------
    url : str
        The url of the answer page.
    cookie : str
        Raw cookie json.
    userAgent : str
        The user agent to use.

    Returns
    -------
    answer : str or array
        The answer data.
        In either string (non-chapter) or array (chapter).
    """
    cookieStr = cookieParser.parseCookie(cookie)
    isChapter = pageParser.checkLink(url)["isChapter"]
    htmlData = requestPage.requestWebsite(url, cookieStr, userAgent)
    if isChapter:
        await asyncio.sleep(8)
        htmlRaw = requestPage.requestChapter(url, cookieStr, userAgent, htmlData)
    else:
        htmlRaw = htmlData
    dataRaw = pageParser.parsePage(htmlRaw, isChapter)
    if isChapter:
        data = dataRaw[1]
    else:
        data = dataRaw[1]
    parsedAnswer = answerParser.getAnswer(data, isChapter)
    if isChapter:
        answer = parsedAnswer[0]
    else:
        answer = parsedAnswer
    return answer

def question(url, cookie, userAgent):
    cookieStr = cookieParser.parseCookie(cookie)
    isChapter = pageParser.checkLink(url)["isChapter"]
    htmlData = requestPage.requestWebsite(url, cookieStr, userAgent)
    if isChapter:
        # await asyncio.sleep(6)
        htmlRaw = requestPage.requestChapter(url, cookieStr, userAgent, htmlData)
    else:
        htmlRaw = htmlData
    dataRaw = pageParser.parsePage(htmlRaw, isChapter)
    if isChapter:
        data = dataRaw[0]
    else:
        data = dataRaw[0]
    parsedQuestion = questionParser.getQuestion(data, isChapter)
    if isChapter:
        question = parsedQuestion
    else:
        question = parsedQuestion
    return question
    


