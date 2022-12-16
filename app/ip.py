import requests as re
import html5lib
from bs4 import BeautifulSoup as bs
import json

def isp():
    url = "http://ipwho.is"
    res = re.get(url).text
    return (res)

def ip():
    url = "https://ipstack.com"
    res = str(re.get(url).content)
    sp = bs(res,'html5lib')
    soup = sp.find('input',attrs={"name":"iptocheck"})
    return soup['value']
