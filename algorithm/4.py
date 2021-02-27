
# pressed the switch
def switch(lamp):
    if lamp == 0: return 1
    else: return 0

# declare lamp (off), 0 means off, 1 means on
lamps = [0] * 100
trips = 100
# first trip
for i in range (0, 100):
    lamps[i] = switch(lamps[i])

for trip in range (2, trips+1):
    n = 0
    while trip**n < 100:
        switches = trip ** n
        lamps[switches] = switch(lamps[switches])
        n += 1
print("after 100 trips from A to B, there are %d lamps will turned on" % sum(lamps))