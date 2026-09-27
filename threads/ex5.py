### Exercise 5: The Relay Baton (Signaling)
# **Objective:** Make one thread wait for another, which is the foundation for the "Barrier" problem we saw earlier.
# *   **The Challenge:** Create two threads: `A` and `B`. Thread `A` prints `"Processing data..."`, sleeps for 2 seconds, and finishes. Thread `B` should print `"Data received!"`. The rule is: Thread `B` **cannot** print its message before Thread `A` finishes sleeping, and you cannot use `time.sleep()` in Thread `B`.
# *   **Hint:** Use a semaphore initialized to `0` (`signal = threading.Semaphore(0)`). Thread `B` tries to do an `acquire()` right at the beginning, and Thread `A` does a `release()` at the end of its work.

import threading
import time

signal = threading.Semaphore(0)

def task_a():
    print("Sending Data...")
    time.sleep(2)
    print("Data Sent")
    signal.release()

def task_b():
    signal.acquire()
    print("Data received!")

tb = threading.Thread(target=task_b)
ta = threading.Thread(target=task_a)

tb.start()
ta.start()

tb.join()
ta.join()