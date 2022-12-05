from cheinsteinpy.parsers import pageParser, cookieParser
from cheinsteinpy import requestPage, api

link = "https://www.chegg.com/homework-help/questions-and-answers/question-1-die-rolled-10-times-let-x-number-times-six-appears-10-rolls-part-probability-4--q63245414"
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
with open("cookie.txt", 'r') as f:
    cookieTxt = f.read()

# cookieStr = cookieParser.parseCookie(cookieTxt)

answer = api.question(link, cookieTxt, userAgent)
print(answer)
"""
payload = {
    "operationName":"QnaPageQuestionByLegacyId",
    "variables": {
        "id":88129188
    },
    "extensions": {
        "persistedQuery": {
            "version":1,
            "sha256Hash":"26efed323ef07d1759f67adadd2832ac85d7046b7eca681fe224d7824bab0928"
        }
    }
}

#data = requestPage.requestWebsite(link, cookieStr, userAgent)
data = requestPage.requestGraphQl(cookieStr, userAgent, payload)
print(data)
"""