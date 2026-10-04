### Exercise 16: Multi-Worker Request Processing Queue
# **Objective:** Scale the producer-consumer pattern to handle multiple concurrent workers.
# *   **The Challenge:** Create 1 Dispatcher thread producing 20 numbered requests and 3 Worker threads processing requests from a shared bounded queue (max size 5). Ensure workers shut down gracefully when a special "STOP" signal item is placed in the queue.

import threading
import time
import random

conditional = threading.Condition()

queue = []
CAPACITY = 5
CONSUMERS = 3

def dispatcher():
    global queue
    kill_count = 0
    item_count = 0
    while kill_count < CONSUMERS:
        item = random.randint(1,5)
        time.sleep(0)

        with conditional:
            conditional.wait_for(lambda: len(queue) < CAPACITY)

            if item == 5:
                kill_count = kill_count + 1

                print(f"  💥 [Dispatcher] Enqueued STOP bullet ({kill_count}/{CONSUMERS})")
            else:
                item_count+=1

                print(f"  📦 [Dispatcher] Enqueued job #{item_count} (val: {item}) | Queue size: {len(queue) + 1}")

            queue.append(item)

            conditional.notify_all()

    print(f"\n   ☠️ [Dispatcher] Dispatched all {CONSUMERS} bullets! Total jobs created: {item_count}. Dispatcher exiting.")


def consumer(consumer_id):
    global queue
    while True:
        with conditional:
            conditional.wait_for(lambda: len(queue) > 0)

            item = queue.pop(0)

            if item == 5:
                print(f"  💀 [Worker {consumer_id}] Drew bullet (5)! Thread dying...")
                break

            print(f"  ⚙️ [Worker {consumer_id}] Processed job {item}")

            time.sleep(random.uniform(0.1, 0.2))


# --- Launch Execution ---
threads = [threading.Thread(target=dispatcher, name="Dispatcher")]
for i in range(CONSUMERS):
    threads.append(threading.Thread(target=consumer, args=(i + 1,), name=f"Consumer-{i+1}"))

for t in threads:
    t.start()

for t in threads:
    t.join()

print("\n--- All threads terminated cleanly ---")
    
    