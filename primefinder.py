prime_list = [] # initialize list that contains primes

def isprime(x):
    for number in prime_list: # go through all values in prime_list
        if x % number == 0: # if number is divisible by prime in prime_list, exit
            return False

    return True # if no numbers are divisible, return True


max_search = int(raw_input("Max value? ")) # ask user for max value that program will search for


prime_list.append(2) # start by initializing 2 as prime number
print 2

for i in range(3,max_search + 1):
    if isprime(i):
        prime_list.append(i) # if i is prime, add i to list
        print i # print i if prime
