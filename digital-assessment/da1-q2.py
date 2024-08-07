def sjf_preemptive_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: x['ArrivalTime'])
    
    remaining_time = [p['BurstTime'] for p in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completed = 0
    current_time = 0
    min_burst = float('inf')
    shortest = 0
    check = False
    
    while completed != n:
        for j in range(n):
            if (processes[j]['ArrivalTime'] <= current_time and
                remaining_time[j] < min_burst and remaining_time[j] > 0):
                min_burst = remaining_time[j]
                shortest = j
                check = True
        if not check:
            current_time += 1
            continue
        remaining_time[shortest] -= 1
        min_burst = remaining_time[shortest]
        if min_burst == 0:
            min_burst = float('inf')
        if remaining_time[shortest] == 0:
            completed += 1
            check = False
            finish_time = current_time + 1
            waiting_time[shortest] = (finish_time - processes[shortest]['BurstTime'] - processes[shortest]['ArrivalTime'])
            if waiting_time[shortest] < 0:
                waiting_time[shortest] = 0
        current_time += 1
    
    for i in range(n):
        turnaround_time[i] = processes[i]['BurstTime'] + waiting_time[i]
    
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
    
    wt, tat, avg_wt, avg_tat = sjf_preemptive_scheduling(processes)
    
    print("\nProcess Schedule:")
    for i in range(num_processes):
        print(f"Process {processes[i]['ProcessID']}: Waiting Time = {wt[i]}, Turnaround Time = {tat[i]}")
    
    print(f"\nAverage Waiting Time: {avg_wt}")
    print(f"Average Turnaround Time: {avg_tat}")

if __name__ == "__main__":
    main()
