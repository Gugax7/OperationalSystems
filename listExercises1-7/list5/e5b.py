# ## Exercise 5: Dining Philosophers
# 5. Implement a simulation of the Dining Philosophers problem. Five philosophers sit around a table and alternate between thinking and eating. There is a fork between each pair of philosophers, and each philosopher must obtain both adjacent forks before eating.
#    a. Implement each philosopher as a thread and each fork as a shared resource protected by a mutex. Initially, have each philosopher attempt to pick up the fork on their left first, and then the one on their right. Remember to include a short `time.sleep()` between these two actions.
#    b. Run the simulation multiple times and verify whether deadlock can occur. Next, modify the implementation to prevent deadlock.

# ---