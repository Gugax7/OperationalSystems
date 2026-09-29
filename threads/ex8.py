# ### Exercise 8: The Rendezvous (Two-way Meeting)
# **Objective:** Make two threads wait for each other before proceeding. This is the simplest form of a barrier.
# *   **The Challenge:** Create Thread A and Thread B. 
#     Thread A prints `"A: Arrived at the meeting point"`, then waits for B. 
#     Thread B sleeps for 3 seconds, prints `"B: Arrived at the meeting point"`, then waits for A. 
#     After BOTH have arrived, they should both print `"Moving forward together!"`.
# *   **Hint:** Use two semaphores initialized to 0: `a_arrived` and `b_arrived`. Thread A signals that it arrived and waits for B. Thread B signals that it arrived and waits for A.

import threading
import time

a_arrived = threading.Semaphore(0)
b_arrived = threading.Semaphore(0)

def task_a():
    print("A: Arrived at the meeting point")
    a_arrived.release()  # 1. Tell Thread B that A is here
    b_arrived.acquire()  # 2. Wait until Thread B signals it is here
    print("A: Moving forward together!")

def task_b():
    time.sleep(3)
    print("B: Arrived at the meeting point")
    b_arrived.release()  # 1. Tell Thread A that B is here
    a_arrived.acquire()  # 2. Wait until Thread A signals it is here
    print("B: Moving forward together!")

tb = threading.Thread(target=task_b)
ta = threading.Thread(target=task_a)

tb.start()
ta.start()

tb.join()
ta.join()