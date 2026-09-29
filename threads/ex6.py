# ### Exercise 6: The Nightclub (Counting Semaphore)
# **Objective:** Understand how to use a counting semaphore to limit simultaneous access to a resource (like a connection pool).
# *   **The Challenge:** Create 10 threads (representing people trying to enter a nightclub). However, the club only has a capacity for 3 people at a time. Each thread should print `"Person [X] is waiting"`, enter the club (print `"Person [X] entered"`), sleep for 2 seconds (partying), and then leave (print `"Person [X] left"`).
# *   **Hint:** Instead of a Mutex (Semaphore initialized to 1), use a counting semaphore initialized to 3: `capacity = threading.Semaphore(3)`.
# *   **What to observe:** You will see exactly 3 threads enter. The rest will wait. As soon as one leaves, another one immediately enters. 

import threading
import time

semaphore = threading.Semaphore(3)

def task(person_id):
    print(f"Person [{person_id}] is waiting")

    semaphore.acquire()

    print(f"Person [{person_id}] entered")

    time.sleep(2)

    print(f"Person [{person_id}] left")
    
    semaphore.release()

    

threads = []

for i in range(10):
    t = threading.Thread(target=task, args=(i+1,))

    threads.append(t)

    t.start()

for t in threads:
    t.join()