import threading
import time
import random

# Shared resource
shared_data = 0
read_count = 0

# Semaphores
mutex = threading.Semaphore(1)  # Controls access to read_count
write_lock = threading.Semaphore(1)  # Ensures exclusive access for writers

class Reader(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index

    def run(self):
        global read_count, shared_data
        while True:
            # Entry section
            mutex.acquire()  # Lock the read_count variable
            read_count += 1
            if read_count == 1:  # If it's the first reader
                write_lock.acquire()  # First reader locks the writer
            mutex.release()  # Unlock the read_count variable

            # Critical section (reading)
            print(f"Reader {self.index} is reading the shared data: {shared_data}")
            time.sleep(random.uniform(1, 3))  # Simulating read time

            # Exit section
            mutex.acquire()  # Lock the read_count variable
            read_count -= 1  # Reader leaves
            if read_count == 0:  # Last reader unlocks the writer
                write_lock.release()
            mutex.release()  # Unlock the read_count variable
            time.sleep(random.uniform(1, 3))  # Simulating time between reads

class Writer(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index

    def run(self):
        global shared_data
        while True:
            # Entry section
            write_lock.acquire()  # Ensure no other writer or reader is writing

            # Critical section (writing)
            shared_data += 1
            print(f"Writer {self.index} is writing to the shared data: {shared_data}")
            time.sleep(random.uniform(1, 3))  # Simulating write time

            # Exit section
            write_lock.release()  # Release the lock after writing
            time.sleep(random.uniform(1, 3))  # Simulating time between writes

if __name__ == "__main__":
    readers = [Reader(i) for i in range(3)]  # Create 3 readers
    writers = [Writer(i) for i in range(2)]  # Create 2 writers

    for reader in readers:
        reader.start()
    for writer in writers:
        writer.start()
