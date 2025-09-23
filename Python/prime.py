# def test(N):
#     if N <= 1:
#         return("no")
#     if N % 3== 0 :
#         return("no")
#     if N % 2 == 0:
#         return ("no")
#     if N % 5 == 0:
#         return("no")
#     if N % 7 == 0 :
#         return("no")
#     if N % 11 == 0:
#         return("no")
        
#     else :
#        return ("yes")
    
# t = int(input())
# for i in range(t):
#     N = int(input())
#     result= test(N)
#     print(result)


import math
def test(N):
    if N <= 1:
        return("no")
    if N == 2:
        return("no")
    if N % 2 == 0:
        return ("no")
    for i in range(3, int(math.sqrt(N))+1, 2):
        if N % i == 0:
            return ("no")
    return ("yes")
        
t = int(input())
for j in range(t):    
    N = int(input())     
    result= test(N)
    print(result)