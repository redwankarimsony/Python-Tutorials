import concurrent.futures
import time

start = time.time()
def do_something(seconds):
    print(f'Sleeping for {seconds} second')
    time.sleep(seconds)
    return f'Done sleeping {seconds} second!'


with concurrent.futures.ProcessPoolExecutor() as executor:
    timelist = [11,10,12,9,5,3,4,8,7,5,5,4,3,2,1]
    results = executor.map(do_something, timelist)
    
    for result in results:
        print(result)



end = time.time()
print(f'Total time elapsed: {end-start} seconds')


