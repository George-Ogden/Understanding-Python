from queue import SimpleQueue, Empty
q = SimpleQueue()
items = ["a",5,True]
for item in items:
    q.put(item)
# while not q.empty():
try:
    while True:
        print(q.get(timeout=1))
except Empty:
    print("Queue is empty")