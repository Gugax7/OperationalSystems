### Exercise 7: The Producer and the Consumer (Ping Pong)
# **Objective:** Coordinate two threads so they alternate their execution perfectly, passing data between them safely.
# *   **The Challenge:** Create a global variable `box = None`. Create a `Producer` thread and a `Consumer` thread. The Producer generates a random number, puts it in the `box`, and waits for it to be consumed. The Consumer waits for a number to be in the `box`, reads it, prints it, and empties the box. They must do this exactly 5 times in a row.
# *   **Hint:** You need TWO semaphores. `item_ready = threading.Semaphore(0)` and `space_available = threading.Semaphore(1)`. The Producer acquires `space_available` and releases `item_ready`. The Consumer does the exact opposite.

import threading
import random

item_ready = threading.Semaphore(0)
space_available = threading.Semaphore(1)

box = None

def consume():
    global box
    for _ in range(5):
        item_ready.acquire()

        print(f"number consumed: {box}")

        box = None

        space_available.release()

def produce():
    global box
    for _ in range(5):
        space_available.acquire()

        box = random.randint(1, 100)

        item_ready.release()

consumer = threading.Thread(target=consume)
producer = threading.Thread(target=produce)

consumer.start()
producer.start()

consumer.join()
producer.join()
