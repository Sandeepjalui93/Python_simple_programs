#WAP to get n number student details using class

class student:
    def getData(self):
        self.name=input("Enter name")
        self.ID=int(input("Enter ID"))
    def showData(self):
        print(self.name)
        print(self.ID)
li = []
for i in range(3):
   li.append(student())
   li[i].getData()
   

for i in range(3):
    li[i].showData()
