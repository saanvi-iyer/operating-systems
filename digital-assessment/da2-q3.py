class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def priority_non_preemptive_scheduling(processes):
    n = len(processes)
    time = 0
    completed = 0

    # Sort processes by arrival time, if two processes have the same arrival time, sort by priority
    processes.sort(key=lambda p: (p.arrival_time, p.priority))

    while completed != n:
        eligible_processes = [p for p in processes if p.arrival_time <= time and p.completion_time == 0]
        
        if eligible_processes:
            # Select process with highest priority (lowest priority value)
            current_process = min(eligible_processes, key=lambda p: p.priority)
            time += current_process.burst_time
            current_process.completion_time = time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            completed += 1
        else:
            # If no process is ready, increment time (idle time)
            time += 1

    avg_waiting_time = sum(p.waiting_time for p in processes) / n
    avg_turnaround_time = sum(p.turnaround_time for p in processes) / n

    print("\nPID\tArrival\tBurst\tPriority\tWaiting\tTurnaround")
    for p in processes:
        print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.priority}\t{p.waiting_time}\t{p.turnaround_time}")
    
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    processes = []
    for i in range(n):
        pid = input(f"Enter Process ID for process {i + 1}: ")
        arrival_time = int(input(f"Enter Arrival Time for process {i + 1}: "))
        burst_time = int(input(f"Enter Burst Time for process {i + 1}: "))
        priority = int(input(f"Enter Priority for process {i + 1} (lower number indicates higher priority): "))
        processes.append(Process(pid, arrival_time, burst_time, priority))

    priority_non_preemptive_scheduling(processes)
