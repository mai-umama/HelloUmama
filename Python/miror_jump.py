def mirror_jump(K,N):

    return min(K , N-K)

t = int(input())
for i in range(t):
    N,K = map(int,input().split())
    print(mirror_jump(K,N))