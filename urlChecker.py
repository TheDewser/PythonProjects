import httplib

with open("urls-to-check.txt", "r") as f:
    #urlList2 = []
    for url in f:
        c = httplib.HTTPConnection(str(url))
        c.request("HEAD", '')
        if c.getresponse().status == 200:
            print('Web site exists')
        else:
            print('Web site does not exist')