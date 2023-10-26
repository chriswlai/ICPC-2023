N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

if N <= M:
    print(max(arr))
else:
    final = []
    subset_len = (N - M) * 2
    for i in range(N - M):
        final.append(arr[i] + arr[subset_len - i - 1])
    print(max(max(arr),max(final)))