'''num = int(input("Enter the number: "))
for i in range(1, (num + 1)):
    print("\n")
    for j in range(1, 11):
        print (i, "x", j, "=", i*j)
'''
    
num = int(input("Enter the number: "))
exp = int(input("Enter the exponent: "))
result = 1
for i in range(1,(exp+1)):
    result = result * num
print ("The result is:", result)
