# -*- coding: utf-8 -*-

import mechanicalsoup
import datetime
URL = 'https://portal.sa.dendai.ac.jp/up/faces/login/Com00505A.jsp'
A_URL = 'https://portal.sa.dendai.ac.jp/up/faces/up/po/Poa00601A.jsp'


def login(username, password):
    brow = mechanicalsoup.Browser()
    login_page = brow.get(URL)
    form = login_page.soup.select('#form1')[0]
    form.select('#form1:htmlUserId')[0]['value'] = username
    form.select('#form1:htmlPassword')[0]['value'] = password
    page2 = brow.submit(form, login_page.url)
    return page2

def get_time_table(page2):
    table = []
    for tag in page2.soup.findAll("td", {"class": "colPad"}):
        for tag2 in tag.findAll("span"):
            table.append(tag2.text)
    table = list(filter(lambda s:s != '', table))
    return table 

def get_news(page2):
    news = []
    for tag in page2.soup.findAll("tr", {"class": "rowHeight"}):
        for tag2 in tag.findAll("span"):
            news.append(tag2.text)
    news = list(filter(lambda s:s !='' and s != '\xa0', news))
    return news
