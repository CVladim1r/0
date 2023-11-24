n = int(input())
a = list(map(int, input().split()))

def check(k, x):
    cnt = 0
    for i in range(n):
        if a[i] <= x:
            cnt += 1
        else:
            cnt = 0
        if cnt == k:
            return True
    return False

res = []
for k in range(1, n + 1):
    l, r = 1, max(a)
    while l < r:
        mid = (l + r) // 2
        if check(k, mid):
            r = mid
        else:
            l = mid + 1
    res.append(l)

print(*res)
