year = int(input())

if ( year%2==0 and year%100 != 0) or year % 400 == 0 :
    print(True)
else:
    print(False)