def count_p(N, M, K):
    count = 0

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            current_element = (i - 1) * M + j

            # Check right neighbor
            if j + 1 <= M:
                neighbor = current_element + 1
                if abs(current_element - neighbor) < K:
                    count += 1

            # Check bottom neighbor
            if i + 1 <= N:
                neighbor = current_element + M
                if abs(current_element - neighbor) < K:
                    count += 1

    return count

N = int(input())
M = int(input())
K = int(input())
print(count_p(N, M, K))
