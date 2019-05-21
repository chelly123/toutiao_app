import redis
import time

r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
p = r.pipeline()

def save_task(task):
    title = task["title"]
    src_link = task["src_link"]
    source = task["source"]
    p.sadd('title', title)
    p.sadd('src_link', src_link)
    p.sadd('source', source)
    print("--" * 20)
    print("-------" + title + "-----------")
    print("--" * 30)
    p.execute()


