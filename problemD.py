# die = []
# for i in range(3):
#     temp = [int(x) for x in input().split()]
#     die.append(temp)

# exp = []
# for arr in die:
#     exp.append(sum(arr) / 2)

# print(exp)

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

def canWin(a, b):
    W = 0
    L = 0
    T = 0
    for val1 in a:
        for val2 in b:
            if val1 > val2: 
                W += 1
            elif val1 < val2:
                L += 1
            else:
                T += 1
    ratio = (W - L + 0.01)*(36 - T)
    if ratio <= 0:
        return False
    return True

if canWin(a, b) and canWin(a, c):
    print(1)
elif canWin(b, a) and canWin(b, c):
    print(2)
elif canWin(c, a) and canWin(c, b):
    print(3)
else:
    print("No dice")