import time
import threading

start = time.time()

def do_something():
    print('Sleeping for 1 second')
    time.sleep(5)
    print('Done Sleeping')


t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()


finish = time.time()
print(f"Total runtime: {finish - start} second(s)")