import math

WHO=0
BID=1
CTR1=2
CTR2=3
CTR3=4
BUDGET=5
YIELD1=6
YIELD2=7
YIELD3=8
CLICKS=9

NAMES = [ 'A', 'B', 'C', 'D', 'E' ]
advertisers = [
    [ 0, 0.10, 0.015, 0.010, 0.005, 1.0 ], # A
    [ 1, 0.09, 0.016, 0.012, 0.006, 2.0 ], # B
    [ 2, 0.08, 0.017, 0.014, 0.007, 3.0 ], # C
    [ 3, 0.07, 0.018, 0.015, 0.008, 4.0 ], # D
    [ 4, 0.06, 0.019, 0.016, 0.010, 5.0 ]  # E
]

CLICKS_PER_DAY = 101

for ad in advertisers:
    for ctr in [ CTR1, CTR2, CTR3 ]:
        ad.append(ctr * ad[BID])
    ad.append(0) # NUM CLICKS

def cmp1(a,b):
    if a[YIELD1] < b[YIELD1]:
        return 1
    if a[YIELD1] > b[YIELD1]:
        return -1
    else:
        return 0

def cmp2(a,b):
    if a[YIELD2] < b[YIELD2]:
        return 1
    if a[YIELD2] > b[YIELD2]:
        return -1
    else:
        return 0

def cmp3(a,b):
    if a[YIELD3] < b[YIELD3]:
        return 1
    if a[YIELD3] > b[YIELD3]:
        return -1
    else:
        return 0

def allocate_ad_slots(advertisers):
    result = []
    copy = [ ad for ad in advertisers if ad[BUDGET] >= ad[BID] ]
    for f in [ cmp1, cmp2, cmp3 ]:
        if len(copy) > 0:
            copy.sort(f)
            result.append(copy[0][WHO])
            copy.pop(0)
    return result

remaining_clicks = CLICKS_PER_DAY
while remaining_clicks > 0:
    slots = allocate_ad_slots(advertisers)
    if len(slots) == 0:
        break
    click_ratio = [ advertisers[who][CTR1+i] for who,i in zip(slots,range(len(slots))) ]
    s = sum(click_ratio)
    click_ratio = [ c/s for c in click_ratio ]
    max_clicks_per_ad = [ math.floor(advertisers[who][BUDGET]/advertisers[who][BID]) for who in slots ]
    n = max_clicks_per_ad[0]
    for i in range(1,len(max_clicks_per_ad)):
        n = min( n, math.floor( max_clicks_per_ad[i] * click_ratio[0] / click_ratio[i] ) )
    n = min( remaining_clicks, math.ceil( n/click_ratio[0] ) )
    remaining_clicks -= n
    for i in range(len(slots)):
        who = slots[i]
        s = sum( [ click_ratio[x] for x in range(i,len(slots)) ] )
        clicks = round( n * ( click_ratio[i] / s ) )
        n -= clicks
        advertisers[who][BUDGET] -= advertisers[who][BID] * clicks
        advertisers[who][CLICKS] += clicks
    assert(n == 0)
    assert( remaining_clicks >= 0 )

for ad in advertisers:
    print NAMES[ad[WHO]], ad[BUDGET] + ad[BID]*ad[CLICKS], ad[BID]*ad[CLICKS], ad[CLICKS]
