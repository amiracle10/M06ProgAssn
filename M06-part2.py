import multiprocessing
import random
import time
from datetime import datetime


def print_time():
    wait_time = random.uniform(0, 1)  
    time.sleep(wait_time)
    print(f"Current time: {datetime.now()} (waited for {wait_time:.2f} seconds)")

if __name__ == "__main__":
    
    processes = []

    for _ in range(3):
        p = multiprocessing.Process(target=print_time)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()