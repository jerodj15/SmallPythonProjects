""" Intiail tutorial
class student:
    def details(self,name,age):
        self.age = age
        self.name = name
        print("the name is {} and the age is {}".format(name,age))

    def __init__(self):
        balance = 20.00
        print("You are welcome")
        print("Balance is {}".format(balance))
"""
"""class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        balance = 0
        credit = 55
        print("The name is {} and the age is {}. The balance is {} and the credit is {}".format(name,age, balance, credit))
"""        
class student:
    def __init__(self, name):
        self.name = name
        self.attend = 0
        self.marks = []
        print("Welcome {} to the school".format(name))
    def addmark (self, ma):
        self.marks.append(ma)
    def attenddays(self):
        self.attend += 1
    def getavg(self):
        return sum(self.marks) / len(self.marks)
