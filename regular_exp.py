import re

usr_inpt=str(input("Enter String: "))
srch_exp=re.findall("Inform.",usr_inpt)
print(srch_exp)



#############################################################
import re

usr_inpt=str(input("Enter String: "))
srch_exp=re.findall("Inform",usr_inpt)

for i in srch_exp:
    print(i)
#############################################################
