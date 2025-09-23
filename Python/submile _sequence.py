def sequence(x,n):
    if n % 2 == 0:
        return(0)
    else:
        return x

t = int(input())
for i in range(t):
    x,n = map(int,input().split())
    result= sequence(x,n)
    print(result)
