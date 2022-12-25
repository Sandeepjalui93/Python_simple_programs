class student:
    def getData(self,n,i):
        self.name=n
        self.ID=i

    def studentDetails(self):
        print("Student name",self.name)
        print("ID is",self.ID)
        
class test(student):
    def getTest(self,p,c,m):
        self.physics=p
        self.chemistry=c
        self.maths=m
        
    def result(self):
        print("Physics marks is",self.physics)
        print("Chemistry marks is",self.chemistry)
        print("Maths marks is",self.maths)
        

t1=test()

name=input("Enter name=")
ID=int(input("Enter ID="))
print("----------------")

p1=int(input("Enter physics marks="))
c1=int(input("Enter chemistry marks="))
m1=int(input("Enter maths marks="))
t1.getData(name,ID)
t1.getTest(p1,c1,m1)

t1.studentDetails()
t1.result()

