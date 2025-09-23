def rent_vs_purchase(X,Y):
    month = 0
    if (X * month >= Y):
        return 0
    
    return (Y-1)//X

T = int(input())

for i in range(T):
    X,Y= map(int,input().split())
    result = rent_vs_purchase(X,Y)
    print(result)
        

# def rent_vs_purchase(X, Y):
#     month = 0
#     if X >= Y:        # ভাড়া কিনে ফেলার দামের সমান বা বেশি হলে
#         return 0
    
#     while X * (month + 1) < Y:
#         month += 1
    
#     return month      # এখানে অবশ্যই return করতে হবে


# T = int(input())
# for i in range(T):
#     X, Y = map(int, input().split())
#     result = rent_vs_purchase(X, Y)
#     print(result)
  