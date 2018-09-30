# Author name : Kote Seema M ('https://github.com/seema-kote/')
# Created Date : 12th Sep 2017

import getpass
def initialize():
    # read info file
    with open("info.txt", 'r') as file:
        #read user information
        content = file.readlines()
        for item in content:
            # Replace \n from each line with empty string
            content[content.index(item)]=item.replace("\n",'')
    return content

def process(data):
    # Show ATM menu
    input = raw_input("\n1. Withdrwal\t2.Change PIN\t3.Balance Enquiry\t4.Exit\n")
    if (input.isdigit()):
        # Withdrawal Choice
        if input=='1':
           withdraw(data)
        # Change Pin Choice
        elif input=='2':
            changePin(data)
        # Balance Enquiry Choice
        elif input=='3':
            balanceEnquiry(data)
        # Exit From menu
        elif input=='4':
            exit()
        process(data)
    else:
        print "Please enter correct choice..."

def verifyCredentials(data):
    # get username and password
    uname = raw_input("User Name:")
    password = getpass.getpass(prompt='Password: ', stream=None)
    # verify user and password
    if (data[0] == uname and data[1] == password):
        return True
    else:
        return False

def writeDetails(data):
    # write details
    file = open("info.txt", 'w')
    for item in data:
        file.write(str(item)+'\n')
    file.close()

def withdraw(data):
    # get withdraw amount from user
    withdrawAmount = int(raw_input("Enter Amount: "))
    if (withdrawAmount < data[2]):
        # enough money ..let him withdraw
        data[2] = int(data[2]) - withdrawAmount
        # Print Balance
        print "Transaction complete.Your current balance is : Rs." + str(data[2]) + " .Thank you !"
        writeDetails(data)
    else:
        print "You do not have enough money."

def changePin(data):
    # get password from user
    cpassward=raw_input("Enter current Passward: ")
    # verify current password
    if cpassward==data[1]:
        # get new password
        data[1]=raw_input("Enter New passward: " )
        # update password in info.txt file
        writeDetails(data)
    else:
        print("Sorry... Wrong passward")

def balanceEnquiry(data):
    # print current balance
    print("Your account Balance is Rs.%s "%data[2])
