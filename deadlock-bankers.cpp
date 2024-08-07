#include <iostream>
#include <vector>
using namespace std;

// safety algorithm
bool isSafe(vector<vector<int>>& max, vector<vector<int>>& allocation, vector<int>& available, vector<vector<int>>& need, int n, int m) {
    vector<int> work = available;
    vector<bool> finish(n, false);
    vector<int> safeSequence(n);

    int count = 0;
    while (count < n) {
        bool found = false;
        for (int p = 0; p < n; p++) {
            if (!finish[p]) {
                bool possible = true;
                for (int j = 0; j < m; j++) {
                    if (need[p][j] > work[j]) {
                        possible = false;
                        break;
                    }
                }
                if (possible) {
                    for (int k = 0; k < m; k++) {
                        work[k] += allocation[p][k];
                    }
                    safeSequence[count++] = p;
                    finish[p] = true;
                    found = true;
                }
            }
        }
        if (!found) {
            return false; // system is not in a safe state
        }
    }
    // display the safe sequence
    cout << "System is in a safe state.\nSafe sequence is: ";
    for (int i = 0; i < n; i++) {
        cout << safeSequence[i] << " ";
    }
    cout << endl;
    return true; // system is in a safe state
}

int main() {
    int n, m;
    cout << "Enter the number of processes: ";
    cin >> n;
    cout << "Enter the number of resource types: ";
    cin >> m;

    vector<vector<int>> max(n, vector<int>(m));
    vector<vector<int>> allocation(n, vector<int>(m));
    vector<int> available(m);
    vector<vector<int>> need(n, vector<int>(m));

    cout << "Enter the allocation matrix:\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> allocation[i][j];
        }
    }

    cout << "Enter the maximum resource matrix:\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> max[i][j];
        }
    }

    cout << "Enter the available resources:\n";
    for (int i = 0; i < m; i++) {
        cin >> available[i];
    }

    // calculating the need matrix
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            need[i][j] = max[i][j] - allocation[i][j];
        }
    }

    if (!isSafe(max, allocation, available, need, n, m)) {
        cout << "System is not in a safe state." << endl;
    }

    return 0;
}
