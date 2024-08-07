def sjf_non_preemptive_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: (x['ArrivalTime'], x['BurstTime']))
    
    current_time = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completed = [False] * n
    
    for i in range(n):
        idx = -1
        min_burst = float('inf')
        for j in range(n):
            if not completed[j] and processes[j]['ArrivalTime'] <= current_time and processes[j]['BurstTime'] < min_burst:
                min_burst = processes[j]['BurstTime']
                idx = j
        if idx == -1:
            current_time += 1
            continue
        completed[idx] = True
        waiting_time[idx] = current_time - processes[idx]['ArrivalTime']
        current_time += processes[idx]['BurstTime']
        turnaround_time[idx] = waiting_time[idx] + processes[idx]['BurstTime']
    
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    
    return waiting_time, turnaround_time, avg_waiting_time, avg_turnaround_time

def main():
    num_processes = int(input("Enter the number of processes: "))
    processes = []
    
    for i in range(num_processes):
        process_id = input(f"Enter ProcessID for process {i+1}: ")
        arrival_time = int(input(f"Enter ArrivalTime for process {i+1}: "))
        burst_time = int(input(f"Enter BurstTime for process {i+1}: "))
        processes.append({'ProcessID': process_id, 'ArrivalTime': arrival_time, 'BurstTime': burst_time})
    
    wt, tat, avg_wt, avg_tat = sjf_non_preemptive_scheduling(processes)
    
    print("\nProcess Schedule:")
    for i in range(num_processes):
        print(f"Process {processes[i]['ProcessID']}: Waiting Time = {wt[i]}, Turnaround Time = {tat[i]}")
    
    print(f"\nAverage Waiting Time: {avg_wt}")
    print(f"Average Turnaround Time: {avg_tat}")

if __name__ == "__main__":
    main()
