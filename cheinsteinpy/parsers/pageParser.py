from bs4 import BeautifulSoup as bs
import re

def checkLink(link):
    isChapter = False
    item = re.search(r'chegg.com/homework-help/questions-and-answers/(.*?)', link)
    if not item:
        isChapter = True
    linkCheck = {"isChapter": isChapter}
    return linkCheck

def getId(link):
    item = re.search(r'chegg.com/homework-help/questions-and-answers/(.*?)-q(\d+)', link)
    if item:
        return item.group(2)
    else:
        return None

def parsePage(data, isChapter):
    if isChapter:
        chapter = data["data"]["textbook_solution"]["chapter"][0]
        json = chapter["problems"][0]
        solutionjson = json["solutionV2"][0]
        questionjson = json["problemHtml"]
        # totalSteps = solutionjson["totalSteps"]
        # solutionSteps = solutionjson["steps"]
        return questionjson, solutionjson
    else:
        soup = bs(data, "html.parser")
        return soup