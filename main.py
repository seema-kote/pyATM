# Author name : Kote Seema M ('https://github.com/seema-kote/')
# Created Date : 12th Sep 2017

import Functions as f

print "Welcome to  Our ATM\n"
print("**** Please Enter credeintials **** \n")

# initilise system
content= f.initialize()
# verify credentials
if(f.verifyCredentials(content)):
    # process Account
    f.process(content)
else:
    print "Enter Valid Username and Password"



