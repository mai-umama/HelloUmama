def cred_coins(X,Y):
    coins = X*Y
    bags = coins // 100
    return bags

t = int(input())
for i in range(t):
    X,Y= map(int,input().split())
    result= cred_coins(X,Y)
    print(result)

        
