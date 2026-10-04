### Exercise 20: Readers-Writers Problem (Fairness / Writer Priority)
# **Objective:** Prevent writer starvation by introducing a turnstile/queue mechanism.
# *   **The Challenge:** Modify Exercise 19 by adding a `turnstile` lock or condition variable that forces arriving readers to wait if a writer is already queued up to write.
# *   **What to observe:** Verify that writers can modify the resource in a reasonable time without being blocked indefinitely by continuous streams of readers.

### Exercise 19: Readers-Writers Problem (Reader Preference & Writer Starvation)
# **Objective:** Implement concurrent shared-resource access where multiple readers are allowed, but writers need exclusive access.
# *   **The Challenge:** Create 5 Reader threads and 1 Writer thread accessing a shared variable. Allow multiple readers to read simultaneously using a `readers_count` variable protected by a mutex, while the writer requires exclusive access to the resource lock.
# *   **What to observe:** Observe that as long as new readers keep arriving, the writer is starved and never gets a chance to write.

import threading
import time
import random

mutex = threading.Lock()
resource_lock = threading.Lock()
turnstile = threading.Lock()

readers_count = 0
shared_data = 0

def reader(reader_id):
    global readers_count, shared_data

    while True:
        with turnstile:
            with mutex:
                readers_count+=1
                if readers_count == 1:
                    resource_lock.acquire()

            print(f"📖 [Reader {reader_id}] Reading data = {shared_data} | Active readers: {readers_count}")
            
            time.sleep(random.uniform(0.1, 0.3))

        with mutex:
            readers_count -= 1

            if readers_count == 0:
                resource_lock.release()

        time.sleep(random.uniform(0.1,0.5))

def writer(writer_id):
    global shared_data

    while True:
        time.sleep(random.uniform(0.2, 0.5))

        with turnstile:
            with resource_lock:
                shared_data+=1
                print(f"🔥 [Writer {writer_id}] UPDATED data to {shared_data}!")
                time.sleep(0.2)

threads = []

writer1 = threading.Thread(target=writer, args=(1,))

threads.append(writer1)

for i in range(5):
    threads.append(threading.Thread(target=reader, args=(i,)))

for t in threads:
    t.start()

for t in threads:
    t.join()

print("\n--- All threads terminated cleanly ---")