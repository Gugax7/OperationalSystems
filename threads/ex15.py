### Exercise 15: Monitor Adaptation with `threading.Condition`
# **Objective:** Implement the bounded queue using Python's Monitor equivalent (`Condition` variables).
# *   **The Challenge:** Reimplement Exercise 14 using `threading.Condition()` instead of raw semaphores. Use `condition.wait_for(lambda: not full)` for producing and `condition.notify_all()` after consuming.

import threading
import random
import time

condition = threading.Condition()
CAPACITY = 5
buffer = []

def producer():
    global buffer
    for _ in range(10):
        prod = random.randint(0,1000)
        time.sleep(0)

        with condition:
            condition.wait_for(lambda: len(buffer) < CAPACITY)

            buffer.append(prod)
            print(f"Produced: {prod} | Buffer size: {len(buffer)}")

            condition.notify_all()

    

def consumer():
    global buffer
    for _ in range(10):
        time.sleep(0.3)

        with condition:
            condition.wait_for(lambda: len(buffer) > 0)

            item = buffer.pop(0)
            print(f"  Consumed: {item} | Buffer size: {len(buffer)}")

            condition.notify_all()

        

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)

p.start()
c.start()

p.join()
c.join()