#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import urllib
import urllib2

startURL = "http://www.mp4ba.com/"

def getHtml(url):
    url_open = urllib2.urlopen(url)
    html = url_open.read()
    return html
def reComplie(r , html):
    r_get = re.compile(r)
    rList = re.findall(r_get , html)
    return rList

def getTorrent(html):
    r=r'href="(show\.php\?.*?)" target='
    # r_get = re.compile(r)
    pagelist = reComplie(r , html)
    for purl in pagelist:
        hpHtml =  getHtml(startURL + purl)
        hpr =  r'<title>(.*?Mp4Ba ).*?<\/title>'
        nameList = reComplie(hpr , hpHtml)
        downr =  r'href="(down\.php\?date=.*?)"'
        urlList = reComplie(downr , hpHtml)
        # print urlList[0]
        # print nameList[0].decode("utf-8")
        urllib.urlretrieve(startURL + urlList[0], "D:/t/eurMovie/%s .torrent" % (nameList[0].decode('utf-8')))


def readPage(url):
    for x in xrange(1,36):
        pageUrl = url + "page=" + str(x)
        print pageUrl
        getTorrent(getHtml(pageUrl))

readPage("http://www.mp4ba.com/index.php?sort_id=3&")



