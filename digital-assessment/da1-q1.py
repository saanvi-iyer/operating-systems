def fcfs_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: x['ArrivalTime'])
    
    current_time = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    for i in range(n):
        if current_time < processes[i]['ArrivalTime']:
            current_time = processes[i]['ArrivalTime']
        waiting_time[i] = current_time - processes[i]['ArrivalTime']
        current_time += processes[i]['BurstTime']
        turnaround_time[i] = waiting_time[i] + processes[i]['BurstTime']
    
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
    
    wt, tat, avg_wt, avg_tat = fcfs_scheduling(processes)
    
    print("\nProcess Schedule:")
    for i in range(num_processes):
        print(f"Process {processes[i]['ProcessID']}: Waiting Time = {wt[i]}, Turnaround Time = {tat[i]}")
    
    print(f"\nAverage Waiting Time: {avg_wt}")
    print(f"Average Turnaround Time: {avg_tat}")

if __name__ == "__main__":
    main()
