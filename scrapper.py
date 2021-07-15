import argparse
import urllib.request, urllib.parse
from bs4 import BeautifulSoup
from random import randint

class proxyScrapeSocks4:
    def __init__(self, url):
        if(arguments.verbose):
            print('[!]Scraping ' + url + '[!]')
        req = urllib.request.Request(url, headers= {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'})
        with urllib.request.urlopen(req) as response:
            string = response.read()
            string = string.decode("utf8")

        if(url == 'https://www.socks4proxylist.xyz/'):
            string = string[string.find('<span style="white-space: pre-line;">IP:PORT') + len('<span style="white-space: pre-line;">IP:PORT') : len(string)]
            string = string[0 : string.find('</span></span></div>')]
            string = string.split('\n')
            
            proxies = string[1 : len(string) - 1]
            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i + '\n')
            
            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url.find('https://www.proxylist.live/dashboard/socks4') != -1):
            soup = BeautifulSoup(string, features="html.parser")
            proxies = []
            for i in soup.find_all(attrs={'class': 'table-'}):
                text = i.find_all('td')
                proxies.append(text[1].text + ':' + text[2].text)

            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i.strip(' ') + '\n')
            
            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')
        
        elif(url == 'https://hidemy.name/es/proxy-list/?type=4#list'):
            soup = BeautifulSoup(string, features="html.parser")
            proxies = []
            tables = soup.find_all('tr')
            tables = tables[1 : len(tables)]

            for i in tables:
                elements = i.find_all('td')
                proxies.append(str(elements[0])[4 : len(str(elements[0])) - 5] + ':' + str(elements[1])[4 : len(str(elements[1])) - 5])

            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i.strip(' ') + '\n')

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url == 'https://github.com/TheSpeedX/PROXY-List/blob/master/socks4.txt'):
            soup = BeautifulSoup(string, features="html.parser")
            proxies = []
            for i in soup.find_all('tr'):
                proxies.append(i.text.strip('\n\t ') + '\n')

            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')
            
            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i)

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url == 'https://www.proxyscan.io/'):
            soup = BeautifulSoup(string, features="html.parser")
            cntx = soup.find(attrs={'id' : 'loadPage'})
            proxies = []
        
            for i in cntx.find_all('tr'):
                if(i.find_all('td')[3].text.find('SOCKS4') != -1  or i.find_all('td')[3].text.find('SOCKS5,SOCKS4') != -1):
                    proxies.append(str(i.find('th').text) + ':' + str(i.find_all('td')[0].text) + '\n')

            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i)

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url == 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all'):
            proxies = string.split('\r')
            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i)

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url == 'https://www.proxy-list.download/api/v1/get?type=socks4'):
            proxies = string.split('\r')
            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i)

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url == 'https://www.proxyscan.io/api/proxy?last_check=50000&format=txt&limit=20type=socks4'):
            proxies = string.split('\r')
            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i)

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')
                    
        elif(url == 'https://www.proxynova.com/proxy-server-list/'):
            soup = BeautifulSoup(string, features="html.parser")
            main = soup.find('tbody')
            proxies = []
            for i in main.find_all('tr'):
                try:
                    rows = i.find_all('td')
                    abbr = str(rows[0].find('abbr'))
                    proxies.append(abbr[abbr.find("<script>document.write('") + len("<script>document.write('") : abbr.find("');</script>")] + ':' + str(rows[1].text.strip(' \n\t\r')))
                except:
                    pass

            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i + '\n')

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')
                


class proxyScrapeSocks5:
    def __init__(self, url):
        if(arguments.verbose):
            print('[!]Scraping ' + url + '[!]')
        
        req = urllib.request.Request(url, headers= {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'})
        with urllib.request.urlopen(req) as response:
            string = response.read()
            string = string.decode("utf8")

        if(url == 'https://www.socks5proxylist.xyz/'):
            string = string[string.find('<span style="white-space: pre-line;">IP:PORT') + len('<span style="white-space: pre-line;">IP:PORT') : len(string)]
            string = string[0 : string.find('</span></span></div>')]
            string = string.split('\n')
            
            proxies = string[1 : len(string) - 1]
            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i + '\n')
            
            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url.find('https://www.proxylist.live/dashboard/socks5') != -1):
            soup = BeautifulSoup(string, features="html.parser")
            proxies = []
            for i in soup.find_all(attrs={'class': 'table-'}):
                text = i.find_all('td')
                proxies.append(text[1].text + ':' + text[2].text)

            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i.strip(' ') + '\n')
            
            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')
        
        elif(url == 'https://hidemy.name/es/proxy-list/?type=5#list'):
            soup = BeautifulSoup(string, features="html.parser")
            proxies = []
            tables = soup.find_all('tr')
            tables = tables[1 : len(tables)]

            for i in tables:
                elements = i.find_all('td')
                proxies.append(str(elements[0])[4 : len(str(elements[0])) - 5] + ':' + str(elements[1])[4 : len(str(elements[1])) - 5])

            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i.strip(' ') + '\n')

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url == 'https://github.com/TheSpeedX/PROXY-List/blob/master/socks5.txt'):
            soup = BeautifulSoup(string, features="html.parser")
            proxies = []
            for i in soup.find_all('tr'):
                proxies.append(i.text.strip('\n\t ') + '\n')

            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')
            
            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i)

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url == 'https://www.proxyscan.io/'):
            soup = BeautifulSoup(string, features="html.parser")
            cntx = soup.find(attrs={'id' : 'loadPage'})
            proxies = []
        
            for i in cntx.find_all('tr'):
                if(i.find_all('td')[3].text.find('SOCKS5') != -1 or i.find_all('td')[3].text.find('SOCKS5,SOCKS4') != -1):
                    proxies.append(str(i.find('th').text) + ':' + str(i.find_all('td')[0].text) + '\n')

            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i)

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url == 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all'):
            proxies = string.split('\r')
            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i)

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url == 'https://www.proxy-list.download/api/v1/get?type=socks5'):
            proxies = string.split('\r')
            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i)

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url == 'https://www.proxyscan.io/api/proxy?format=txt&limit=20type=socks5'):
            proxies = string.split('\r')
            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i)

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url == 'https://spys.one/en/socks-proxy-list/'):
            soup = BeautifulSoup(string, features="html.parser")
            rows = soup.find_all(attrs={'onmouseover' : "this.style.background='#002424'"})
            proxies = []
            for i in rows:
                tds = i.find_all('td')
                if(tds[1].text == 'SOCKS5'):
                    proxies.append(tds[0].text)

            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i + '\n')

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')



class proxyScrapeHttp:
    def __init__(self, url):
        if(arguments.verbose):
            print('[!]Scraping ' + url + '[!]')
        
        req = urllib.request.Request(url, headers= {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'})
        with urllib.request.urlopen(req) as response:
            string = response.read()
            string = string.decode("utf8")

        if(url == 'https://free-proxy-list.net/'):
            soup = BeautifulSoup(string, features="html.parser")
            proxies = []
            main = soup.find('tbody')
            for i in main.find_all('tr'):
                rows = i.find_all('td')
                proxies.append(rows[0].text + ':' + rows[1].text)

            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i + '\n')
            
            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url.find('https://www.proxylist.live/dashboard/proxylist') != -1):
            soup = BeautifulSoup(string, features="html.parser")
            proxies = []
            for i in soup.find_all(attrs={'class': 'table-default'}):
                text = i.find_all('td')
                proxies.append(text[1].text + ':' + text[2].text)
                

            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i.strip(' ') + '\n')
            
            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')
        
        elif(url == 'https://hidemy.name/es/proxy-list/?type=h#list'):
            soup = BeautifulSoup(string, features="html.parser")
            proxies = []
            tables = soup.find_all('tr')
            tables = tables[1 : len(tables)]

            for i in tables:
                elements = i.find_all('td')
                proxies.append(str(elements[0])[4 : len(str(elements[0])) - 5] + ':' + str(elements[1])[4 : len(str(elements[1])) - 5])

            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i.strip(' ') + '\n')

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url == 'https://github.com/TheSpeedX/PROXY-List/blob/master/http.txt'):
            soup = BeautifulSoup(string, features="html.parser")
            proxies = []
            for i in soup.find_all('tr'):
                proxies.append(i.text.strip('\n\t ') + '\n')

            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')
            
            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i)

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url == 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all'):
            proxies = string.split('\r')
            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i)

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url == 'https://www.proxy-list.download/api/v1/get?type=http'):
            proxies = string.split('\r')
            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i)

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url == 'https://www.proxyscan.io/api/proxy?format=txt&limit=20type=http'):
            proxies = string.split('\r')
            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i)

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

        elif(url == 'https://spys.one/en/https-ssl-proxy/'):
            soup = BeautifulSoup(string, features="html.parser")
            rows = soup.find_all(attrs={'onmouseover' : "this.style.background='#002424'"})
            proxies = []
            for i in rows:
                tds = i.find_all('td')
                proxies.append(tds[0].text)

            if(arguments.verbose):
                print('[i]Scraped proxies length: ' + str(len(proxies)) + '[i]\n[i]Saving proxies[i]')

            with open(arguments.output + '.txt', 'a') as file:
                for i in proxies:
                    file.write(i + '\n')

            if(arguments.verbose):
                print('[+]All proxies saved[+]\n')

                
                

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--verbose', dest = "verbose", help = "Gives information during the process", default = False, type = bool)
    parser.add_argument('-o', '--output', dest = "output", help = "Modify the output file name", default = "output", type = str)
    parser.add_argument('-p', '--proxy', dest = "proxy", help = "Selects the proxy type (socks4, socks5, http)", required = True)

    arguments = parser.parse_args()

    socks4 = ['https://www.socks4proxylist.xyz/', 'https://sockslist.net/proxy/server-socks-hide-ip-address#proxylist', 'https://www.proxynova.com/proxy-server-list/', 'https://www.proxyscan.io/api/proxy?last_check=50000&format=txt&limit=20type=socks4', 'https://www.proxy-list.download/api/v1/get?type=socks4', 'https://hidemy.name/es/proxy-list/?type=4#list', 'https://github.com/TheSpeedX/PROXY-List/blob/master/socks4.txt', 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all', 'https://www.proxyscan.io/', 'https://www.proxylist.live/dashboard/socks4', 'https://www.proxylist.live/dashboard/socks4?page=2', 'https://www.proxylist.live/dashboard/socks4?page=3', 'https://www.proxylist.live/dashboard/socks4?page=4', 'https://www.proxylist.live/dashboard/socks4?page=5', 'https://www.proxylist.live/dashboard/socks4?page=6', 'https://www.proxylist.live/dashboard/socks4?page=7', 'https://www.proxylist.live/dashboard/socks4?page=8', 'https://www.proxylist.live/dashboard/socks4?page=9', 'https://www.proxylist.live/dashboard/socks4?page=10', 'https://www.proxylist.live/dashboard/socks4?page=11', 'https://www.proxylist.live/dashboard/socks4?page=12', 'https://www.proxylist.live/dashboard/socks4?page=13', 'https://www.proxylist.live/dashboard/socks4?page=14', 'https://www.proxylist.live/dashboard/socks4?page=15', 'https://www.proxylist.live/dashboard/socks4?page=16', 'https://www.proxylist.live/dashboard/socks4?page=17', 'https://www.proxylist.live/dashboard/socks4?page=18', 'https://www.proxylist.live/dashboard/socks4?page=19', 'https://www.proxylist.live/dashboard/socks4?page=20', 'https://www.proxylist.live/dashboard/socks4?page=21']
    socks5 = ['https://spys.one/en/socks-proxy-list/', 'https://github.com/TheSpeedX/PROXY-List/blob/master/socks5.txt', 'https://www.socks5proxylist.xyz/', 'https://www.proxylist.live/dashboard/socks5?', 'https://hidemy.name/es/proxy-list/?type=5#list', 'https://www.proxyscan.io/api/proxy?format=txt&limit=20type=socks5', 'https://www.proxy-list.download/api/v1/get?type=socks5', 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all', 'https://www.proxyscan.io/', 'https://www.proxylist.live/dashboard/socks5?page=2', 'https://www.proxylist.live/dashboard/socks5?page=3', 'https://www.proxylist.live/dashboard/socks5?page=4', 'https://www.proxylist.live/dashboard/socks5?page=5' 'https://www.proxylist.live/dashboard/socks5?page=6']
    http = ['https://free-proxy-list.net/', 'https://spys.one/en/https-ssl-proxy/', 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all', 'https://www.proxy-list.download/api/v1/get?type=http', 'https://www.proxyscan.io/api/proxy?format=txt&limit=20type=http', 'https://hidemy.name/es/proxy-list/?type=h#list', 'https://github.com/TheSpeedX/PROXY-List/blob/master/http.txt', 'https://www.proxylist.live/dashboard/proxylist?page=1', 'https://www.proxylist.live/dashboard/proxylist?page=2', 'https://www.proxylist.live/dashboard/proxylist?page=3', 'https://www.proxylist.live/dashboard/proxylist?page=4', 'https://www.proxylist.live/dashboard/proxylist?page=5', 'https://www.proxylist.live/dashboard/proxylist?page=6', 'https://www.proxylist.live/dashboard/proxylist?page=7', 'https://www.proxylist.live/dashboard/proxylist?page=8', 'https://www.proxylist.live/dashboard/proxylist?page=9', 'https://www.proxylist.live/dashboard/proxylist?page=10', 'https://www.proxylist.live/dashboard/proxylist?page=11', 'https://www.proxylist.live/dashboard/proxylist?page=12', 'https://www.proxylist.live/dashboard/proxylist?page=13', 'https://www.proxylist.live/dashboard/proxylist?page=14', 'https://www.proxylist.live/dashboard/proxylist?page=15', 'https://www.proxylist.live/dashboard/proxylist?page=16', 'https://www.proxylist.live/dashboard/proxylist?page=17', 'https://www.proxylist.live/dashboard/proxylist?page=18', 'https://www.proxylist.live/dashboard/proxylist?page=19', 'https://www.proxylist.live/dashboard/proxylist?page=20', 'https://www.proxylist.live/dashboard/proxylist?page=21']


    if(arguments.proxy == "socks4"):
        if(arguments.verbose):
            print('[i]Scraping started (' + arguments.proxy + ')[i]')
        for i in socks4:
            proxyScrapeSocks4(i)
    elif(arguments.proxy == "socks5"):
        if(arguments.verbose):
            print('[i]Scraping started (' + arguments.proxy + ')[i]')
        for i in socks5:
            proxyScrapeSocks5(i)
    elif(arguments.proxy == "http"):
        if(arguments.verbose):
            print('[i]Scraping started (' + arguments.proxy + ')[i]')
        for i in http:
            proxyScrapeHttp(i)
    else:
        print("[-]INVALID PROXY FORMAT: " + arguments.proxy + "[-]")
        print("-Accepted formats: socks4|socks5|http")