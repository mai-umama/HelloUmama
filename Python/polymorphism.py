# print(1 + 2) #3
# print(type(1))
# print("art"+"school") #concatenate
# print(type("art"))
# print([1,2,3] + [4,5,6]) #merge
# print(type([1,2,3]))

# class Complex:
#     def __init__(self, real,img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i +" , self.img,"j")

#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal, newImg)

# num1 = Complex(3,7)
# num1.showNumber()

# num2 = Complex(4, 2)
# num2.showNumber()

# num3 = num1 - num2
# num3.showNumber()

#PRACTISE
# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
    
#     def showDetails(self):
#         print("role:",self.role)
#         print("dept:",self.dept)
#         print("salary:",self.salary)

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name= name
#         self.age = age
#         super().__init__("Engineer","IT","75000")


# e1= Engineer("Aurka","28" )
# e1.showDetails()
# print("name:",e1.name)

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,odr2):
        return self.price > odr2.price
    
odr1 = Order("chips",20)
odr2 = Order("tea",15)

print(odr1 > odr2)
