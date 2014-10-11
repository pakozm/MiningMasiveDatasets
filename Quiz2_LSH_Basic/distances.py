import math
def edit_distance(str1, str2):
    N=len(str1)
    M=len(str2)
    INF=4*(N+M)
    F = [ [ INF ]*(M+1) for i in range(0,N+1) ]
    F[0][0] = 0
    for i in range(1,N+1):
        F[i][0] = i
    for j in range(1,M+1):
        F[0][j] = j
    for i in range(1,N+1):
        for j in range(1,M+1):
            if str1[i-1] == str2[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = min(F[i-1][j]+1, F[i][j-1]+1)
    return F[N][M]

def L1_distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def L2_distance(a,b):
    return math.sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2 )

if __name__ == "__main__":
    edit_distance("hello", "hal")
