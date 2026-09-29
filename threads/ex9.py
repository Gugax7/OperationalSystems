### Exercise 9: The Deadlock (The Deadly Embrace)
# **Objective:** Intentionally create a bug where threads freeze forever. This teaches you the danger of using multiple locks incorrectly.
# *   **The Challenge:** Create two Mutexes: `mutex1` and `mutex2` (both initialized to 1). 
#     Thread A must: acquire `mutex1`, sleep for 1 second, and then try to acquire `mutex2`. 
#     Thread B must: acquire `mutex2`, sleep for 1 second, and then try to acquire `mutex1`.
# *   **What to observe:** The program will never finish. It will freeze forever. Thread A holds lock 1 and needs lock 2. Thread B holds lock 2 and needs lock 1. Neither can proceed. You will have to force quit the program (Ctrl+C).

import threading
import time

import threading
import time

mutex1 = threading.Semaphore(1)
mutex2 = threading.Semaphore(1)

def task_a():
    print("A: Arrived at the meeting point")
    mutex1.acquire()

    time.sleep(1)

    mutex2.acquire()
    print("A: Moving forward together!")

def task_b():
    print("B: Arrived at the meeting point")
    mutex2.acquire()

    time.sleep(1)

    mutex1.acquire()
    print("B: Moving forward together!")

tb = threading.Thread(target=task_b)
ta = threading.Thread(target=task_a)

tb.start()
ta.start()

tb.join()
ta.join()