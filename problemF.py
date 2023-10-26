N = int(input())
adj_list = {}
for i in range(N-1):
    a, b = map(int, input().split())
    if a in adj_list:
        adj_list[a].append(b)
    else:
        adj_list[a] = [b]
    if b in adj_list:
        adj_list[b].append(a)
    else:
        adj_list[b] = [a]

to_parent = {1: -1}
stack = [1]
hasBeen = {1: -1}
while len(stack) > 0:
    curr = stack.pop()
    children = adj_list[curr]
    for child in children:
        if not child in hasBeen:
            to_parent[child] = curr
            stack.append(child)
            hasBeen[child] = True

final = []

def genPrimes(N):
    primes = [2]
    for i in range(3, 100000):
        if len(primes) == N:
            break
        isComposite = False
        for prime in primes:
            if i % prime == 0:
                isComposite = True
                break
        if not isComposite:
            primes.append(i)
    return primes

primes = genPrimes(60)
nums = {i for i in range(4, N+1)}
primes.reverse()

final = []
for i in range(1, N + 1):
    if i == 1:
        final.append(i)
    else:
        while primes[-1] in nums:
            primes.pop()
        final.append(to_parent[i]*primes.pop())
        nums.add(final[-1])

print(" ".join(list(map(str,final))))