# add function
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multyply(x, y):
    return x * y


def devide(x, y):
    return x / y


print("select operation.")
print("1.add")
print("2.subtract")
print("4.multyply")
print("3.devide")


choise = input("Enter choice(1/2/3/4:")

num1 = float(input("Enter First Number:"))
num2 = float(input("Enter Second Number:"))

if choise == '1':
    print(num1, "+", num2, "=", add(num1, num2))

if choise == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

if choise == '3':
    print(num1, "*", num2,"=", multyply(num1,num2))

if choise == '4':
    print(num1, "/", num2,"=", devide(num1,num2))
