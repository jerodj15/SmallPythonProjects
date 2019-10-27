class person:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def __str__(self):
        return("name: {}\nage: {}".format(self.name,self.age))

class teacher(person):
    def __init__(self,name,age,sub):
        person.__init__(self, name, age)
        self.sub = sub
    def __str__(self):
        return (person.__str__(self) + "\nsub : {}".format(self.sub))


class student(person):
    def __init__(self,name,age,loan):
        person.__init__(self, name, age)
        self.loan = loan
    def __str__(self):
        return (person.__str__(self) + "\nloan : {}".format(self.loan))
