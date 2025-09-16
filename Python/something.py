T = int(input())  
for _ in range(T):
    R = list(map(int, input().split()))  
    
    if all(d == 0 for d in R):   
        print("IN")
    else:
        print("OUT")