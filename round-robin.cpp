#include <iostream>
#include <vector>
#include <queue>

using namespace std;

void roundRobin(int p[], int at[], int bt[], int tq, int n) {
    vector<int> wt(n, 0), tat(n, 0), rem_bt(n), exec_order;
    int time = 0, context_switches = 0;
    queue<int> process_queue;
    bool done = false;
    int current = -1;

    for (int i = 0; i < n; i++)
        rem_bt[i] = bt[i];

    // Initially push all processes that have already arrived
    for (int i = 0; i < n; i++) {
        if (at[i] <= time) {
            process_queue.push(i);
        }
    }

    while (!done) {
        done = true;
        if (!process_queue.empty()) {
            int i = process_queue.front();
            process_queue.pop();

            if (rem_bt[i] > 0) {
                done = false;
                exec_order.push_back(p[i]);

                if (rem_bt[i] > tq) {
                    time += tq;
                    rem_bt[i] -= tq;
                    context_switches++;
                } else {
                    time += rem_bt[i];
                    rem_bt[i] = 0;
                    wt[i] = time - at[i] - bt[i];
                    tat[i] = time - at[i];
                }

                // Push any new processes that have arrived during this time
                for (int j = 0; j < n; j++) {
                    if (at[j] > time - tq && at[j] <= time && rem_bt[j] > 0 && j != i) {
                        process_queue.push(j);
                    }
                }

                // If the current process is not finished, push it back
                if (rem_bt[i] > 0) {
                    process_queue.push(i);
                }
            }
        } else {
            // If the queue is empty, increment time to the next process arrival
            for (int j = 0; j < n; j++) {
                if (rem_bt[j] > 0) {
                    time = at[j];
                    process_queue.push(j);
                    break;
                }
            }
        }
    }

    cout << "Process\tAT\tBT\tTAT\tWT\n";
    int total_wt = 0, total_tat = 0;
    for (int i = 0; i < n; i++) {
        total_wt += wt[i];
        total_tat += tat[i];
        cout << p[i] << "\t" << at[i] << "\t" << bt[i] << "\t" << tat[i] << "\t" << wt[i] << "\n";
    }

    float avg_wt = (float)total_wt / n;
    float avg_tat = (float)total_tat / n;

    cout << "Execution Order: ";
    for (size_t i = 0; i < exec_order.size(); i++) {
        cout << exec_order[i];
        if (i != exec_order.size() - 1) {
            cout << " -> ";
        }
    }
    context_switches=exec_order.size()-1;
    cout << "\nContext Switches: " << context_switches << "\n";
    cout << "Average Waiting Time: " << avg_wt << "\n";
    cout << "Average Turnaround Time: " << avg_tat << "\n";
}

int main() {
    int n, tq;

    cout << "Enter the number of processes: ";
    cin >> n;

    int p[n], at[n], bt[n];

    for (int i = 0; i < n; i++) {
        cout << "Enter arrival time and burst time for process " << i + 1 << ": ";
        cin >> at[i] >> bt[i];
        p[i] = i + 1;
    }

    cout << "Enter the time quantum: ";
    cin >> tq;

    roundRobin(p, at, bt, tq, n);

    return 0;
}
