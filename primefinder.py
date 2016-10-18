import time
import math

runtime_list = []
max_search = int(raw_input("Max value? ")) # ask user for max value that program will search for

def isprime(x):
    sqrt_x = math.sqrt(x) # find square root of x
    for number in prime_list: # go through all values in prime_list
        if x % number == 0: # if number is divisible by prime in prime_list, exit
            return False
        elif number > sqrt_x:
            return True # if items in list are greater than square root, must be prime

start_time = time.time() # time at start of loop

prime_list = [] # initialize list that contains primes
prime_list.append(2) # start by initializing 2 as prime number
print 2
    

for i in range(3,max_search + 1,2):
    if isprime(i):
        prime_list.append(i) # if i is prime, add i to list
        print i

print 'Runtime: ' + str((time.time() - start_time)) # significantly if not printing results
