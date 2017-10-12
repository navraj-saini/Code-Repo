class Nidhi:
    
    def __init__(self,Name,Age,Gen,salary,chall):
        
        self.Name=Name
        self.Age=Age
        self.Gen=Gen
        self.email= Name+"24"+"@gmail.com"
        
    def Deaf(self):
        print("Nidhi is having this much Sal: ",salary)
        
    def Move(self):
        print("Nidhi moves very:"+chall)
        
Name=str(input("Enter name: "))
Age=int(input("Enter Age: "))
Gen=str(input("Enter Gen: "))
salary=int(input("Enter salary: "))
chall=str(input("Enter Chall :"))

nidhi=Nidhi(Name,Age,Gen,salary,chall)
nidhi.Deaf()
nidhi.Move()
print(nidhi.email)
