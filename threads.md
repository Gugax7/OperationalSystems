
### Exercise 1: The Baptism of Threads
**Objective:** Understand how to create threads and realize that you do not control their execution order.
*   **The Challenge:** Write a program that creates 5 threads. Each thread should receive an ID number (from 1 to 5) and print to the screen: `"Hello, I am Thread [X]"`.
*   **What to observe:** Run the program several times. Is the order they print to the terminal always 1, 2, 3, 4, 5? Probably not. The Operating System decides the schedule.

### Exercise 2: The Time Factor (Real Concurrency)
**Objective:** Prove that threads are running at the same time (concurrency) and learn to use `join()`.
*   **The Challenge:** Create 3 threads. Thread 1 must sleep (`time.sleep(3)`) for 3 seconds. Thread 2 must sleep for 2 seconds. Thread 3 must sleep for 1 second. Upon waking up, each should print `"Thread [X] woke up!"`. The main program must wait for all of them to finish (using `.join()`) and print `"End of program"` at the very end.
*   **What to observe:** Will the entire program take 6 seconds (3+2+1) or only 3 seconds to finish? If it takes only 3, you have proven that they worked concurrently.

### Exercise 3: The Race Condition Chaos
**Objective:** Create a bug on purpose to understand why we need semaphores.
*   **The Challenge:** Create a global variable `counter = 0`. Create 2 threads. The job of each thread is a loop that repeats the instruction `counter += 1` one million times. At the end of the program, print the counter's value.
*   **What to observe:** The expected result was for the counter to end at 2 million (1 million from each thread). But the result will be a random, broken number. Why? Because both tried to read and write to the same variable at the exact same time, stepping on each other.

### Exercise 4: The Traffic Cop (Mutex)
**Objective:** Fix the bug from Exercise 3 using a Binary Semaphore (Mutex).
*   **The Challenge:** Take the code from Exercise 3. Create a semaphore initialized to 1 (`mutex = threading.Semaphore(1)`). Right before the thread does `counter += 1`, it must do an `acquire()` (lock the door). Right after, do a `release()` (unlock the door).
*   **What to observe:** Now the program will be slightly slower, but the final result will be exactly 2,000,000. You have guaranteed **mutual exclusion**.

### Exercise 5: The Relay Baton (Signaling)
**Objective:** Make one thread wait for another, which is the foundation for the "Barrier" problem we saw earlier.
*   **The Challenge:** Create two threads: `A` and `B`. Thread `A` prints `"Processing data..."`, sleeps for 2 seconds, and finishes. Thread `B` should print `"Data received!"`. The rule is: Thread `B` **cannot** print its message before Thread `A` finishes sleeping, and you cannot use `time.sleep()` in Thread `B`.
*   **Hint:** Use a semaphore initialized to `0` (`signal = threading.Semaphore(0)`). Thread `B` tries to do an `acquire()` right at the beginning, and Thread `A` does a `release()` at the end of its work.

### Exercise 6: The Nightclub (Counting Semaphore)
**Objective:** Understand how to use a counting semaphore to limit simultaneous access to a resource (like a connection pool).
*   **The Challenge:** Create 10 threads (representing people trying to enter a nightclub). However, the club only has a capacity for 3 people at a time. Each thread should print `"Person [X] is waiting"`, enter the club (print `"Person [X] entered"`), sleep for 2 seconds (partying), and then leave (print `"Person [X] left"`).
*   **Hint:** Instead of a Mutex (Semaphore initialized to 1), use a counting semaphore initialized to 3: `capacity = threading.Semaphore(3)`.
*   **What to observe:** You will see exactly 3 threads enter. The rest will wait. As soon as one leaves, another one immediately enters. 

### Exercise 7: The Producer and the Consumer (Ping Pong)
**Objective:** Coordinate two threads so they alternate their execution perfectly, passing data between them safely.
*   **The Challenge:** Create a global variable `box = None`. Create a `Producer` thread and a `Consumer` thread. The Producer generates a random number, puts it in the `box`, and waits for it to be consumed. The Consumer waits for a number to be in the `box`, reads it, prints it, and empties the box. They must do this exactly 5 times in a row.
*   **Hint:** You need TWO semaphores. `item_ready = threading.Semaphore(0)` and `space_available = threading.Semaphore(1)`. The Producer acquires `space_available` and releases `item_ready`. The Consumer does the exact opposite.

### Exercise 8: The Rendezvous (Two-way Meeting)
**Objective:** Make two threads wait for each other before proceeding. This is the simplest form of a barrier.
*   **The Challenge:** Create Thread A and Thread B. 
    Thread A prints `"A: Arrived at the meeting point"`, then waits for B. 
    Thread B sleeps for 3 seconds, prints `"B: Arrived at the meeting point"`, then waits for A. 
    After BOTH have arrived, they should both print `"Moving forward together!"`.
*   **Hint:** Use two semaphores initialized to 0: `a_arrived` and `b_arrived`. Thread A signals that it arrived and waits for B. Thread B signals that it arrived and waits for A.

### Exercise 9: The Deadlock (The Deadly Embrace)
**Objective:** Intentionally create a bug where threads freeze forever. This teaches you the danger of using multiple locks incorrectly.
*   **The Challenge:** Create two Mutexes: `mutex1` and `mutex2` (both initialized to 1). 
    Thread A must: acquire `mutex1`, sleep for 1 second, and then try to acquire `mutex2`. 
    Thread B must: acquire `mutex2`, sleep for 1 second, and then try to acquire `mutex1`.
*   **What to observe:** The program will never finish. It will freeze forever. Thread A holds lock 1 and needs lock 2. Thread B holds lock 2 and needs lock 1. Neither can proceed. You will have to force quit the program (Ctrl+C).

### Exercise 10: The Group Project (Custom Barrier)
**Objective:** Implement the exact barrier algorithm we discussed earlier, applying everything you've learned.
*   **The Challenge:** Create 4 threads. Each thread does "Part 1" (sleeps for a random time between 1 and 4 seconds). None of the threads can start "Part 2" until all 4 have finished Part 1. 
*   **Hint:** You need:
    1. A shared counter `threads_finished = 0`.
    2. A Mutex (`Semaphore(1)`) to protect the counter.
    3. A Barrier Semaphore (`Semaphore(0)`) to act as the turnstile.
    When a thread finishes Part 1, it safely increments the counter. If it is the last thread (counter == 4), it releases the barrier. Then, all threads must pass through the turnstile (`acquire` followed immediately by `release`).
*   **What to observe:** You will see the threads finishing Part 1 at different times, but they will all print `"Starting Part 2"` at practically the exact same millisecond.

### Exercise 11: Graceful Signal Handling (`signal` module)
**Objective:** Intercept OS signals in Python to prevent abrupt program termination.
*   **The Challenge:** Write a program with an infinite loop printing `"Processing work..."` every second. Register a handler for `SIGINT` (Ctrl+C). When triggered, print `"SIGINT received! Cleaning up before exiting..."`, wait 2 seconds, and exit gracefully without a stack trace.
*   **Hint:** Use Python's built-in `signal` and `sys` modules.

### Exercise 12: Process Communication via Pipe (`multiprocessing.Pipe`)
**Objective:** Pass data safely between two separate Python processes instead of threads.
*   **The Challenge:** Create two processes using `multiprocessing`. Process 1 (Sender) generates 5 random numbers and sends them through a `Pipe`. Process 2 (Receiver) reads from the pipe, calculates the sum, and prints the result.

### Exercise 13: Character Buffer Corruption & Busy-Waiting
**Objective:** Observe string/buffer corruption from concurrent writes and compare Busy-Waiting with `threading.Lock`.
*   **The Challenge:** Create a global list `buffer = []`. Create 4 threads, each appending `"hello world"` character-by-character into `buffer` with `time.sleep(0.001)` between characters. 
*   **Part A:** Run without protection and inspect the corrupted output.
*   **Part B:** Fix it using a custom Busy-Waiting flag (`while locked: pass`).
*   **Part C:** Fix it using `threading.Lock()`. Compare CPU usage between both fixes.

### Exercise 14: Bounded Queue Producer-Consumer (Semaphores)
**Objective:** Manage a finite resource buffer using counting semaphores and mutexes.
*   **The Challenge:** Implement a shared queue of maximum size N = 5. Create 1 Producer thread and 1 Consumer thread. 
*   **Hint:** Use `empty = Semaphore(5)`, `full = Semaphore(0)`, and `mutex = Lock()`. The producer waits for `empty`, locks `mutex`, pushes an item, unlocks, and releases `full`. The consumer does the inverse.

### Exercise 15: Monitor Adaptation with `threading.Condition`
**Objective:** Implement the bounded queue using Python's Monitor equivalent (`Condition` variables).
*   **The Challenge:** Reimplement Exercise 14 using `threading.Condition()` instead of raw semaphores. Use `condition.wait_for(lambda: not full)` for producing and `condition.notify_all()` after consuming.

### Exercise 16: Multi-Worker Request Processing Queue
**Objective:** Scale the producer-consumer pattern to handle multiple concurrent workers.
*   **The Challenge:** Create 1 Dispatcher thread producing 20 numbered requests and 3 Worker threads processing requests from a shared bounded queue (max size 5). Ensure workers shut down gracefully when a special "STOP" signal item is placed in the queue.

### Exercise 17: Dining Philosophers (Deadlock Simulation)
**Objective:** Reproduce a classic deadlock scenario using locks and forced timing delays.
*   **The Challenge:** Create 5 philosopher threads and 5 `threading.Lock()` instances representing forks. Each philosopher tries to acquire `left_fork`, sleeps for 0.01 seconds (simulating delay), and then tries to acquire `right_fork`.
*   **What to observe:** Run the simulation until all 5 philosophers hold their left fork and freeze indefinitely waiting for their right fork (Deadlock).

### Exercise 18: Dining Philosophers (Deadlock Prevention)
**Objective:** Eliminate deadlock by breaking symmetry or using resource ordering.
*   **The Challenge:** Modify Exercise 17 so that even-numbered philosophers pick up the left fork first, while odd-numbered philosophers pick up the right fork first.
*   **What to observe:** Verify that the system runs smoothly without freezing, allowing all philosophers to think and eat repeatedly.

### Exercise 19: Readers-Writers Problem (Reader Preference & Writer Starvation)
**Objective:** Implement concurrent shared-resource access where multiple readers are allowed, but writers need exclusive access.
*   **The Challenge:** Create 5 Reader threads and 1 Writer thread accessing a shared variable. Allow multiple readers to read simultaneously using a `readers_count` variable protected by a mutex, while the writer requires exclusive access to the resource lock.
*   **What to observe:** Observe that as long as new readers keep arriving, the writer is starved and never gets a chance to write.

### Exercise 20: Readers-Writers Problem (Fairness / Writer Priority)
**Objective:** Prevent writer starvation by introducing a turnstile/queue mechanism.
*   **The Challenge:** Modify Exercise 19 by adding a `turnstile` lock or condition variable that forces arriving readers to wait if a writer is already queued up to write.
*   **What to observe:** Verify that writers can modify the resource in a reasonable time without being blocked indefinitely by continuous streams of readers.