import time
import concurrent.futures

start = time.time()

def do_something(seconds = 1):
    print(f'Sleeping for {seconds} second')
    time.sleep(seconds)
    return f'Done Sleeping {seconds} sleep'



with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish = time.time()
print(f"Total runtime: {finish - start} second(s)")