def sellablePairs(ar):
    pairs = 0
    start = 0
    for i in range(start, len(ar)):
        for j in range(start+1, len(ar)):
            if(ar[i] == ar[j]):
                pairs += 1
                start += 1
                break
        start += 1
    return pairs

pairs = 0
n = int(input())
if n >= 1 and n <= 100:
    ar = [int(item) for item in input().split()]
    if len(ar) >= 0 and len(ar) <= n:
        pairs = sellablePairs(ar)
        print(pairs)
    else: print("invalid socks input, not more than stocks")
else: print("invalid stock input, not more than 100 and must positive number")