import json

# Parses the Cookie for the Chegg Account
def parseCookie(cookieTxt):
    cookieRaw = json.loads(cookieTxt)
    cookieString = ""
    z = True
    for cookie in cookieRaw:
        if not z:
            cookieString += "; "
        cookieString += "{name}={value}".format(**cookie)
        z = False
    cookie = cookieString.strip()
    return cookie