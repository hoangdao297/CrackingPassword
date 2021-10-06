import pandas as pd
import string
import time
import random
import itertools
import copy 

#start_time = time.time()
def inputpassword():
    print("Enter your password: ")
    userpass=input()
    return userpass

def readfilewordlistcsv(file):
    print("\nProcessing...\n")
    df = pd.read_csv(file,delimiter = "\n", header = None, names = ["Passwords"],encoding = "ISO-8859-1")
    return df['Passwords'].values.tolist()
  
def bruteforceinwordlist(guesspasswordlist, actual_password):
    starttimelist=time.time()
    for guess_password in guesspasswordlist:
        print(guess_password)
        if guess_password == actual_password:
            print("\nYour password is in the wordlist, it will need to be changed")
            print("Time to check your password in wordlist: ",(time.time()-starttimelist))
            return 1
    return 0

def generatenewpassword():
    alphabetlist_lower=list(string.ascii_lowercase)
    alphabetlist_upper=list(string.ascii_uppercase)
    specialcharacter=list(string.punctuation)
    number=[0,1,2,3,4,5,6,7,8,9]
    n=int(input("Enter the number of words you want your password to be added: "))
    addstr=''
    for i in range(0,n):
        randlist=random.randrange(0,4)
        if (randlist==0):
            randelement=random.randrange(0,len(alphabetlist_lower))
            addstr+=alphabetlist_lower[randelement]
        elif (randlist==1):
            randelement=random.randrange(0,len(alphabetlist_upper))
            addstr+=alphabetlist_upper[randelement]
        elif (randlist==2):
            randelement=random.randrange(0,len(specialcharacter))
            addstr+=specialcharacter[randelement]
        else:
            randelement=random.randrange(0,len(number))
            addstr+=str(number[randelement])
    return addstr
    
def tupletostring(tuple):
    string =  ''.join(tuple)
    return string

def bruteforce(init,userpasswordafter):
    starttimecrack=time.time()
    for possiblesequence in itertools.product(string.printable,repeat=(len(userpasswordafter)-len(init))):
        password_copy=init[:]
        password_copy+=tupletostring(possiblesequence)
        print(password_copy)
        if (password_copy==userpasswordafter):
            print("Password is cracked!")
            return (time.time()-starttimecrack)

def comparetimeexecution(password,addpassword):
	oldpass_time=bruteforce('',password)
	newpass_time=bruteforce('',password+addpassword)
	print("Time to crack old password: ",oldpass_time)
	print("Time to crack new password: ",newpass_time)

def main():
	actual_password=inputpassword()
	guesspasswordlist=list(map(str,readfilewordlistcsv('rockyou.txt')))
	print("Check your password in the wordlist: ")
	presence=bruteforceinwordlist(guesspasswordlist,actual_password)
	if (presence==1):
		addinpassword=generatenewpassword()
		comparetimeexecution(actual_password,addinpassword)
		print("Your new password: ",(actual_password+addinpassword))
	else:
		print("Your password is not in the wordlist")
		print("Do you want to add more character into your password to check ? (yes/no)")
		ans=input()
		if (ans=="YES" or ans=="yes"):
			addinpassword=generatenewpassword()
			comparetimeexecution(actual_password,addinpassword)
			print("Your new password: ",(actual_password+addinpassword))
		else:
			exit()

main()

