import requests
URL = "https://www.mediawiki.org/w/api.php"

def token(S,ttype):
    PARAMS_0 = {
        'action':"query",
        'meta':"tokens",
        'type':ttype,
        'format':"json"
        }
    R = S.get(url=URL, params=PARAMS_0)
    DATA = R.json()
    LOGIN_TOKEN = DATA['query']['tokens']['logintoken']
    return LOGIN_TOKEN

def login(S,token,uname,passwd): # require "login" type token
    PARAMS_1 = {
        'action':"login",
        'lgname':uname,
        'lgpassword':passwd,
        'lgtoken':LOGIN_TOKEN,
        'format':"json"
    }
    R = S.post(URL, data=PARAMS_1)
    DATA = R.json()
    status = DATA["login"]["result"]
    if status == "Success":
        print("Logged in as "+DATA["login"]["lgusername"])
        return True
    else:
        print("Login Failed because: "+status)
        return False

def getpage(S,title): # no token required
    PARAMS = {
        "action":"query",
        "prop":"revisions",
        "titles":title,
        "rvslots":"*",
        "rvprop":"content",
        "formatversion":"2",
        'format':"json"
    }
    R = S.get(URL, data=PARAMS)
    DATA = R.json()
    try:
        if DATA["query"]["pages"]["missing"] == True:
            return False
        else:
            return True
    except KeyError:
        return DATA["query"]["pages"]["revisions"]["slots"]["main"]

def edit(S,token,title,content): # csrf token required, WIP
    PARAMS_3 = {
        "action": "edit",
        "title": title,
        "token": token,
        "format": "json",
        "text": content,
    }
    R = S.post(URL, data=PARAMS_3)
    DATA = R.json()
