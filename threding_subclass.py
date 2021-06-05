from threading import Thread
import threading
import time


def print_epoch(nameOfThread, delay):
    count = 0
    while count <5:
        time.sleep(delay)
        count += 1
        print(nameOfThread, "+++++++++++", count , time.time())

class MyThread(Thread):
    def __init__(self, name, delay):
        Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print(f'{self.name} started')
        print_epoch(self.name, self.delay)
        print(f'{self.name} ended')
        

if __name__ == "__main__":
    t1 = MyThread('thread1', 1)
    t2 = MyThread('thread2', 2)

    print(threading.currentThread())

    t1.start()
    t2.start()

    print(threading.active_count())
    print(threading.currentThread())

