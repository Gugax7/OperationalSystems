### Exercise 18: Dining Philosophers (Deadlock Prevention)
# **Objective:** Eliminate deadlock by breaking symmetry or using resource ordering.
# *   **The Challenge:** Modify Exercise 17 so that even-numbered philosophers pick up the left fork first, while odd-numbered philosophers pick up the right fork first.
# *   **What to observe:** Verify that the system runs smoothly without freezing, allowing all philosophers to think and eat repeatedly.

import threading
import time

forks = [threading.Lock(), threading.Lock(), threading.Lock(), threading.Lock(), threading.Lock()]
solution_lock = threading.Lock()

def phylosopher(id):
    fork_right = (id + 1) % 5
    fork_left = id

    first_fork = fork_right
    last_fork = fork_left

    if id % 2 == 0:
        first_fork = fork_left
        last_fork = fork_right

    forks[first_fork].acquire()

    print(f"Phylosopher {id} acquire left fork (fork {fork_left})")

    time.sleep(1)

    forks[last_fork].acquire()
    
    print(f"Phylosopher {id} acquire left fork (fork {fork_right})")
    print(f"Phylosopher {id} ate!")

    forks[first_fork].release()
    forks[last_fork].release()

threads = []
for i in range(5):
    threads.append(threading.Thread(target=phylosopher, args=(i,)))

for t in threads:
    t.start()

for t in threads:
    t.join()

print("\n--- All threads terminated cleanly ---")