#WAP to get student details using class

class student:
    def getData(self):
        self.name=input("Enter name")
        self.ID=int(input("Enter ID"))
    def showData(self):
        print(self.name)
        print(self.ID)

s1=student()
s1.getData()
s1.showData()
