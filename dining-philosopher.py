import threading
import time
import random

class Philosopher(threading.Thread):
    def __init__(self, index, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.index=index
        self.left_fork=left_fork
        self.right_fork=right_fork

    def run(self):
        while True:
            print(f"Philosopher {self.index} is thinking.")
            time.sleep(random.uniform(1,3)) #simulated thinking
            print(f"Philosopher {self.index} is hungry.")

            #pick up left and right forks (binary semaphores)
            self.left_fork.acquire()
            print(f"Philosopher {self.index} picked up left fork.")
            self.right_fork.acquire()
            print(f"Philosopher {self.index} picked up right fork.")
            
            print(f"Philosopher {self.index} is thinking.")
            time.sleep(random.uniform(1,3)) #simulated eating

            #release forks after eating
            self.left_fork.release()
            self.right_fork.release()
            print(f"Philosopher {self.index} put down forks.")

if __name__ == "__main__":
    num_philosophers=5
    forks=[threading.Semaphore(1) for _ in range(num_philosophers)]
    philosophers = []

    for i in range(num_philosophers):
        philosopher=Philosopher(i, forks[i],forks[(i+1)%num_philosophers])
        philosophers.append(philosopher)

    for philosopher in philosophers:
        philosopher.start()

