#!/usr/bin/python
import httplib
import csv
with open('urls-results.csv', 'wb') as csvfile:
    urlwriter = csv.writer(csvfile, delimiter=',')
    urlwriter.writerow(['URL', 'Status'])
    with open("urls-to-check.txt", "r") as f:
        urls = f.read().splitlines()
        for url in urls:
            try:
                c = httplib.HTTPConnection(url)
                c.request("HEAD", '')
                if c.getresponse().status == 200:
                    #print(url+' - ' +'Web site exists') #--> uncomment the print() if you want to watch process
                    urlwriter.writerow([url,'Web Site Exists'])
            except:
                #print(url+' - '+'Site not available')
                urlwriter.writerow([url,'Offline'])