# ## Exercise 6: Readers and Writers
# 6. Implement a simulation of the Readers and Writers problem. Consider a set of threads accessing the same shared resource (e.g., a file or database). There are two types of threads:
#    (i) Readers: only query the resource, so multiple readers can access it simultaneously; and
#    (ii) Writers: modify the resource and require exclusive access.
#    While a writer is writing, no reader or other writer can access the resource.
#    a. Implement a solution that respects these access rules. Each reader and each writer must be implemented as a thread.
#    b. Run the simulation with multiple readers and few writers. Observe that if new readers can enter while a writer is waiting, the writer may remain waiting indefinitely (starvation).
#    c. Modify the implementation to prevent writer starvation.

# ---