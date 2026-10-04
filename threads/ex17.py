### Exercise 17: Dining Philosophers (Deadlock Simulation)
# **Objective:** Reproduce a classic deadlock scenario using locks and forced timing delays.
# *   **The Challenge:** Create 5 philosopher threads and 5 `threading.Lock()` instances representing forks. Each philosopher tries to acquire `left_fork`, sleeps for 0.01 seconds (simulating delay), and then tries to acquire `right_fork`.
# *   **What to observe:** Run the simulation until all 5 philosophers hold their left fork and freeze indefinitely waiting for their right fork (Deadlock).

import threading
import time

forks = [threading.Lock(), threading.Lock(), threading.Lock(), threading.Lock(), threading.Lock()]
solution_lock = threading.Lock()

def phylosopher(id):
    fork_right = (id + 1) % 5
    fork_left = id

    forks[fork_left].acquire()

    print(f"Phylosopher {id} acquire left fork (fork {fork_left})")

    time.sleep(1)

    forks[fork_right].acquire()
    
    print(f"Phylosopher {id} acquire left fork (fork {fork_right})")
    print(f"Phylosopher {id} ate!")

    forks[fork_left].release()
    forks[fork_right].release()

threads = []
for i in range(5):
    threads.append(threading.Thread(target=phylosopher, args=(i,)))

for t in threads:
    t.start()

for t in threads:
    t.join()

print("\n--- All threads terminated cleanly ---")