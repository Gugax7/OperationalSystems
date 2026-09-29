### Exercise 12: Process Communication via Pipe (`multiprocessing.Pipe`)
# **Objective:** Pass data safely between two separate Python processes instead of threads.
# *   **The Challenge:** Create two processes using `multiprocessing`. Process 1 (Sender) generates 5 random numbers and sends them through a `Pipe`. Process 2 (Receiver) reads from the pipe, calculates the sum, and prints the result.

import multiprocessing
import random

conn1, conn2 = multiprocessing.Pipe()

def sender(conn):
    for _ in range(5):
        num = random.randint(1,100)
        print(f"Sender sent: {num}")
        conn.send(num)
    conn.close()

def receiver(conn):
    total = 0
    for _ in range(5):
        num = conn.recv()
        total+=num

        print(f"Receiver got: {num}")
    print(f"Total: {total}")

    conn.close()

p1 = multiprocessing.Process(target=sender, args=(conn1,))
p2 = multiprocessing.Process(target=receiver, args=(conn2,))

p1.start()
p2.start()

p1.join()
p2.join()