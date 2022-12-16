from time import sleep
import requests
import re

"""
name: active crawler

discription:
    simply follows links starting from a few popular websites
    and should hopefully find as many as possible, although
    there are some websites that don't have links to them
    like small personal websites, which I don't know how I
    will get to them. Maby it can find a way into the wayback
    machine or googles list of ips?

version:
    v0.1-tested-unfixed

"""
    
responce_codes = {
    400: "Client error",
    403: "Forbidden",
    404: "Doesn't exist",
    429: "Too many requests"
}

def valid(url: str):
    if re.fullmatch(r'^http[s]?://([A-Za-z0-9\-]*\.[A-Za-z0-9\-]*\.[A-Za-z0-9\-]*(/[A-Za-z0-9\_\-\+\=\%\&\,\/\.\#\;\?\@ ]*$|$|/$)|[A-Za-z0-9\-]*\.[A-Za-z0-9\-]*(/[A-Za-z0-9\_\-\+\=\%\&\,\/\.\#\;\?\@ ]*$|$|/$)|[A-Za-z0-9\-]*\.[A-Za-z0-9\-]*\.[A-Za-z0-9\-]*\.[A-Za-z0-9\-]*(/[A-Za-z0-9\_\-\+\=\%\&\,\/\.\#\;\?\@ ]*$|$|/$)|(?!192\.168)(?!127\.)(?!10\.)(?!172\.(1[6-9]|2[0-9]|3[0-1]))\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(/$|/.*$|$|:\d*$))', url) != None:
        return True
    else:
        return False

def special(url: str):
    if re.fullmatch(r'^(?!http)(ftp|rsync|apple-app|[A-Za-z0-9]*?)://([A-Za-z0-9\_\%\-\?]*\.[A-Za-z0-9\_\%\-\?]*\.[A-Za-z]*|[A-Za-z0-9\_\%\-\?]*\.[A-Za-z]*|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(/.*$|:\d*$|/$|$)', url) != None:
        return True
    else:
        return False

def mailaddr(url: str):
    if re.findall('^[A-Za-z0-9\-\_]*@[A-Za-z0-9\-\_]*(\.[A-Za-z0-9\-\_]*){1,5}$', url) != None:
        return True
    else:
        return False

def mail(url: str):
    for i in re.findall(r'^(mailto):[A-Za-z0-9\-\_]*@[A-Za-z0-9\-\_]*(\.[A-Za-z0-9\-\_]*){1,5}$', url):
        if type(i) == tuple:
            i = i[0]

        addr = re.sub('(mailto):', '', i)

        if mailaddr(addr):
            return addr
        else:
            return False
    return False

invalids = []
specials = []
emails = []
ips = []

class crawler:
    def __init__(self, requestdelay=0, starturls=["example.com"], headers="", returnurls=False):
        if type(starturls) is not list and type(starturls) == str:
            starturls = list(starturls)
        
        for url in starturls:
            if type(url) is not str:
                raise ValueError(f"starturls should contain only strings of urls, {url} of type {type(url)} is not a str")

        if type(requestdelay) is not int and type(requestdelay) is not float:
            raise TypeError(f"requestdelay must be int or float, not {type(requestdelay)}")

        if headers == "":
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
            }
        
        self.starturls = starturls
        self.delay = requestdelay
        self.headers = headers
        self.returnurls = returnurls
    
    class queue:
        def __init__(self, starturls):
            self.que = starturls

        def push(self, url: str):
            self.que.append(url)

        def pop(self):
            return self.que.pop(0)

        def count(self):
            return len(self.que)

        def queued(self):
            return self.que

    class scanner:
        def __init__(self, headers):
            self.headers = headers
        
        def __find_links(self, data, base):
            links = []

            if base.endswith('/'):
                base = base[0:len(base)-1]

            minibase = base

            if '/' in minibase:
                minibase = "http://" + minibase.split('/')[2]

            if minibase.endswith('.'):
                minibase = minibase[0:len(minibase)-1]
            if base.endswith('.'):
                base = base[0:len(base)-1]
            
            for i in re.findall('href=\".*?\"|href=\'.*?\'|src=\'.*?\'|src=\".*?\"', data):
                if len(i) > 2:
                    if i.startswith("href=\"") or i.startswith("href='"):
                        i = i[6:len(i)-1]
                    elif i.startswith("src=\"") or i.startswith("src='"):
                        i = i[5:len(i)-1]
            
                    if valid(i):
                        links.append(i)
                    elif valid(base + i[1:len(i)]):
                        links.append(base + i[1:len(i)])
                    elif valid(base + "/" + i):
                        links.append(base + "/" + i)
                    elif valid(base + i):
                        links.append(base + i)
                    elif valid(minibase + i):
                        links.append(minibase + i)
                    elif valid(minibase + '/' + i):
                        links.append(minibase+'/'+i)
                    elif mail(i):
                        emails.append(i)
                    elif not valid(i):
                        if special(i):
                            if i not in specials:
                                specials.append(i)
                        elif "redirect" in i and not valid(i):
                            if i not in invalids:
                                print("failed to parse redirect")
                        else:
                            if mail(i):
                                if mail(i) not in emails:
                                    emails.append(mail(i))
                            else:
                                if i not in invalids:
                                    print(f"{i} is not valid {not valid(i)}")
                                invalids.append(i)
    
            for i in re.findall('url\((\"|\').*?(\"|\')\)', data):
                if len(i) > 2:
                    i = re.sub('url\((\"|\')|(\"|\')\)', '', i)
                    if valid(base + i):
                        links.append(base + i)
                    elif valid(base + i[1:len(i)]):
                        links.append(base + i[1:len(i)])
                    elif valid(i):
                        links.append(i)
                    elif valid(base + "/" + i):
                        links.append(base + "/" + i)
                    elif valid(base + i):
                        links.append(base + i)
                    elif valid(minibase + i):
                        links.append(minibase + i)
                    elif valid(minibase + '/' + i):
                        links.append(minibase+'/'+i)
                    elif mail(i):
                        emails.append(i)
                    elif not valid(i):
                        if special(i):
                            if i not in specials:
                                specials.append(i)
                        elif "redirect" in i and not valid(i):
                            if i not in invalids:
                                print("failed to parse redirect")
                        else:
                            if mail(i):
                                if mail(i) not in emails:
                                    emails.append(mail(i))
                            else:
                                if i not in invalids:
                                    print(f"{i} is not valid {not valid(i)}")
                                invalids.append(i)
    
            for i in re.findall(r'import((\s|){(.*?\n*)*?}(\s|)from|)(\s|)(\"|\').*?(\"|\');', data):
                if len(i) > 2:
                    if type(i) is not str:
                        continue
                    
                    i = re.sub(r"import(\s|)?(\"|{.*?}(\s|)from\")|\";", "", i)
                    if valid(base + i):
                        links.append(base + i)
                    elif valid(base + i[1:len(i)]):
                        links.append(base + i[1:len(i)])
                    elif valid(i):
                        links.append(i)
                    elif valid(base + "/" + i):
                        links.append(base + "/" + i)
                    elif valid(base + i):
                        links.append(base + i)
                    elif valid(minibase + i):
                        links.append(minibase + i)
                    elif valid(minibase + '/' + i):
                        links.append(minibase+'/'+i)
                    elif mail(i):
                        emails.append(i)
                    elif not valid(i):
                        if special(i):
                            if i not in specials:
                                specials.append(i)
                        elif "redirect" in i and not valid(i):
                            if i not in invalids:
                                print("failed to parse redirect")
                        else:
                            if mail(i):
                                if mail(i) not in emails:
                                    emails.append(mail(i))
                            else:
                                if i not in invalids:
                                    print(f"{i} is not valid {not valid(i)}")
                                invalids.append(i)
                        
            return links
        
        def scan(self, url: str):
            if url.startswith("data:"):
                return ''
            
            try:
                req = requests.get(url, allow_redirects=True, headers=self.headers)
            except requests.exceptions.SSLError:
                print(f"{url} gave a bad SSL certificate                        ")
                invalids.append(url)
                return ''
            except requests.exceptions.InvalidURL:
                print(f"{url} is invalid                            ")
                invalids.append(url)
                return ''
            except requests.exceptions.ConnectionError:
                # removed print due to tons of "cant be connected to"s on older websites
                #print(f"{url} can't be connected to                        ")
                invalids.append(url)
                return ''
            
            if req.status_code != 200:
                invalids.append(url)
                if req.status_code in responce_codes.keys():
                    print(f"{url} {req.status_code}: {responce_codes[req.status_code]}                        ")
                else:
                    print(f"{url} {req.status_code}: UNDEFINED                        ")

            data = req.text
            base = "http://" + re.sub(r'http(s|):\/\/|\/.*', '', req.url)

            if not "Content-Type" in req.headers:
                print(f"{url}'s doesn't have a content type                     ")
                invalids.append(url)
                return ''
                
            type = req.headers["Content-Type"]
            req.close()

            if ';' in type:
                type = type.split(';')[0]

            if ' ' in type:
                type = type.split(' ')[0]

            if type.startswith("image"):
                return ''

            links = self.__find_links(data, base)

            return links

    def start(self):
        queue = self.queue(self.starturls)
        scanner = self.scanner(self.headers)
        processed = 0

        try:
            while True:
                print(f"{processed} urls proccessed, {queue.count()} urls left in queue, and {len(invalids)} invalid urls             ", end="\r")

                if self.delay != 0:
                    sleep(self.delay)
                
                if queue.count() == 0:
                    print('')
                    queue.push(input("ran out of urls, new url: "))
                
                url = queue.pop()  # get top url from queue
                
                if url == '' or url == None or url == "#" or url == "http://#" or url in invalids:
                    continue

                if not valid(url):
                    if special(url):
                        print(f"{url} is special             ")
                        if url not in specials:
                            specials.append(url)
                    elif valid('http://' + url):
                        url = 'http://' + url
                    elif valid("http://" + url.split('//')[len(url.split('//'))-1]):
                        url = "http://" + url.split('//')[len(url.split('//'))-1]
                    else:
                        print(f'{url} is not valid            ')
                        invalids.append(url)
                        continue
    
                urls = scanner.scan(url)  # scan url for more urls
                processed += 1
    
                if urls == '' or len(urls) == 0:  # check that there are any at all
                    if self.delay > 0:
                        sleep(self.delay)
                        
                    continue
                
                for url in urls:

                    if url == "http://#" or url == "#":
                        continue
                    
                    if url in queue.queued():  # if its already in the queue, ignore it
                        if self.delay > 0:
                            sleep(self.delay)
                        
                        continue
    
                    queue.push(url)  # add urls to queue to be scanned
    
                if self.delay > 0:  # if self.delay is set, sleep its value
                    sleep(self.delay)

        except KeyboardInterrupt:
            print(f"{processed} urls proccessed, {queue.count()} urls left in queue, and {len(invalids)} invalid urls                        \n")
            print("finished proccessing, exiting")

            emails = list(dict.fromkeys(emails))

            if len(emails) > 0:
                print(f"\nfound {len(emails)} emails:")
                for i in emails:
                    if "mailto:" in i:
                        i = re.sub(r'^(mailto):', '' 'i')
                    print(i)

            specials = list(dict.fromkeys(specials))
                
            if len(specials) > 0:
                print(f"\nfound {len(specials)} special urls:")
                for i in specials:
                    print(i)

        if self.returnurls:
            return queue.queued
        
crawlbot = crawler()
crawlbot.start()
