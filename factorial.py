fact = 1
num = int(input("Enter any numer: "))
for i in range(1,(num+1)):
    fact = fact * i
print("The factorial of the",num, "is",fact)

i = 1
fact = 1
while(i <= num):
    fact = fact * i
    i = i+1

print ("The factorial of the number", num, "is", fact)

