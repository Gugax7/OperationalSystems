# ## Exercise 3: Shared Buffer & Race Conditions
# 3. Write a program containing multiple threads that repeatedly write, character by character, the same content (e.g., “hello world”) to a shared buffer. In each iteration of the loop, insert an instruction that puts the program to sleep for a short period.
#    a. By running the program for a given period, did you observe any race condition?
#    b. Implement a solution using busy-waiting-based mutual exclusion algorithms and evaluate the buffer size at the end of a given period.

# ---

import threading
import time

t_0 = time.time()

n_threads=2
buffer = str()

busy_lock = 0

def hello():
    global buffer, busy_lock
    for x in 'hello world ':
        while busy_lock == 1:
            pass
        busy_lock = 1

        buffer += x
        time.sleep(1e-6)

        busy_lock = 0

def hello_loop():
    while time.time()-t_0 < 1:
        hello()


threads = []
for i in range(n_threads):
    thread = threading.Thread(target=hello_loop)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(buffer)
print(len(buffer))

