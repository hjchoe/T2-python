# James Choe
# Assignment 4.5.1- Final Week's project
# 3/12/2021

import urllib.request
import urllib.parse
from html.parser import HTMLParser
import html2text
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
#url = "http://data.pr4e.org/romeo.txt"
#url = "https://www.pingree.org/"

while True:
    url = input("\nEnter the full url to the website you'd like to search (done to exit program):\n")
    if url == "done":
        exit()
    else:
        try:
            req = urllib.request.Request(url=url, headers=headers)
            website = urllib.request.urlopen(req)
            if website.getcode() == 200:
                break
            else:
                print("Invalid Input")
        except:
            print("Invalid Input")

o = urllib.parse.urlparse(url)
filename = o.netloc + o.path.replace("/", '|')
f = open(f"raw_{filename}.txt", "w+")

try: 
    req = urllib.request.Request(url=url, headers=headers) 

    with urllib.request.urlopen(req) as response:
        print(f"result code: {response.getcode()}")        
        html = response.read()
        html = html.decode("utf-8") 
        lines = html.splitlines(False)
        for line in lines:
            f.write(f"{line}\n")
     
except Exception as e: 
    print(str(e)) 

f.close()

f = open(f"{filename}.txt", "w+")

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        f.write(f"\nStart tag: {tag}")
        for attr in attrs:
            f.write(f"\n    attr: {attr}")

    def handle_endtag(self, tag):
        f.write(f"\nEnd tag: {tag}")

    def handle_data(self, data):
        f.write(f"\nData: {data}")

    def handle_comment(self, data):
        f.write(f"\nComment: {data}")

    def handle_decl(self, data):
        f.write(f"\nDecl: {data}")

parser = MyHTMLParser()

parser.feed(html)
f.close()

f = open(f"raw_{filename}.txt", "r")
lines = f.readlines()
nf = open(f"searchresults.txt", "w+")
h = html2text.HTML2Text()
h.ignore_links = False
length = len(lines)

for i in range(0, length):
    handledline = h.handle(lines[i])
    if handledline != "" or handledline != "\n":
        nf.write(f"{handledline}\n")

f.close()
nf.close()