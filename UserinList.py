Databse=["Harry","Vicky","Dami","Vijay"]

name=str(input("Enter Name: "))

if name in Databse:
    print("Welcome back",name)
else:
    print("Please Sign in first")
    
#########################################################################################  
    
Databse=["Harry","Vicky","Dami","Vijay"]

name=str(input("Enter Name: "))

if name in Databse:
    print("Welcome back",name)
else:
    print("Please Sign in first")
    new_user=str(input("Enter Name to Sign up: "))
    x=Databse.append(new_user)
    print("Successfull")
    
print(Databse)

#########################################################################################
