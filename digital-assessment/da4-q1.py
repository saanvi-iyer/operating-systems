import threading
import time

# Shared variables for Peterson's Solution
flag = [False, False]  # Flag array for process 0 and process 1
turn = 0  # Turn variable to decide whose turn it is to enter the critical section

# Number of iterations each process will execute
NUM_ITERATIONS = 7

# Critical Section
def critical_section(process_id):
    """
    Simulates the critical section where a process performs some work.
    Each process will print a message upon entering and leaving the critical section.
    """
    print(f"Process {process_id} is entering the critical section.")
    time.sleep(1)  # Simulating work inside the critical section
    print(f"Process {process_id} is leaving the critical section.")

# Peterson's Solution for Process 0
def process_0():
    """
    Simulates process 0 using Peterson's algorithm to manage access to the critical section.
    It ensures that process 0 waits for its turn if process 1 is in the critical section.
    """
    global flag, turn
    for _ in range(NUM_ITERATIONS):
        # Entry Section for process 0
        flag[0] = True
        turn = 1
        while flag[1] and turn == 1:
            pass  # Busy wait until process 1 finishes

        # Critical Section for process 0
        critical_section(0)

        # Exit Section for process 0
        flag[0] = False

        # Simulating the remainder section
        time.sleep(0.5)  # Simulate work done outside the critical section

# Peterson's Solution for Process 1
def process_1():
    """
    Simulates process 1 using Peterson's algorithm to manage access to the critical section.
    It ensures that process 1 waits for its turn if process 0 is in the critical section.
    """
    global flag, turn
    for _ in range(NUM_ITERATIONS):
        # Entry Section for process 1
        flag[1] = True
        turn = 0
        while flag[0] and turn == 0:
            pass  # Busy wait until process 0 finishes

        # Critical Section for process 1
        critical_section(1)

        # Exit Section for process 1
        flag[1] = False

        # Simulating the remainder section
        time.sleep(0.5)  # Simulate work done outside the critical section

# Main function to create threads and execute Peterson's solution
def main():
    """
    Creates two threads representing two processes that will attempt to access a shared
    resource (critical section) using Peterson's algorithm.
    """
    # Create threads for process 0 and process 1
    thread_0 = threading.Thread(target=process_0)
    thread_1 = threading.Thread(target=process_1)

    # Start the threads
    thread_0.start()
    thread_1.start()

    # Wait for both threads to complete
    thread_0.join()
    thread_1.join()

    print("Both processes have finished execution.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
