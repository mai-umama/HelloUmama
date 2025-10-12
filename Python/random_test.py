import math
n = int(input())
def is_prime(n):
    if(n<=1):
        return False
    for i in range (2,int(math.sqrt(n)+1)):
        if(n%i == 0):
            return False
    return True

if is_prime(n):
    print("NO PUNISHMENT")
else:
    for i in range(n):
        print("I DID NOT DO THE ASSIGNMENT.")
