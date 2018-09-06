import redis
import pymongo
import json


def process_mongo():
    rediscli = redis.StrictRedis(host='localhost', port=6379, db=0)
    mongocli = pymongo.MongoClient(host='localhost', port=27017)

    db = mongocli['itcast']
    sheet = db['monban']

    while True:
        source, data = rediscli.blpop(["bangumi_spider:items"])
        item = json.loads(data)
        sheet.insert(item)


if __name__ == '__main__':
    process_mongo()
