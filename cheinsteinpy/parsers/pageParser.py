from bs4 import BeautifulSoup as bs
import re

def checkLink(link):
    isChapter = False
    item = re.search(r'chegg.com/homework-help/questions-and-answers/(.*?)', link)
    if not item:
        isChapter = True
    linkCheck = {"isChapter": isChapter}
    return linkCheck

def parsePage(data, isChapter):
    if isChapter:
        chapter = data["data"]["textbook_solution"]["chapter"][0]
        json = chapter["problems"][0]
        solutionjson = json["solutionV2"][0]
        # totalSteps = solutionjson["totalSteps"]
        # solutionSteps = solutionjson["steps"]
        return solutionjson
    else:
        soup = bs(data, "html.parser")
        questionhtml = soup.find("div", {"class": "question-body-text"})
        answerhtml = soup.find("div", {"class": "answer-given-body"})
        return questionhtml, answerhtml