import threading
from queue import Queue
from lxml import etree
import requests
import json
import time


class ThreadCrawl(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        super(ThreadCrawl, self).__init__()
        # 线程名
        self.threadName = threadName
        # 页码队列
        self.pageQueue = pageQueue
        # 数据队列
        self.dataQueue = dataQueue
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

    def run(self):
        print('启动' + self.threadName)
        while not CRAWL_EXIT:
            try:
                # 可选参数blocking，默认值True
                # 1. 队列为空，blocking默认为True，不会结束，进入阻塞状态，直到队列有新数据
                # 2. 队列为空，blocking为False，就弹出一个Queue.empty()异常
                page = self.pageQueue.get(False)
                url = 'http://bangumi.tv/game/browser?sort=rank&page=' + str(page)
                print(url)
                response = requests.get(url, headers=self.headers)
                content = response.content.decode()
                time.sleep(1)
                self.dataQueue.put(content)

            except:
                pass

        print('结束' + self.threadName)


class ThreadParse(threading.Thread):
    def __init__(self, threadName, dataQueue, filename, mutex):
        super(ThreadParse, self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue
        self.filename = filename
        self.mutex = mutex

    def run(self):
        print('启动' + self.threadName)
        while not PARSE_EXIT:
            try:
                html = self.dataQueue.get(False)

                self.parse(html)

            except:
                pass
        print("退出" + self.threadName)

    def parse(self, html):
        xml = etree.HTML(html)

        game_info = xml.xpath('//ul[@class="browserFull"]/li/div[@class="inner"]')
        # items = []
        for each in game_info:
            name = each.xpath('./h3/a')[0].text
            rank = each.xpath('./span[@class="rank"]/text()')[0]
            rate = each.xpath('./p[@class="rateInfo"]/small')[0].text

            item = {
                'name': name,
                'rank': rank,
                'rate': rate,

            }
            # print(item)
        #     items.append(item)
        # print(items)

        # with 后面有两个必须执行的操作：__enter__ 和 _exit__
        # 不管里面的操作结果如何，都会执行打开、关闭
        # 打开锁、处理内容、释放
            with self.mutex:
                self.filename.write(json.dumps(item, ensure_ascii=False) + '\n\n')
            # self.mutex.acquire()
            # jsonstr = json.dumps(item, ensure_ascii=False) + '\n\n'
            # self.filename.write(jsonstr)
            # self.mutex.release()


CRAWL_EXIT = False
PARSE_EXIT = False


def main():
    # 页码队列
    pageQueue = Queue(10)
    # 先进先出
    for i in range(1, 11):
        pageQueue.put(i)
    # html是数据队列，参数为空表示不限制
    dataQueue = Queue()

    filename = open('game.json', 'a')
    # 创建锁
    mutex = threading.Lock()
    # 采集线程名字
    crawllist = ['采集thread1', '采集thread2', '采集thread3']
    # 存储采集线程
    threadcrawl = []
    for threadName in crawllist:
        threadc = ThreadCrawl(threadName, pageQueue, dataQueue)
        threadc.start()
        threadcrawl.append(threadc)

    # 解析线程名字
    parselist = ['解析thread1', '解析thread2', '解析thread3']
    # 存储解析线程
    threadparse = []
    for threadName in parselist:
        threadp = ThreadParse(threadName, dataQueue, filename, mutex)
        threadp.start()
        threadparse.append(threadp)

    # 等待pageQueue为空，采集线程退出循环
    while not pageQueue.empty():
        pass

    # 如果pageQueue为空，采集线程退出循环
    global CRAWL_EXIT
    CRAWL_EXIT = True

    print('pageQueue为空')

    for threadcr in threadcrawl:
        threadcr.join()
        print('1')

    while not dataQueue.empty():
        pass

    global PARSE_EXIT
    PARSE_EXIT = True

    for threadpr in threadparse:
        threadpr.join()
        print('2')

    with mutex:
        filename.close()
    # time.sleep(20)
    # filename.close()
    print('谢谢使用')


if __name__ == '__main__':
    main()
