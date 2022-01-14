from bs4 import BeautifulSoup as bs

def getQuestion(dataRaw, isChapter):
    if isChapter:
        html = bs(dataRaw, "html.parser")
        if "<b>" or "</b>" in html:
            strong = html.find_all("b")
            for i in strong:
                i.replace_with("**" + i.text + "**")
        hasimg = False
        if "<img>" or "</img>" in html:
            hasimg = True
            img = html.find_all("img")
            for i in img:
                url = i["src"]
                i.replace_with(" " + url + " ")
            text = html.get_text()
            text = text.strip()
            if hasimg:
                text = " ".join(text.split())
        return text
    else:
        if 'class="hidden"' in str(dataRaw):
            hidden = dataRaw.find_all("div", {"class": "hidden"})
            for i in hidden:
                i.replace_with("")
        if "<strong>" or "</strong>" in str(dataRaw):
            strong = dataRaw.find_all("strong")
            for i in strong:
                i.replace_with("**" + i.text + "**")
        if "<img>" or "</img>" in str(dataRaw):
            img = dataRaw.find_all("img")
            for i in img:
                url = i["src"]
                i.replace_with(url)
        questionList = []
        for k in dataRaw.contents[1:-1]:
            txt = k.text
            questionList.append(txt)
        questionList = [x for x in questionList if x]
        if questionList[0] == "\n":
            questionList = questionList[1:]
        if questionList[-1] == "\n":
            questionList = questionList[:-1]      
        questionList = " ".join(questionList)
        return questionList