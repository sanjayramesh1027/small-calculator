#define the functions

def add(x,y):
    """"This function adds 2 numbers"""
    return x + y

def substract(x,y):
    """"This function adds 2 numbers"""
    return x - y

def multiply(x,y):
    """"This function adds 2 numbers"""
    return x * y

def devide(x,y):
    """"This function adds 2 numbers"""
    return x/y

def power(x,y):
    """"this  gives power"""

    return pow(x,y)

#take input from user
print("select operation.")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Devide")
print("5.power")
choice=input("Enter choice 1/2/3/4/5:")

num1 =float(input("Enter first number: "))
num2 =float(input("Enter the second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1,num2))

elif choice == '2':
    print(num1, "-", num2, "=", substract(num1,num2))

elif choice == '3':
    print(num1, "x", num2, "=", multiply(num1,num2))

elif choice == '4':
    print(num1, "/", num2, "=", devide(num1,num2))