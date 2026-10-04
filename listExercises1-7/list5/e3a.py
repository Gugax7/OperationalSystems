# ## Exercise 3: Shared Buffer & Race Conditions
# 3. Write a program containing multiple threads that repeatedly write, character by character, the same content (e.g., “hello world”) to a shared buffer. In each iteration of the loop, insert an instruction that puts the program to sleep for a short period.
#    a. By running the program for a given period, did you observe any race condition?
# ---

# import threading
# import time
# import random

# buffer = ''

# def writer():
#     global buffer
#     for c in "hello world ":
#         time.sleep(random.uniform(0.1, 0.4))
#         buffer+= c

# threads = []

# for i in range(5):
#     t = threading.Thread(target=writer)

#     threads.append(t)

#     t.start()

# for t in threads:
#     t.join()

# print(f"buffer: {buffer}")
# print(f"len: {len(buffer)}")

import threading
import time

t_0 = time.time()

n_threads=2
buffer = str()

def hello():
    global buffer
    for x in 'hello world ':
        buffer += x
        time.sleep(1e-6)

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