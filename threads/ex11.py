### Exercise 11: Graceful Signal Handling (`signal` module)
# **Objective:** Intercept OS signals in Python to prevent abrupt program termination.
# *   **The Challenge:** Write a program with an infinite loop printing `"Processing work..."` every second. Register a handler for `SIGINT` (Ctrl+C). When triggered, print `"SIGINT received! Cleaning up before exiting..."`, wait 2 seconds, and exit gracefully without a stack trace.
# *   **Hint:** Use Python's built-in `signal` and `sys` modules.

import signal
import sys
import time

def handle_sigint(signum, frame):
    print("\nSIGINT received! Cleaning up before exiting...")
    time.sleep(2)
    print("Cleanup complete. Exiting gracefully")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

while True:
    print("Processing work...")
    time.sleep(1)

