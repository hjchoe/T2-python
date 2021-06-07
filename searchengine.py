# James Choe
# Assignment 4.5.1- Final Week's project
# 3/12/2021

import urllib.request
import html2text
import re
from colorama import Fore, Back, Style

try:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

    def get_website_url():
        while True:
            url = input(Fore.BLUE + "\nEnter the full url to the website you'd like to search (done to exit program):\n" + Fore.WHITE)
            if url == "done":
                exit()
            else:
                try:
                    print(Fore.MAGENTA + "\nAttempting Connection...")
                    req = urllib.request.Request(url=url, headers=headers)
                    website = urllib.request.urlopen(req)
                    if website.getcode() == 200:
                        print(Fore.GREEN + "Connection Successful")
                        break
                    else:
                        print(Fore.RED + "Connection Failed")
                except:
                    print(Fore.RED + "Invalid Input")
        return url

    def fetch_website_data(url):
        try: 
            req = urllib.request.Request(url=url, headers=headers) 

            with urllib.request.urlopen(req) as response:
                print(Fore.MAGENTA + f"\nresult code: " + Fore.YELLOW + f"{response.getcode()}\n")   
                html = response.read()
                html = html.decode("utf-8") 
                lines = html.splitlines(False)
                print(Fore.GREEN + f"Fetched Data Successfully\n")
                return lines
        except Exception as e: 
            print(Fore.RED + str(e)) 
            return None

    def write_website_data(lines):
        f = open(f"websiteresults.txt", "w+", encoding='UTF-8')
        raw = open(f"rawresults.txt", "w+", encoding='UTF-8')
        h = html2text.HTML2Text()
        h.ignore_links = False
        length = len(lines)

        for i in range(0, length):
            try:
                raw.write(f"{lines[i]}\n")
            except:
                print(Fore.RED + f"error writing line:\n{Fore.WHITE}{lines[i]}")
            handledline = h.handle(lines[i])
            #handledline = handledline.replace("\n", '')
            if handledline != "":
                try:
                    f.write(f"{handledline}\n")
                except:
                    print(Fore.RED + f"error writing line:\n{Fore.WHITE}{handledline}")
        f.close()
        raw.close()
        print(Fore.CYAN + f"Finished saving website data to database txt file: {Fore.YELLOW}websiteresults.txt\n")

    def get_search_target():
        target = input(Fore.BLUE + "\nEnter what you want to search the website for (done to exit program):\n" + Fore.WHITE)
        if target == "done":
            exit()
        return target

    def fetch_search_data(target):
        print(Fore.MAGENTA + f"\nSearching for {Fore.YELLOW}{target}{Fore.MAGENTA}...")
        
        f = open(f"websiteresults.txt", "r")
        file = f.readlines()

        exact_matches = []
        exact_match_count = 0
        close_matches = []
        close_match_count = 0
        i = 1
        for line in file:
            if re.search(target, line, re.IGNORECASE):
                exact_matches.append(f"{line}:::{i}")
                exact_match_count += 1
            else:
                words = target.split(" ")
                for word in words:
                    if re.search(word, line, re.IGNORECASE):
                        close_matches.append(f"{line}:::{word}:::{i}")
                        close_match_count += 1
                        break
            i += 1
        print(Fore.MAGENTA + f"Found {Fore.YELLOW}{exact_match_count}{Fore.MAGENTA} exact matches and {Fore.YELLOW}{close_match_count}{Fore.MAGENTA} close matches")
        return exact_matches, exact_match_count, close_matches, close_match_count

    def write_search_data(url, target, exact, close):
        f = open(f"searchresults.txt", "w+", encoding='UTF-8')
        
        f.write(f"[ Info ]\n\nWebsite:\n   {url}\nSearch Target:\n   {target}")

        f.write(f"\n\n[ Exact Matches ]")
        for match in exact:
            matchinfo = match.split(":::")
            f.write(f"\n  Line: {matchinfo[1]}\n  Result:\n    {matchinfo[0]}")

        f.write(f"\n\n[ Close Matches ]")
        for match in close:
            matchinfo = match.split(":::")
            f.write(f"\n  Line: {matchinfo[2]}\n  Word in Target:\n    {matchinfo[1]}\n  Result:\n    {matchinfo[0]}")

        f.close()
        print(Fore.CYAN + f"\nFinished saving search data to database txt file: {Fore.YELLOW}searchresults.txt\n")

    def filter_google_search(url, target):
        print(Fore.MAGENTA + f"\nFiltering google search results for {Fore.YELLOW}{target}{Fore.MAGENTA}...")
        f = open(f"searchresults.txt", "w+", encoding='UTF-8')
        rf = open(f"websiteresults.txt", "r", encoding='UTF-8')

        f.write(f"[ Info ]\n\nWebsite:\n   {url}\nGoogle Search Target:\n   {target}")
        f.write(f"\n\n[ Results ]\n")

        lines = rf.readlines()
        length = len(lines)
        num_results = 0
        for i in range(0, length):
            if lines[i].startswith("### "):
                f.write(f"\n{lines[i]}")
                j = 1
                while i+j < length and lines[i+j] != "[\n" and not lines[i+j].startswith("Related searches") and not lines[i+j].startswith("##"):
                    f.write(f"  {lines[i+j]}")
                    j += 1
                num_results += 1
        
        f.write(f"\n\n[ Related Searches ]\n")

        num_related = 0
        for i in range(0, length):
            if lines[i].startswith("Related searches"):
                j = 1
                while i+j < length and lines[i+j] != "[\n" and not lines[i+j].startswith("###") and not lines[i+j].startswith("[Next >]") and not lines[i+j].startswith("[Images]"):
                    f.write(f"  {lines[i+j]}")
                    j += 1
                num_related += 1

        f.close()
        rf.close()

        print(Fore.MAGENTA + f"Found {Fore.YELLOW}{num_results}{Fore.MAGENTA} results and {Fore.YELLOW}{num_related}{Fore.MAGENTA} related search sections")
        print(Fore.CYAN + f"\nFinished saving filtered search data to database txt file: {Fore.YELLOW}searchresults.txt\n" + Fore.WHITE)

    def filter_wiki_invalid():
        raw = open("rawresults.txt", "r", encoding='UTF-8')
        lines = raw.readlines()
        length = len(lines)
        for i in range(0, length):
            line = lines[i]
            if line.startswith("<i>The page "):
                resultline = line
                break
        results = resultline.split("<li class='mw-search-result'><div class='mw-search-result-heading'>")
        results.pop(0)
        print(Fore.MAGENTA + f"\nResults:\n")
        for result in results:
            result = result.replace("&quot;", "\"")
            result = result.replace("&amp;", "&")
            linkindex = result.find("<a href=\"")+9
            i = 1
            while result[linkindex + i] != "\"":
                i += 1
            link = f"https://en.wikipedia.org{result[linkindex:linkindex+i]}"
            
            titleindex = result.find("title=\"")+7
            i = 1
            while result[titleindex + i] != "\"":
                i += 1
            title = result[titleindex:titleindex+i]

            descindex1 = result.find("<div class='searchresult'>")+26
            i = 1
            while result[descindex1 + i] != "<":
                i += 1
            desc1 = result[descindex1:descindex1+i]
            
            garbindex = result.find("<span class=\"searchmatch\">")+26
            i = 1
            while result[garbindex + i] != ">":
                i += 1
            descindex2 = garbindex + i + 1
            i = 1
            while result[descindex2 + i] != "<":
                i += 1
            desc2 = result[descindex2:descindex2+i]

            print(f"{Fore.YELLOW}{title}:\n{Fore.BLUE}{link}\n{Fore.CYAN}{desc1}{desc2}\n" + Fore.WHITE)


    def filter_wiki_valid():
        s = open("searchresults.txt", "w+")
        raw = open("rawresults.txt", "r", encoding='UTF-8')
        lines = raw.readlines()
        length = len(lines)
        resultlines = []
        for i in range(0, length):
            line = lines[i]
            if f"</table>" in line and f"<p>" in lines[i+1]:
                resultlines.append(lines[i+1])

        links = []
        for i in range(0, length):
            line = lines[i]
            linkindex = line.find("/wiki")
            if linkindex != -1:
                j = 0
                end = ["\"", ">", "\n"]
                while linkindex+j < len(line) and line[linkindex + j] not in end:
                    j += 1
                line = line.replace("\n", "")
                link = f"https://en.wikipedia.org{line[linkindex:linkindex+j]}"
                if link not in links:
                    links.append(link)
                    s.write(link)
        print(Fore.MAGENTA + "\nLinks:\n")
        for link in links:
            print(f"{Fore.CYAN}{link}")


    # MAIN
    def search_document(url):
        search_target = get_search_target()
        exact, exactN, close, closeN = fetch_search_data(search_target)
        write_search_data(url, search_target, exact, close)

    def google_search():
        target = input(Fore.BLUE + "\nEnter what you want to search google for (done to exit program):\n" + Fore.WHITE)
        if target == "done":
            exit()
        utarget = target.replace(" ", "%20")
        url = f"https://www.google.com/search?q={utarget}"
        lines = fetch_website_data(url)
        write_website_data(lines)
        filter_google_search(url, target)

    def website_search():
        while True:
            url = input(Fore.BLUE + "\nEnter the full url to the website you'd like to search (done to exit program):\n" + Fore.WHITE)
            if url == "done":
                exit()
            else:
                try:
                    print(Fore.MAGENTA + "\nAttempting Connection...")
                    req = urllib.request.Request(url=url, headers=headers)
                    website = urllib.request.urlopen(req)
                    if website.getcode() == 200:
                        print(Fore.GREEN + "Connection Successful")
                        break
                    else:
                        print(Fore.RED + "Connection Failed")
                except:
                    print(Fore.RED + "Invalid Input")
        lines = fetch_website_data(url)
        write_website_data(lines)
        search_document(url)

    def wiki_search():
        target = input(Fore.BLUE + "\nEnter what you want to search wikipedia for (done to exit program):\n" + Fore.WHITE)
        if target == "done":
            exit()
        utarget = target.replace(" ", "_")
        url = f"https://en.wikipedia.org/wiki/{utarget}"
        lines = fetch_website_data(url)
        if lines == None:
            print(Fore.RED + f"\nThere was no wikipedia page called: {Fore.YELLOW}{utarget}\n" + Fore.MAGENTA + f"searching for similar results...")
            url = f"https://en.wikipedia.org/w/index.php?search={utarget}"
            lines = fetch_website_data(url)
            write_website_data(lines)
            filter_wiki_invalid()
        else:
            write_website_data(lines)
            filter_wiki_valid()
        

    while True:
        type = input(Fore.BLUE + "\nWould you like to search a website, google, or wikipedia (done to exit program):\n" + Fore.WHITE)
        if type == "done":
            exit()
        elif type == "google":
            google_search()
        elif type == "website":
            website_search()
        elif type == "wikipedia":
            wiki_search()
        else:
            print(Fore.RED + "Invalid Type")
except KeyboardInterrupt:
    print(Style.RESET_ALL)
except SystemExit:
    print(Style.RESET_ALL)