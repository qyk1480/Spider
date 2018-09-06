import requests
from retrying import retry

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}


@retry(stop_max_attempt_number=3)
def _parse_url(url):
    print('*'*10)
    response = requests.get(url, headers=headers, timeout=5)
    return response.content.decode()


def parse_url(url):
    try:
        html_str = _parse_url(url)

    except:
        html_str = None
    return html_str


if __name__ == '__main__':
    url = "www.baidu.com/"
    print(parse_url(url))
