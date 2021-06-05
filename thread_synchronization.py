import threading
import time

x =0

def thread_task(lock):
    global x
    for i in range(200000):
        lock.acquire()
        x += 1
        lock.release()
        
    

def main_task():
    lock = threading.Lock()

    t1 = threading.Thread(target=thread_task, name='thread1', args=(lock,))
    t2 = threading.Thread(target=thread_task, name = 'thread2', args=(lock,))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()


if __name__ == "__main__":
    main_task()
    print(x)




