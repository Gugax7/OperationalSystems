### Exercise 10: The Group Project (Custom Barrier)
# **Objective:** Implement the exact barrier algorithm we discussed earlier, applying everything you've learned.
# *   **The Challenge:** Create 4 threads. Each thread does "Part 1" (sleeps for a random time between 1 and 4 seconds). None of the threads can start "Part 2" until all 4 have finished Part 1. 
# *   **Hint:** You need:
#     1. A shared counter `threads_finished = 0`.
#     2. A Mutex (`Semaphore(1)`) to protect the counter.
#     3. A Barrier Semaphore (`Semaphore(0)`) to act as the turnstile.
#     When a thread finishes Part 1, it safely increments the counter. If it is the last thread (counter == 4), it releases the barrier. Then, all threads must pass through the turnstile (`acquire` followed immediately by `release`).
# *   **What to observe:** You will see the threads finishing Part 1 at different times, but they will all print `"Starting Part 2"` at practically the exact same millisecond.

import threading
import time

THREAD_COUNT = 4

barrier = threading.Semaphore(0)
mutex = threading.Semaphore(1)

threads_ready = 0

def task(id, wait_time):
    global threads_ready

    time.sleep(wait_time)

    print(f"Thread [{id}] finished part 1")

    with mutex:
        threads_ready+=1

        if threads_ready == THREAD_COUNT:
            barrier.release()
            print(f"Thread [{id}] finished last")

    print(f"Thread [{id}] is waiting the others")

    barrier.acquire()

    print(f"Thread [{id}] was released")

    barrier.release()

    print(f"Thread [{id}] finishes part 2")

            
threads = []
wait_times = [1, 4, 3, 2]

for i in range(THREAD_COUNT):
    t = threading.Thread(target=task, args=(i+1, wait_times[i]))

    threads.append(t)

    t.start()

for t in threads:
    t.join()

