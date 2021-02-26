def sellablePairs(ar):
    pairs = 0
    for color in ar:
        ar.pop(0)
        for j in range(0, len(ar)):
            if(color == ar[j]):
                pairs += 1
                ar.pop(j)
                break
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