from threading import Thread, Lock
import random, time

lock = Lock()
start_count = 0
finish_count = 0
def advanced_function():
    global start_count, finish_count, lock
    lock.acquire()
    print(f"Thread {start_count}: start")
    start_count += 1
    lock.release()
    time.sleep(1)
    lock.acquire()
    print(f"Thread {finish_count}: finish")
    finish_count += 1
    lock.release()

def function(number):
    print(f"Thread {number}: start")
    # time.sleep(random.random())
    time.sleep(1)
    print(f"Thread {number}: finish")

# print("Creating thread")
# thread = Thread(target=function,args=(1,),daemon=True)
# print("Starting thread")
# thread.start()
# print("Waiting for thread to join")
# thread.join()
# print("All done")

threads = []
for i in range(10):
    thread = Thread(target=advanced_function)
    # thread = Thread(target=function,args=(i,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()