import string
import time
import random
import itertools
import copy

def tupletostring(tuple):
    string =  ''.join(tuple)
    return string

def bruteforce(userpasswordinit,userpasswordafter):
    starttimecrack=time.time()
    count=0
    for possiblesequence in itertools.product(string.printable,repeat=(len(userpasswordafter)-len(userpasswordinit))):
        count+=1
        password_copy=userpasswordinit[:]
        password_copy+=tupletostring(possiblesequence)
        print(password_copy)
        if (password_copy==userpasswordafter):
            print("Password is cracked!")
            print(count)
            return (time.time()-starttimecrack)

def main():
	"""timefor5=bruteforce('','5')
	timeforj=bruteforce('','j')
	timeforJ=bruteforce('','J')
	timeformoneysign=bruteforce('','$')
	timeforpt =bruteforce('','%')"""
	timeex=bruteforce('','5mM@')
	"""timefor5j=bruteforce('','5j')
	timefor5J=bruteforce('','5J')
	timefor5ms=bruteforce('','5$')
	print("Time for 5: ",timefor5)
	print("Time for j: ",timeforj)
	print("Time for J: ",timeforJ)
	print("Time for $: ",timeformoneysign)
	print("Time for %: ",timeforpt)"""
	print("Time for pass: ",timeex)
	"""print("Time for 5j: ",timefor5j)
	print("Time for 5J: ",timefor5J)
	print("Time for 5$: ",timefor5ms)"""


main()
