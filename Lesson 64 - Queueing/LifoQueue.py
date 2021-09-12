# from queue import LifoQueue, Empty
# q = LifoQueue()
# items = ["a",5,True]
# for item in items:
#     q.put(item)
# # while not q.empty():
# try:
#     while True:
#         print(q.get(timeout=1))
# except Empty:
#     print("Queue is empty")

from queue import LifoQueue, Empty, Full
from threading import Thread
import random
import time

q = LifoQueue(maxsize=0)
items = ["a",5,True]
def add(*items):
    try:
        for item in items:
            q.put(item,timeout=random.random())
            time.sleep(random.random())
    except Full:
        print("Queue is full")
Thread(target=add,args=items).start()
Thread(target=add,args=["orange","apple","banana"]).start()

try:
    while True:
        print(q.get(timeout=2))
        time.sleep(0.5)
except Empty:
    print("Queue is empty")