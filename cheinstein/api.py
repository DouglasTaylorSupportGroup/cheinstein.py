from .parsers import cookieParser, pageParser, answerParser
from . import requestPage

def answer(url, cookie, userAgent):
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
        # await asyncio.sleep(6)
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
    


