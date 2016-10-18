import time
import math

#Int variables here:
runtime_list = []
max_search = 1000 #int(raw_input("Max value? ")) # ask user for max value that program will search for
#Functions:

def isprime(x):
    sqrt_x = math.sqrt(x) # find square root of x
    for number in prime_list: # go through all values in prime_list
        if x % number == 0: # if number is divisible by prime in prime_list, exit
            return False
        elif number > sqrt_x:
            return True # if items in list are greater than square root, must be prime



# Lets user know test has started
print "TEST START"



#Iterates through 10,000 times
for i in range(10000):

    start_time = time.time() # time at start of loop
    #Int loop variables

    prime_list = [] # initialize list that contains primes
    prime_list.append(2) # start by initializing 2 as prime number
    
    #code here:

    for i in range(3,max_search + 1,2):
        if isprime(i):
            prime_list.append(i) # if i is prime, add i to list


    #print time.time() - start_time #optional print time per pass
    runtime_list.append(time.time() - start_time)



print '----- Average runtime: ' + str(sum(runtime_list) / (len(runtime_list))) + ' seconds -----'


# Checks whether isprime returns the correct values for 2-100
prime_check = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
prime_list = []

prime_list.append(2)
print 2

for i in range(3,101):
    if isprime(i):
        prime_list.append(i)

if prime_list == prime_check:
    print "TEST SUCCESS"
else:
    print "ERRORS DETECTED"
    
