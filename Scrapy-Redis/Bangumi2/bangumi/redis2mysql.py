import redis
import pymysql
import json


def process_mysql():
    mysqlcli = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='bangumi', charset='utf8')
    rediscli = redis.StrictRedis(host='localhost', port=6379, db=0)

    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop(["bangumi_spider:items"])

        item = json.loads(data)

        cursor1 = mysqlcli.cursor()
        sql = 'insert into myban (name, name_ch, rank, score, info) values (%s, %s, %s, %s, %s)'
        cursor1.execute(sql, [item['name'], item['name_ch'], item['rank'], item['score'], item['info']])
        mysqlcli.commit()
        cursor1.close()

    mysqlcli.close()


if __name__ == '__main__':
    process_mysql()

# create table myban(
#     id int primary key auto_increment not null,
#     name varchar(255) not null,
#     name_ch varchar(255) not null,
#     rank varchar(255) not null,
#     score varchar(255) not null,
#     info text not null) character set utf8;
