import math
T = int (input())
for i in range(T):
    N,K= map(int,input().split())
    A = list(map(int,input().split()))
    result = []
    for j in A:
        if K>= j:
            result.append('1')
            K -= j
        else:
            result.append('0')

    print(''.join(result))
