lower = 1
higher = 1
guess = 1

def call(i):
    print("buf[" + str(i) + "]")
    val = int(input())
    return val

while True:
    guess = (guess + 1) * 2 - 1
    val = call(guess)
    
    if val == 0:
        higher = guess
        break
    else:
        lower = guess

step = higher - lower
while True:
    # print(lower, higher)
    if higher - lower <= 0:
        print("debugging time")
        break
    if higher - lower == 1:
        print("strlen(buf) = " + str(higher))
        break
    
    step = max(step//2, 1)

    guess = lower + step
    
    val = call(guess)

    if val != 0:
        lower = guess
    else:
        higher = guess



    

