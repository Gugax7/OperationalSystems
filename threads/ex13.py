### Exercise 13: Character Buffer Corruption & Busy-Waiting
# **Objective:** Observe string/buffer corruption from concurrent writes and compare Busy-Waiting with `threading.Lock`.
# *   **The Challenge:** Create a global list `buffer = []`. Create 4 threads, each appending `"hello world"` character-by-character into `buffer` with `time.sleep(0.001)` between characters. 
# *   **Part A:** Run without protection and inspect the corrupted output.
# *   **Part B:** Fix it using a custom Busy-Waiting flag (`while locked: pass`).
# *   **Part C:** Fix it using `threading.Lock()`. Compare CPU usage between both fixes.

import threading
import time

locked = False
buffer = ''
lock = threading.Lock()

def task():
    global buffer
    for c in "hello world ":
        time.sleep(0)
        buffer = buffer + c

def task_busy_locked():
    global buffer, locked

    while locked:
        pass

    locked = True

    for c in "hello world ":
        time.sleep(0)
        buffer = buffer + c

    locked = False

def task_mutex():
    global buffer

    with lock:
        for c in "hello world ":
            time.sleep(0)
            buffer = buffer + c

# task mutex its amazingly faster than with busy lock

threads = []

for i in range(10):
    t = threading.Thread(target=task_mutex)

    threads.append(t)

    t.start()

for t in threads:
    t.join()

print(buffer)