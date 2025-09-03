def is_leap(year):
    if(year %4==0 and year%100 != 0) or(year%400==0):
        print(True)
        return True
    else:
        print(False)
        return False
    
# to pass the test cases on hackerrank we have to write return 
# if we want to run the code normally we must call the function 
# like is_leap(1900)