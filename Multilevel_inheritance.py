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
        
    def showMarks(self):
        print("Physics marks is",self.physics)
        print("Chemistry marks is",self.chemistry)
        print("Maths marks is",self.maths)
        
class result(test):
    def calc(self):
        self.tot = self.physics+self.chemistry+self.maths
    def show(self):
        print("totale is ", self.tot)

t1=result()

name=input("Enter name=")
ID=int(input("Enter ID="))

t1.getData(name,ID)
t1.studentDetails()

print("----------------")

p1=int(input("Enter physics marks="))
c1=int(input("Enter chemistry marks="))
m1=int(input("Enter maths marks="))

t1.getTest(p1,c1,m1)

t1.showMarks()
t1.calc()
t1.show()
