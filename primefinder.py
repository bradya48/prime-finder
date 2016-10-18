import sys

prime_list = [2]

def isprime(x):
    for number in prime_list:
        if x % number == 0:
            return False

    return True


max_search = int(raw_input("Max value? "))


prime_list.append(2)
print 2

for i in range(2,max_search):
    if isprime(i):
        prime_list.append(i)
        print i
        
