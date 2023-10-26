lookup = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

# def romToArab(s):
#     stack = []
#     flag = float("-inf")
#     for i in range(len(s)-1, -1, -1):
#         if lookup[s[i]] > flag:
#             print("changed")
#             flag = lookup[s[i]]
        
#         print(flag)

#         if not stack:
#             stack.append(lookup[s[i]])
#         if stack and lookup[s[i]] > stack[-1]:
#             stack.append(lookup[s[i]])
#             flag = lookup[s[i]]
        
#         print(stack)
#         if stack and lookup[s[i]] < flag:
#             temp = stack.pop()
#             stack.append(temp-lookup[s[i]])
    
#     return sum(stack)

def romToArab2(s):
    s = [lookup[i] for i in s]
    flag = s[-1]
    final = 0
    while len(s) > 0:
        val = s.pop()
        if val < flag:
            final -= val
        else:
            flag = val
            final += val
    return final


n = int(input())
for i in range(n):
    print(romToArab2(input()))