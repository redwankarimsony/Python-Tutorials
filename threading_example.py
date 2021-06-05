import threading
import time


def print_epoch(nameOfThread, delay):
    count = 0
    while count <5:
        time.sleep(delay)
        count += 1
        print(nameOfThread, "+++++++++++", count , time.time())

def print_cube(num):
    print(f"Cube: {num*num*num}")

def print_square(num):
    print(f"Square: {num*num}")


if __name__ == "__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(15,))


    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(f"{t1.name} and {t2.name} are finished execution!!")