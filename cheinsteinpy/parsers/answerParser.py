from bs4 import BeautifulSoup as bs

def getAnswer(dataRaw, isChapter):
    if dataRaw is None:
        return None
    else:
        if isChapter:
            totalSteps = dataRaw["totalSteps"]
            stepList = []
            for i in dataRaw["steps"]:
                html = bs(str(i["html"]), "html.parser")
                if "<b>" or "</b>" in i:
                    strong = html.find_all("b")
                    for i in strong:
                        i.replace_with("**" + i.text + "**")
                hasimg = False
                if "<img>" or "</img>" in i:
                    hasimg = True
                    img = html.find_all("img")
                    for i in img:
                        url = i["src"]
                        i.replace_with(" " + url + " ")
                text = html.get_text()
                text = text.strip()
                if hasimg:
                    text = " ".join(text.split())
                stepList.append(text)
            return stepList, totalSteps
        else:
            if 'class="hidden"' in str(dataRaw):
                hidden = dataRaw.find_all("div", {"class": "hidden"})
                for i in hidden:
                    i.replace_with("")
            if "<strong>" or "</strong>" in str(dataRaw):
                strong = dataRaw.find_all("strong")
                for i in strong:
                    if "<img>" or "</img>" or "<img alt=" in str(i):
                        img = dataRaw.find_all("img")
                        for i in img:
                            url = i["src"]
                            i.replace_with(url)
                    else:
                        i.replace_with("**" + i.text + "**")
            if "<img>" or "</img>" or "<img alt=" in str(dataRaw):
                img = dataRaw.find_all("img")
                for i in img:
                    url = i["src"]
                    if ".cloudfront.net" in url:
                        if "https://" not in url:
                            url = f"https:{url}"
                    i.replace_with(" " + url + " ")
            answerList = []
            for k in dataRaw.contents[1:-1]:
                txt = k.text
                if "\n" in txt and len(txt) > 2:
                    newtxt = txt.replace("\n", " ")
                    answerList.append(newtxt)
                else:
                    answerList.append(txt)
            answerList = [x for x in answerList if x]
            if answerList[0] == "\n":
                answerList = answerList[1:]
            if answerList[-1] == "\n":
                answerList = answerList[:-1]
            answer = (" ".join((" ".join(answerList)).split(" "))).strip()
            return answer