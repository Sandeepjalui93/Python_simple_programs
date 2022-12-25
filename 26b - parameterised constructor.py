#WAP to get student details using class

class student:
    def __init__(self, n, i):
        self.name = n
        self.id = i
    def showData(self):
        print(self.name)
        print(self.id)


name=input("Enter name")
ID=int(input("Enter ID"))
s1=student(name, ID)
#s1.getData()
s1.showData()
