num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
try:
    num3 = num1/num2
except:
    print("You can't divide the number by zero")
else:
    print(num3)
