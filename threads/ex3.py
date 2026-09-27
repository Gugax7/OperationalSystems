# ### Exercise 3: The Race Condition Chaos
# **Objective:** Create a bug on purpose to understand why we need semaphores.
# *   **The Challenge:** Create a global variable `counter = 0`. Create 2 threads. The job of each thread is a loop that repeats the instruction `counter += 1` one million times. At the end of the program, print the counter's value.
# *   **What to observe:** The expected result was for the counter to end at 2 million (1 million from each thread). But the result will be a random, broken number. Why? Because both tried to read and write to the same variable at the exact same time, stepping on each other.

import threading
import time

THREAD_COUNT = 2

counter = 0

def task(thread_id, sum_range):
    global counter
    for _ in range(sum_range):
        temp = counter
        time.sleep(0)
        counter = temp + 1

    print(f"sum finished for thread {thread_id}")

threads = []

for i in range(THREAD_COUNT):
    t = threading.Thread(target=task, args=(i+1, 10000))

    threads.append(t)

    t.start()

for t in threads:
    t.join()

print("counter: ", counter)