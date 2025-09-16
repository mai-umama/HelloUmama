# n = int(input())
# notes = n * 4
# print(notes)

# n = int(input())
# if(n == 1):
#     print("one")
# elif(n== 2):
#     print("two")
# elif(n == 3):
#     print("three")
# elif(n == 4):
#     print("four")
# elif( n== 5):
#     print("five")
# elif( n== 6):
#     print("six")
# elif( n== 7):
#     print("severn")
# elif(n==8):
#     print("eight")
# elif(n==9):
#     print("nine")

# else:
#     print("Greater than 9")

# N = int(input())

# if( N == 404):
#     print("NOT FOUND")
# else:
#     print("FOUND")

# X = int(input())
# final_rent = 2 * X
# print(final_rent)

# n = int(input())

# sum = 0

# while n > 0:
#     sum += n %10
#     n //= 10
# print(sum)

# T = int(input())  
# for _ in range(T):
#     R = list(map(int, input().split()))  
    
#     if all(d == 0 for d in R):   
#         print("IN")
#     else:
#         print("OUT")

# n = int(input())
# count = 0
# for i in range(n):
#     a,b,c = map(int,input().split())
#     if (a+b+c >= 2):
#         count+=1
# print(count)

T = int(input())
for i in range(T):
    N =int(input())
    S = input().strip()
    complementary={
        'A':'T',
        'T':'A',
        'C':'G',
        'G': 'C'
    }
    final ="".join(complementary[ch] for ch in S)
    print(final)