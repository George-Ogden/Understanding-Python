from queue import PriorityQueue, Empty
import random
q = PriorityQueue()
items = ["a",5,True]
for item in items:
    q.put((-random.random(),item))
# while not q.empty():
try:
    while True:
        priority, item = q.get(timeout=1)
        print(priority,item)
except Empty:
    print("Queue is empty")