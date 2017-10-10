#!/usr/bin/python
import httplib

with open("urls-to-check.txt", "r") as f:
    urls = f.read().splitlines()
    #urlList2 = []
    for url in urls:
        c = httplib.HTTPConnection(url)
        c.request("HEAD", '')
        if c.getresponse().status == 200:
            print(url+' - ' +'Web site exists')
        else:
            print('Web site does not exist')