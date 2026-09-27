# ### Exercise 4: The Traffic Cop (Mutex)
# **Objective:** Fix the bug from Exercise 3 using a Binary Semaphore (Mutex).
# *   **The Challenge:** Take the code from Exercise 3. Create a semaphore initialized to 1 (`mutex = threading.Semaphore(1)`). Right before the thread does `counter += 1`, it must do an `acquire()` (lock the door). Right after, do a `release()` (unlock the door).
# *   **What to observe:** Now the program will be slightly slower, but the final result will be exactly 2,000,000. You have guaranteed **mutual exclusion**.

import threading
import time

THREAD_COUNT = 2

mutex = threading.Semaphore(1)

counter = 0

def task(thread_id, sum_range):
    global counter
    for _ in range(sum_range):
        mutex.acquire()

        temp = counter
        time.sleep(0)
        counter = temp + 1

        mutex.release()

    print(f"sum finished for thread {thread_id}")

threads = []

for i in range(THREAD_COUNT):
    t = threading.Thread(target=task, args=(i+1, 10000))

    threads.append(t)

    t.start()

for t in threads:
    t.join()


print("counter: ", counter)