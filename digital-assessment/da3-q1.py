def isSafe(maximum, allocation, available, need, n, m):
    work = available[:]
    finish = [False] * n
    safeSequence = [-1] * n

    count = 0
    while count < n:
        found = False
        for p in range(n):
            if not finish[p]:
                possible = True
                for j in range(m):
                    if need[p][j] > work[j]:
                        possible = False
                        break
                if possible:
                    for k in range(m):
                        work[k] += allocation[p][k]
                    safeSequence[count] = p
                    count += 1
                    finish[p] = True
                    found = True
        if not found:
            return False, None  # system is not in a safe state

    # display the safe sequence
    print("System is in a safe state.")
    print("Safe sequence is:", ' '.join(map(str, safeSequence)))
    return True, safeSequence  # system is in a safe state


def main():
    n = int(input("Enter the number of processes: "))
    m = int(input("Enter the number of resource types: "))

    allocation = []
    maximum = []
    available = list(map(int, input(f"Enter the available resources (space-separated, {m} values): ").split()))

    print("Enter the allocation matrix (space-separated row-wise):")
    for _ in range(n):
        allocation.append(list(map(int, input().split())))

    print("Enter the maximum resource matrix (space-separated row-wise):")
    for _ in range(n):
        maximum.append(list(map(int, input().split())))

    # calculating the need matrix
    need = [[maximum[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

    safe, _ = isSafe(maximum, allocation, available, need, n, m)
    if not safe:
        print("System is not in a safe state.")


if __name__ == "__main__":
    main()
