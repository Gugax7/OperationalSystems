### Exercise 14: Bounded Queue Producer-Consumer (Semaphores)
# **Objective:** Manage a finite resource buffer using counting semaphores and mutexes.
# *   **The Challenge:** Implement a shared queue of maximum size N = 5. Create 1 Producer thread and 1 Consumer thread. 
# *   **Hint:** Use `empty = Semaphore(5)`, `full = Semaphore(0)`, and `mutex = Lock()`. The producer waits for `empty`, locks `mutex`, pushes an item, unlocks, and releases `full`. The consumer does the inverse.

import threading
import random
import time

empty = threading.Semaphore(5)
full = threading.Semaphore(0)

mutex = threading.Lock()

buffer = []

def producer():
    global buffer
    for _ in range(10):
        prod = random.randint(0,1000)
        time.sleep(0)

        empty.acquire()

        with mutex:      # 2. Safely add to buffer
            buffer.append(prod)
            print(f"Produced: {prod} | Buffer size: {len(buffer)}")

        full.release()
    

def consumer():
    global buffer
    for _ in range(10):
        time.sleep(0.3)

        full.acquire()

        with mutex:
            item = buffer.pop(0)
            print(f"  Consumed: {item} | Buffer size: {len(buffer)}")

        empty.release()

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)

p.start()
c.start()

p.join()
c.join()