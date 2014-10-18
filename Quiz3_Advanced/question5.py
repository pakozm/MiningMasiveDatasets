wlen=40
time=100
buckets = {
    100 : 1,
    98  : 1,
    95  : 2,
    92  : 2,
    87  : 4,
    80  : 8,
    65  : 8
}

## Suppose that at times 101 through 105, 1's appear in the stream. Compute the
## set of buckets that would exist in the system at time 105. Then identify one
## such bucket from the list below. Buckets are represented by pairs (end-time,
## size).

buckets2 = {
    10? : 1
    100 : 2,
    95  : 4,
    87  : 4,
    80  : 8,
}
