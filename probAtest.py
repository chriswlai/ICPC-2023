def calc(N, K):
    cts = [K + 1]
    while cts[-1] <= 10**9 + 1:
        cts.append(cts[-1]*K + 1)

    ls = [1]
    for i in range(len(cts)-1):
        ls.append(ls[-1]*K + 1)

    final = 0
    while len(cts) > 0:
        bigboi = ls.pop()
        bigboisize = cts.pop()
        while N >= bigboisize:
            N -= bigboisize
            final += bigboi

    print(final)

for i in range(1, 50):
    # for j in range(2, 10):
        calc(i,2)