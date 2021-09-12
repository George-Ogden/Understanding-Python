from queue import Queue, Empty, Full
from threading import Thread
import random
import time

q = Queue(maxsize=3)
items = ["a",5,True]
def add(*items):
    try:
        for item in items:
            q.put(item,timeout=random.random())
    except Full:
        print("Queue is full")
Thread(target=add,args=items).start()
Thread(target=add,args=["orange","apple","banana"]).start()

try:
    while True:
        print(q.get(timeout=2))
        time.sleep(2)
except Empty:
    print("Queue is empty")