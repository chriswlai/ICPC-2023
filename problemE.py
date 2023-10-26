timeLookup = []
max_occur = 0
# occurLookup = []

items = 0
n = int(input())
for i in range(n):
    timeLookup.append(list(map(int, reversed(input().split()))))
    # occurLookup.append([timeLookup[i][1],timeLookup[i][0]])
    max_occur = max(max_occur, timeLookup[i][1])
    items += timeLookup[i][1]

timeLookup.sort()
# occurLookup.sort(reverse=True)
time = 0

print(timeLookup)

while len(timeLookup) >= 2:
    print(timeLookup)

    if timeLookup[-1][0] != occurLookup[-1][1]:
        time += max(timeLookup[-1][0], occurLookup[-1][1])
        timeLookup[-1][1] -= 1
        timeLookup[-2][1] -= 1

    if timeLookup[-2][1] == 0:
        timeLookup.pop(-2)
    if timeLookup[-1][1] == 0:
        timeLookup.pop()

    time += timeLookup[0][1] * timeLookup[0][0]
print(time)