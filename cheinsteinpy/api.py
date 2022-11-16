from cheinsteinpy.parsers import questionParser
from .parsers import cookieParser, pageParser, answerParser
from . import requestPage

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

def getId(url):
    """
    Gets the id of the question.

    Parameters
    ----------
    url : str
        The url to check.

    Returns
    -------
    id : str
        The id of the question.
    """
    return pageParser.getId(url)

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
    if isChapter:
        # await asyncio.sleep(6)
        htmlData = requestPage.requestWebsite(url, cookieStr, userAgent)
        htmlRaw = requestPage.requestChapter(url, cookieStr, userAgent, htmlData)
    else:
        qid = pageParser.getId(url)
        data = {
            "operationName":"QnaPageQuestionByLegacyId",
            "variables": {
                "id":int(qid)
            },
            "extensions": {
                "persistedQuery": {
                    "version":1,
                    "sha256Hash":"26efed323ef07d1759f67adadd2832ac85d7046b7eca681fe224d7824bab0928"
                }
            }
        }
        raw = requestPage.requestGraphQl(cookieStr, userAgent, data)
        htmlRaw = raw["data"]["questionByLegacyId"]["htmlAnswers"][0]["answerData"]["html"]
    dataRaw = pageParser.parsePage(htmlRaw, isChapter)
    if isChapter:
        data = dataRaw[1]
    else:
        data = dataRaw
    parsedAnswer = answerParser.getAnswer(data, isChapter)
    if isChapter:
        answer = parsedAnswer[0]
    else:
        answer = parsedAnswer
    return answer

def question(url, cookie, userAgent):
    """
    Gets question data from Chegg.

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
        data = dataRaw[0]
    else:
        data = dataRaw[0]
    parsedQuestion = questionParser.getQuestion(data, isChapter)
    if isChapter:
        question = parsedQuestion
    else:
        question = parsedQuestion
    return question
    


