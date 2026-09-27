# ### Exercise 2: The Time Factor (Real Concurrency)
# **Objective:** Prove that threads are running at the same time (concurrency) and learn to use `join()`.
#           *   **The Challenge:** Create 3 threads. Thread 1 must sleep (`time.sleep(3)`)
#                   for 3 seconds. Thread 2
#                   must sleep for 2 seconds. Thread 3 must sleep for 1 second. Upon waking up,
#                   each should print `"Thread
#                   [X] woke up!"`. The main program must wait for all of them to finish (using
#                   `.join()`) and print `"End
#                   of program"` at the very end.
#           *   **What to observe:** Will the entire program take 6 seconds (3+2+1) or only
#                   3 seconds to finish? If
#                   it takes only 3, you have proven that they worked concurrently.


import threading
import time

def task(thread_id, sleep_duration):
    print(f"hello! i am thread {thread_id} and im going to sleep right now for {sleep_duration} seconds")
    time.sleep(sleep_duration)
    print(f"thread {thread_id} woke up!")

threads = []
durations = [3, 2 ,1]

start_time = time.time()

for i in range(3):
    t = threading.Thread(target=task, args=(i+1, durations[i]))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

time_taken = time.time() - start_time
print(f"program ended! time taken: {time_taken:.2f}")

