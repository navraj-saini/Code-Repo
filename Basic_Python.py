#list
l=[1,2,3,4,5,6,7,8]
l.append(87)
print(l)
p=[22,33]
l.extend(p)
print(l)




#################################################

#Shopping 

list_x=[]

Usr_inpt=int(input("Enter size of List: "))

for i in range(1,Usr_inpt+1):
    Shopping_Items=str(input("Enter {} Item : ".format(i)))
    
    list_x.append(Shopping_Items)
    
print(list_x
