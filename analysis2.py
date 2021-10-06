import string
import time
import random
import itertools
import copy
import pandas as pd
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
def main():
	guesspasswordlist=list(map(str,readfilewordlistcsv('rockyou.txt')))
	addstr=generatenewpassword()
	print("Your new password: ", ('jack'+addstr))
	#bruteforceinwordlist(guesspasswordlist,('jack'+addstr))

main()