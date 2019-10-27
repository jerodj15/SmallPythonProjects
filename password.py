password = "williams"
for i in range (3):
    pwd = input("Please enter the password: ")
    j = 2
    if (pwd == password):
        print("Welcome")
        break
    else:
        print("Wrong password, chances left", j-i)
        
        continue

print("Try next time")
