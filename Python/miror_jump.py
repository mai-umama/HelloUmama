def mirror_jump(K,N):

    return min(K , N-K)

t = int(input())
for i in range(t):
    N,K = map(int,input().split())
    print(mirror_jump(K,N))

# def mirror_jump(K,N):

#     if K > (N*0.5):
#         moves = N-K
#         return moves

#     elif K < (N/2):
#         moves = K
#         return moves

#     else:
#         return 0

# t = int(input())
# for i in range(t):
#     N,K = map(int,input().split())
#     print(mirror_jump(K,N))