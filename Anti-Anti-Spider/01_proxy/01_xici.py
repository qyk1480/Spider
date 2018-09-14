import requests
from bs4 import BeautifulSoup
import json
import pymysql


def xiciproxy():
    url = 'http://www.xicidaili.com/nn/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')

    ip_port = []
    table = soup.find('table', attrs={'id': 'ip_list'}).find_all('tr')
    for ipList in table[1:]:
        ip = ipList.find_all('td')[1].get_text()
        port = ipList.find_all('td')[2].get_text()
        http = ipList.find_all('td')[5].get_text().lower()
        # ip_port.append([http, ip, port])
        ip_port.append('%s://%s:%s' % (http, ip, port))
    # print(ip_port)
    return ip_port

def verify(ip_port):
    verified = []

    for ip in ip_port:
        if ip.startswith('https'):
            print(ip)
            url = 'https://www.ipip.net/'
            proxy = 'http://' + ip[8:]
            proxies = {'https': proxy}
            try:
                response = requests.get(url, proxies=proxies)
                html = response.text
                soup = BeautifulSoup(html, 'lxml')
                htmlip = soup.find('div', attrs={'class', 'yourInfo'}).find('li').find('a').get_text()
                print(htmlip)
                ip = ip[8:]
                if ip.startswith(htmlip):
                    ip, port = ip.split(':')
                    verified.append(['https', ip, port])
                    print(verified)
            except:
                pass
        else:
            url = 'http://icanhazip.com/'
            print(ip)
            proxies = {'http': ip}
            try:
                response = requests.get(url, proxies=proxies)
                html = response.text
                print(html)
                ip = ip[7:]
                if ip.startswith(html.strip()):
                    ip, port = ip.split(':')
                    verified.append(['http', ip, port])
                    print(verified)
            except:
                pass
    return verified

def proxy2mysql(verifiedip):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='spider', charset='utf8')
    cur = conn.cursor()
    for ip in verifiedip:
        sql = 'insert into xici(protocol, ip, port) values (%s, %s, %s)'
        cur.execute(sql, ip)
        conn.commit()
    cur.close()
    conn.close()


def main():
    ip_port = xiciproxy()
    verifiedip = verify(ip_port)
    proxy2mysql(verifiedip)

if __name__ == '__main__':
    main()
    