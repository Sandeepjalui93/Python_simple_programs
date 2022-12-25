class student:
    def getData(self):
        self.name=input("Enter name=")
        self.ID=int(input("Enter ID="))
        
    def showData(self):
        print("Student name",self.name)
        print("ID is",self.ID)
        
class test(student):
    def getData(self):
        student.getData(self)
        self.physics=int(input("Enter physics marks="))
        self.chemistry=int(input("Enter chemistry marks="))
        self.maths=int(input("Enter maths marks="))
        
    def showData(self):
        student.showData(self)
        print("Physics marks is",self.physics)
        print("Chemistry marks is",self.chemistry)
        print("Maths marks is",self.maths)
        

t1=test()

print("----------------")



t1.getData()
t1.showData()


