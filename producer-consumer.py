import threading
import time
import random

class Producer(threading.Thread):
    def __init__(self, buffer, empty, full, mutex):
        threading.Thread.__init__(self)
        self.buffer = buffer
        self.empty = empty
        self.full = full
        self.mutex = mutex

    def run(self):
        while True:
            item = random.randint(1, 100)
            self.empty.acquire() # Wait for an empty slot
            self.mutex.acquire() # Acquire mutex to access buffer
            print(f"Producer produced: {item}")
            self.buffer.append(item)
            self.mutex.release() # Signal that an item is produced
            self.full.release()

class Consumer(threading.Thread):
    def __init__(self, buffer, empty, full, mutex): 
        threading.Thread.__init__(self)
        self.buffer = buffer 
        self.empty = empty 
        self.full = full
        self.mutex = mutex

    def run(self):
        while True:
            self.full.acquire() # Wait for an item
            self.mutex.acquire() # Acquire mutex to access buffer
            item = self.buffer.pop(0)
            print (f"Consumer consumed: {item}")
            self.mutex.release()
            self.empty.release() # Signal that an empty slot is available 
            time.sleep(random. uniform (1, 3)) # Simulating consumption time

if __name__== "__main__":
    buffer = []
    buffer_size = 5
    empty = threading.Semaphore (buffer_size)
    full = threading.Semaphore (0)
    mutex = threading.Semaphore (1)
    producer = Producer (buffer, empty, full, mutex) 
    consumer = Consumer (buffer, empty, full, mutex)
    producer.start() 
    consumer.start()