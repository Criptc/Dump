from time import sleep
import requests
import re

class crawler:
    def __init__(self, url: str, layers: int, delay=0, redirects=True, stayondomain=False, ignore404=False, autohttp=True, autocom=True, quiet=False, extentions=['all']):
        if type(layers) is not int:
            raise TypeError(f"layers must be of type int \ntype: {type(layers)}\nvalue: {layers}")
        
        if type(delay) is not int and type(delay) is not float:
            raise TypeError("loop_delay_seconds must be of type int or of type float")
        
        if type(redirects) is not bool and type(redirects) is int:
            raise TypeError("redirects is weather to redirect on a 301/2, not how many redirect to do")
        elif type(redirects) is not bool and type(redirects) is not int:
            raise TypeError("redirects must be of type bool")
        
        if type(url) is not str:
                raise TypeError("url must be of type str")
        elif len(url) < 2:
            raise ValueError("url is too short to be a working url")
        elif '.' not in url and autocom:
            url = url + '.com'
        elif '.' not in url and not autocom:
            raise ValueError("url contains no domain extention (ie: .com), enable autocom to automaticlly add .com")
        
        if autohttp:
            if not url.startswith("https://") and not url.startswith("http://"):
                url = "http://" + url

        
        self.url = url
        self.layers = layers
        self.loop_delay_seconds = delay
        self.redirects = redirects
        self.stayondomain = stayondomain
        self.quiet = quiet
        self.unknown_links = []
        self.extentions = extentions
        self.four04 = ignore404

    def find_links(self, html, base):
        links = []
        for i in re.findall('href=\".*?\"|href=\'.*?\'|src=\'.*?\'|src=\".*?\"', html):
            if len(i) > 2:
                if i.startswith("href=\"") or i.startswith("href='"):
                    i = i[6:len(i)-1]  # remove href=" and trailing "
                elif i.startswith("src=\"") or i.startswith("src='"):
                    i = i[5:len(i)-1]  # remove src=" and trailing "
        
                if i.startswith("/"):
                    links.append(base + i)
                elif i.startswith("./"):
                    links.append(base + i[1:len(i)])
                elif i.startswith("http"):
                    links.append(i)
                elif i.startswith("data:image"):
                    links.append(i)
                else:
                    self.unknown_links.append(i)

        for i in re.findall('url\((\"|\').*?(\"|\')\)', html):  # for finding css links
            if len(i) > 2:
                i = re.sub('url\((\"|\')|(\"|\')\)', '', i)
                if i.startswith("/"):
                    links.append(base + i)
                elif i.startswith("./"):
                    links.append(base + i[1:len(i)])
                elif i.startswith("http"):
                    links.append(i)
                elif i.startswith("data:image"):
                    links.append(i)

        for i in re.findall('import((\s|){(.*?\n*)*?}(\s|)from|)(\s|)(\"|\').*?(\"|\');', html):  # for finding js links
            if len(i) > 2:
                i = re.sub("import(\s|)?(\"|{.*?}(\s|)from\")|\";", "", i)
                if i.startswith("/"):
                    links.append(base + i)
                elif i.startswith("./"):
                    links.append(base + i[1:len(i)])
                elif i.startswith("http"):
                    links.append(i)
                elif i.startswith("data:image"):
                    links.append(i)
                else:
                    self.unknown_links.append(i)
        
        return links

    def find_type(self, link: str):
        req = requests.get(link, allow_redirects=self.redirects)
        type = req.headers["Content-Type"]
        stat = req.status_code
        req.close()
    
        if ";" in type:
            type = type.split(';')[0]
        
        if type == "text/html":
            return "htm", stat
        elif type == "text/javascript" or type == "application/javascript":
            return "js", stat
        elif type.startswith("image"):
            return "img", stat
        elif type == "text/css":
            return "css", stat
        else:
            return "other", stat

    def layer(self, linklist: list):
        htmllinks = []
        jslinks = []
        csslinks = []
        imagelinks = []
        otherlinks = []
        num = 0
        percent = 0
            
        for url in linklist:
            if url.startswith("data:image"):
                imagelinks.append(url)
                num += 1
                if not self.quiet:
                    percent = round((num / len(linklist)) * 100, 1)
                    print(f"making requests: {num}/{str(len(linklist))}   {str(percent)}%          ", end="\r")
            else:
                type, stat = self.find_type(url)

                if not stat == 404:
                    if type == 'htm':
                        htmllinks.append(url)
                    elif type == 'js':
                        jslinks.append(url)
                    elif type == "css":
                        csslinks.append(url)
                    elif type == 'img':
                        imagelinks.append(url)
                    elif type == 'other':
                        otherlinks.append(url)
            
                if self.loop_delay_seconds > 0:
                    sleep(self.loop_delay_seconds)
                num += 1
                if not self.quiet:
                    percent = round((num / len(linklist)) * 100, 1)
                    print(f"making requests: {num}/{str(len(linklist))}   {str(percent)}%          ", end="\r")
        
        if not self.quiet:
            print('')
            return htmllinks, jslinks, csslinks, imagelinks, otherlinks
    
    def loop(self, lnks: list):
        n = 0
        newlinks = []
        html_links, js_links, css_links, image_links, other_links = self.layer(lnks)
    
        for url in js_links:
            if self.stayondomain:
                if self.check not in url:
                    continue
            if self.loop_delay_seconds > 0:
                sleep(self.loop_delay_seconds)
            req = requests.get(url, allow_redirects=self.redirects)
            js = req.text
            base = req.url[0:len(req.url)-1]
            req.close()
            lnks = self.find_links(js, base)
            for i in lnks:
                newlinks.append(i)
                n += 1
                if not self.quiet:
                    print(f"links found: {n} type: javascript              ", end="\r")
    
        for url in html_links:
            if self.stayondomain:
                if self.check not in url:
                    continue
            if self.loop_delay_seconds > 0:
                sleep(self.loop_delay_seconds)
            req = requests.get(url, allow_redirects=self.redirects)
            html = req.text
            base = req.url[0:len(req.url)-1]
            req.close()
            lnks = self.find_links(html, base)
            for i in lnks:
                newlinks.append(i)
                n += 1
                if not self.quiet:
                    print(f"links found: {n} type: html              ", end="\r")

        for url in css_links:
            if self.stayondomain:
                if self.check not in url:
                    continue
            if self.loop_delay_seconds > 0:
                sleep(self.loop_delay_seconds)
            req = requests.get(url, allow_redirects=self.redirects)
            css = req.text
            base = req.url[0:len(req.url)-1]
            req.close()
            lnks = self.find_links(css, base)
            for i in lnks:
                newlinks.append(i)
                n += 1
                if not self.quiet:
                    print(f"links found: {n} type: css              ", end="\r")

        newlinks = list(dict.fromkeys(newlinks))  # remove duplicits
        if not self.quiet:
            print('')
        return newlinks

    def start(self):
        req = requests.get(self.url, allow_redirects=self.redirects)
        html = req.text
        self.ogbase = req.url[0:len(req.url)-1]
        
        self.check = re.sub("http(s|)://|/.*", "", self.ogbase).split('.')
        if len(self.check) == 3:
            self.check = ".".join(self.check[1:len(self.check)])
        elif len(self.check) == 2:
            self.check = ".".join(self.check)
            
        req.close()

        if self.stayondomain:
            lnkst = self.find_links(html, self.ogbase)
            lnks = []
            for i in lnkst:
                if self.check in i:
                    lnks.append(i)
            del lnkst
        else:
            lnks = self.find_links(html, self.ogbase)
        
        if len(lnks) <= 0:
            print("no links found in base page\does this page have any links?\nif stayondomain is true, are all the links not on this domain?")
            return

        links = list(dict.fromkeys(lnks))  # remove duplicits

        if not self.quiet:
            print(f"{len(links)} links found in start page\n")
            print(f"{'' if self.layers == 0 else f'looping {self.layers} time(s)'}\n")
            
        if self.layers > 0:
            for _ in range(self.layers):
                newlinks = self.loop(links)
                for i in newlinks:
                    if self.stayondomain:
                        if self.check in i:
                            links.append(i)
                    else:
                        links.append(i)

                if not self.quiet:
                    print(f"{len(newlinks)} links found this loop")
                    
                if self.loop_delay_seconds > 0:
                    sleep(self.loop_delay_seconds)
                elif not self.quiet:
                    print("\n")

            if not self.quiet:
                print(f"{len(links)} total links found")

            if "all" not in self.extentions:
                lnks = []
                num = 0
                for ex in self.extentions:
                    for url in links:
                        if url.endswith('.' + ex):
                            lnks.append(url)
                    
                        if not self.quiet:
                            percent = round(num / (len(links)*len(self.extentions)) * 100, 1)
                            print(f"sorting types... {num}/{len(links)*len(self.extentions)}   {str(percent)}%          ", end="\r")
                            num += 1

                if not self.quiet:
                    print('\n')
                    print(f'{len(links)-len(lnks)} links filtered out, {len(lnks)} links found')
                    
                return lnks
            
            return links
        else:
            if "all" not in self.extentions:
                lnks = []
                num = 0
                for ex in self.extentions:
                    for url in links:
                        if url.endswith('.' + ex):
                            lnks.append(url)
                    
                        if not self.quiet:
                            percent = round(num / (len(links)*len(self.extentions)) * 100, 1)
                            print(f"sorting types... {num}/{len(links)*len(self.extentions)}   {str(percent)}%          ", end="\r")
                            num += 1

                if not self.quiet:
                    print('\n')
                    print(f'{len(links)-len(lnks)} links filtered out, {len(lnks)} links found')
                    
                return lnks
            
            return links

if __name__ == "__main__":
    test = crawler("github.com", 2, quiet=False, stayondomain=True, extentions=["exe", "py", "png", "jpg"])
    links = test.start()
    print(links)    
