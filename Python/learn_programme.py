# n = int(input("enter num:"))
# count = 0
# i = 5

# while n // i > 0:
#     count += n // i
#     i *= 5

# print(count)



# a = '2'
# b = 3
# sum = a + b
# print(sum)

# friends =["tonu", "israt", "sami","azmain","Mati"]
# heros = ["captain","iron man","Thor","hulk"]

# def print_list(list):
#     for item in list :
#         print(item, end =" ")


# def cal_fact(n):
#     fact = 1 
#     for i in range(1 , n+1):
#         fact *= i
#     print(fact)

# def cal_INR(n):
#     converter= n * 83
#     print(n ,"USD =" ,converter,"INR")
#     return converter


# def check_num():
#     n = int(input("Enter a number: "))
#     if ( n%2== 0):
#         return"even"
#     else:
#         return"odd"
       
# check_num()

# def show(n):
#     if(n == -2):
#         return
#     print(n)
#     show(n-1)
#     print("end")

# show(5) #5,4,3,2,1
    
# def print_list(list,idx=0):
#     if( idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)

# fruits = [ "mango","lichi","apple","jackfruit","banana"]

# print_list(fruits)


# age = int(input("enter your age: "))
# gender = input("enter your genter: ")

# if(gender == "female"and age >= 18):
#    print("can get married as a girl")
#    print("female,can vote")

# elif(gender == "male" and age == 18):
#    print("male,can vote")

# elif(gender == "male" and age == 21):
#    print("male,can vote")
#    print("can get married")

# else:
#    print("can vote")


# T = int(input("enter test case: "))

# for _ in range(T):
#     A, B = map(int, input("Enter two integers: ").split())
#     X = (B - A % B) % B
#     print(X)

# T = int(input("Enter number of test cases: "))

# for _ in range(T):
#     A, B = map(int, input("Enter two integers A and B separated by space: ").split())
#     X = (B - A % B) % B
#     print(X)

# f = open("python\demo.txt" , "a+")
# f.write("hello")

# print(f.read())
# f.write("hello")

# f.close()

# with open("python\demo.txt" , "r") as f:
#     data = f.read()
#     print(data)


# with open("python\demo.txt" , "w") as f:
#     f.write("new data")




# with open("python\sample.txt" , "r") as f:
#     data = f.read()

# new_data = data.replace("Java","Python")
# print(new_data)

# with open("python\sample.txt" , "w") as f:
#     f.write(new_data)
# def find_word():
#     word = "learning"
#     with open("python\sample.txt" , "r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("Not Found")
# def find_line():
#     word = "sql"
#     data = True
#     line_no=1
#     with open("python\sample.txt" , "r") as f:
#         while data :
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no +=1

#     return -1

# print(find_line())


# with open("python\sample.txt", "r") as f:
#     data = f.read()
#     print(data)

# num = ""
# for i in range(len(data)):
#     if(data[i] == ","):
#         print(int(num))
#         num = ""

#     else:
#         num += data[i]
# count = 0
# with open("python\sample.txt", "r") as f:
#      data = f.read()
   
#      nums= data.split(",")
#      for val in nums :
#           if (int(val)%2 == 0):
#                count+= 1

# print(count)

# chapter 8

# creating class
# class Student:
#     college_name = "ABC college "
#     name = "anomyous"
#     def __init__(self,fullname,marks):
#         self.name = fullname
#         self.marks = marks
#     def welcome(self):
#         print("welcome student",self.name)

#     def get_marks(self):
#         return self.marks
# s1 = Student( "Akif",99)
# s1.welcome()
# print(s1.get_marks()) 

# print(s1.name,s1.marks)

# s2 = Student("Maisha",84)
# print(s2.name,s2.marks)

# print(Student.college_name)

# # class car:
#     color = "green"
#     brand = "marcidies"

# car1 = car()
# print(car1.color)
# print(car1.brand)

# class Student:
#     def __init__(self,name,marks): #[99,96,78]
#         self.name = name
#         self.marks = marks 

#     @staticmethod
#     def hello():
#         print("Hello")
#     def Get_average(self):
#         sum=0
#         for val in self.marks :
#             sum +=val
#         print("Hi",self.name,"your avg score is:", sum/3)

# s1 = Student("Muza",[96,85,83])
# s1.Get_average()

# s2 =Student("Aurka",[90,79,98])
# s2.Get_average()
# s1.hello()

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True 
#         self.acc = True 
#         print("car started..")

# car1 = Car()
# car1.start()

# class Account :
#     def __init__(self,bal,acc):
#         self.balance = bal 
#         self.account_no= acc

#     def debit(self,amount):
#         self.balance-= amount
#         print("Tk",amount,"was debited")
#         print("Total balance=", self.get_balance)

#     def credit(self,amount):
#         self.balance += amount
#         print("Tk",amount,"was credited")
#         print("Total balance=", self.get_balance())

#     def get_balance(self):
#         return self.balance 
    
# acc1 = Account(10000,12345)
# acc2= Account(20000,78954)
# print(acc1.balance)
# print(acc1.account_no)

# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(40000)
# acc1.debit(10000)

# acc2.debit(500)

# class Student:
#     def __init__(self,name):
#         self.name= name

# s1 = Student("Umama")
# print(s1.name)
# del s1.name 
# print(s1.name)

# class Account:
#     def __init__(self,acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account("1234", "abcd")

# print(acc1.acc_no)
# # print(acc1.__acc_pass)
# print(acc1.reset_pass())

# class Person:
#     __name= "anonymous"

#     def __hello():
#         print("hello person")

# p1 = Person()
# print(p1.__hello())

# class Person :
#     __name ="anonymus"
#     def __hello(self):
#         print("Hello user")

#     def welcome(self):
#         self.__hello()
# p1 = Person()

# print(p1.welcome())

# class Car :
#     def __init__(self,type):
#          self. type= type

#     @staticmethod
#     def start():
#         print("car started..") 

#     @staticmethod 
#     def stop():
#         print("car stopped")

# class ToyotaCar(Car):
#      def __init__(self,name,type ):
#         super().__init__(type)
#         self.name = name

# car1 = ToyotaCar("pirus","electric")
# print(car1.type) 

# class fortuner(ToyotaCar):
#     def __init__(self,type):
#          self.type= type
# car1 = fortuner("disel")

# car1.start()
# print(car1.brand)

# class A :
#     varA = "welcome to class A"
# class B:
#     varB="welcome to class B"
    
# class C(A,B):
#     varC = "welcome to class C" 
# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# class Person:
#     name = "anonymous"

#     # def changeName(self,name):
#     #     self.__class__.name  = name
#     @classmethod
#     def changeName(cls, name):
#         cls.name = name 

# p1 = Person()
# p1.changeName("Aurka")
# print(p1.name)
# print(Person.name)

# class Student:
#     def __init__(self,phy,che,math):
#         self.phy = phy 
#         self.che = che
#         self.math = math
#         self.percentage = str((self.phy + self.che + self.math)/3) + "%"
    
#     def calcPercentage(self):
#         self.percentage =  str((self.phy + self.che + self.math)/3) + "%"

# stu1 = Student(98,97,99)
# print(stu1.percentage)

# stu1.phy = 86
# print(stu1.phy)
# stu1.calcPercentage() 
# print(stu1.percentage)

class Student:
    def __init__(self,phy,che,math):
        self.phy = phy 
        self.che = che
        self.math = math
    @property
    def percentage(self): #attribute
        return str((self.phy + self.che + self.math)/3) + "%"
stu1 = Student(99,96,97)
print(stu1.percentage)

stu1.phy = 86 
print(stu1.percentage)