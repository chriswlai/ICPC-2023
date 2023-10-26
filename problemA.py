N, K = map(int, input().split())

cts = [K + 1]
while cts[-1] <= 5 * 10**18 + 1:
    cts.append(cts[-1]*K + 1)

ls = [1]
for i in range(len(cts)-1):
    ls.append(ls[-1]*K + 1)

final = 0
while len(cts) > 0:
    if N < K: 
        break
    bigboi = ls.pop()
    bigboisize = cts.pop()
    while N >= bigboisize:
        N -= bigboisize
        final += bigboi
        if N < K: 
            break
    if N < K: 
        break

if final == 0:
    print(1)
else:    
    print(final)