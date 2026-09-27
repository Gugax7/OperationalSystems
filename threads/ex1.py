# ### Exercise 1: The Baptism of Threads
# **Objective:** Understand how to create threads and realize that you do
#                not control their execution order.
#                *   **The Challenge:** Write a program that creates 5 threads. Each 
#                    thread should receive an ID number (from 1 to 5) and print to the
#                    screen: `"Hello, I am Thread [X]"`.
#                *   **What to observe:** Run the program several times. Is the order
#                    they print to the terminal always 1, 2, 3, 4, 5? Probably not. 
#                    The Operating System decides the schedule.

import threading

def thread_task(thread_id):
    print(f"I am thread {thread_id}")

threads = []

for i in range(5):
    t = threading.Thread(target=thread_task, args=(i+1,))

    threads.append(t)

    t.start()

for t in threads:
    t.join()


