import matplotlib.pyplot as plt
from tabulate import tabulate

def fcfs(requests, head):
    seek_sequence = [head] + requests
    seek_time = sum(abs(seek_sequence[i] - seek_sequence[i + 1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, seek_time

def scan(requests, head, disk_size):
    requests.sort()
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]
    seek_sequence = [head] + left[::-1] + [0] + right
    seek_time = sum(abs(seek_sequence[i] - seek_sequence[i + 1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, seek_time

def c_scan(requests, head, disk_size):
    requests.sort()
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]
    seek_sequence = [head] + right + [disk_size - 1] + [0] + left
    seek_time = sum(abs(seek_sequence[i] - seek_sequence[i + 1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, seek_time

def look(requests, head):
    requests.sort()
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]
    seek_sequence = [head] + right + left[::-1]
    seek_time = sum(abs(seek_sequence[i] - seek_sequence[i + 1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, seek_time

def c_look(requests, head):
    requests.sort()
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]
    seek_sequence = [head] + right + left
    seek_time = sum(abs(seek_sequence[i] - seek_sequence[i + 1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, seek_time

# Parameters
disk_size = 200
initial_head = 50
requests = [98, 183, 37, 122, 14, 124, 65, 67]

# Run algorithms
algorithms = {'FCFS': fcfs, 'SCAN': scan, 'C-SCAN': c_scan, 'LOOK': look, 'C-LOOK': c_look}
results = {}

# Disk scheduling algorithm results
for name, func in algorithms.items():
    seek_sequence, seek_time = func(requests, initial_head, disk_size) if 'SCAN' in name else func(requests, initial_head)
    results[name] = (seek_sequence, seek_time)
table_data = [(name, seek_sequence, seek_time) for name, (seek_sequence, seek_time) in results.items()]
print("\nAlgorithm Results:")
print(tabulate(table_data, headers=["Algorithm", "Seek Sequence", "Seek Time"], tablefmt="grid"))

# Calculate Efficiency Ranking
sorted_results = sorted(results.items(), key=lambda x: x[1][1])
table_data = [(name, time) for name, (_, time) in sorted_results]
print("\nEfficiency Ranking (from most efficient to least efficient):")
print(tabulate(table_data, headers=["Algorithm", "Seek Time"], tablefmt="grid"))

# Plotting seek operations
plt.figure(figsize=(10, 6))
for name, (seek_sequence, _) in results.items():
    plt.plot(seek_sequence, marker='o', label=name)

plt.title("Disk Scheduling Seek Operations")
plt.xlabel("Seek Operations")
plt.ylabel("Track Number")
plt.legend()
plt.show()
