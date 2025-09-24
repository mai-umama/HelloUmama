t =  int(input())
for i in range (t):
    X,Y= map(int,input().split())

    groups = (X+Y)//3
    twos_group=min(Y,groups) #if the num of Y is greater thn groups it still take the smallest num cause the min function
    score= groups + twos_group
    print(score)