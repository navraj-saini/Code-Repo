class Xyz:
    def __init__(self,Fname,Lname,age,Gen):
        self.fname=Fname
        self.lname=Lname
        self.AGE=age
        self.GEN=Gen
        
    def frst_last(self):
        print("Fullname is : ", Fname + Lname)
        
    def Oage(self):
        print("The age and gender is: " + Gen , age)

Fname=str(input("Fname : "))
Lname=str(input("Lname : "))
age=int(input("Age : "))
Gen=str(input("Gen : "))

xyz=Xyz(Fname,Lname,age,Gen)
xyz.Oage()
xyz.frst_last()
