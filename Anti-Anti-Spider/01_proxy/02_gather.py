import requests
from bs4 import BeautifulSoup
import json
import pymysql
import re

def gatherproxy():
    url = 'http://www.gatherproxy.com/zh/proxylist/country/?c=China'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    response = requests.get(url, headers=headers)
    html = response.text
    # print(html)

    ip_port = []
    list_rule = re.compile(r'insertPrx\(.*?\);')
    ip_list = list_rule.findall(html)
    # print(ip_list)

    ip_rule = re.compile(r'"PROXY_IP":"(.*?)"')
    port_rule = re.compile(r'"PROXY_PORT":"(.*?)"')
    for ipstr in ip_list:
        ip = ip_rule.findall(ipstr)[0]
        portOx = port_rule.findall(ipstr)[0]
        port = hex2int(portOx)
        ip_port.append('http://%s:%s' % (ip, port))
    print(ip_port)
    return ip_port

def hex2int(portOx):
    b = [0,0,0,0]
    for i in range(len(portOx)):
        try:
            b[i] = int(portOx[i])
        except:
            b[i] = ord(portOx[i]) - 55

        else:
            b[i] = int(portOx[i])

    if len(portOx) == 2:
        port = 16*b[0] + b[1]
    elif len(portOx) == 3:
        port = 16*16*b[0] + 16*b[1] + b[2]
    elif len(portOx) == 4:
        port = 16*16*16*b[0] + 16*16*b[1] + 16*b[2] + b[3]

    return port

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
        sql = 'insert into gather(protocol, ip, port) values (%s, %s, %s)'
        cur.execute(sql, ip)
        conn.commit()
    cur.close()
    conn.close()


def main():
    ip_port = gatherproxy()
    verifiedip = verify(ip_port)
    proxy2mysql(verifiedip)

if __name__ == '__main__':
    main()
    