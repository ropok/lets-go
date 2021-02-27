import math

def countingValleys(s):
    sea_level = 0
    valley = 0
    temp = 0
    temp_valley = 0
    for step in s:
        temp = sea_level
        if step == 'U':
            sea_level += 1
        elif step == 'D':
            sea_level -= 1
        if temp == 0 and sea_level == -1:
            temp_valley += 0.5
        if temp == -1 and sea_level == 0:
            temp_valley += 0.5
    valley = math.floor(temp_valley)
    return valley

valleys = 0
n = int(input())
if n >= 2:
    s = [str(item) for item in input().split()]
    if len(s) == n:
       valleys =  countingValleys(s)
       print(valleys)
    else: print("invalid number of steps input, must be same as steps's number")
else: print("invalid number of steps, at least 2")