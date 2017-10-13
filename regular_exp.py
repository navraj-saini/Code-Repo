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

Regular Expression

import re

strn=input("Enter String: ")

if regex is re.findall("\w{0,6}.\w{0,6}@\w{0,6}.\w{0,3}",strn):
    print("Valid Email")
    print(regex)
else:
    print("Invalid")


