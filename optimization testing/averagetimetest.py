import time

#Int variables here:


#Functions:



print "START"



#Iterates through 10,000 times
for i in range(10000):

    start_time = time.time() # time at start of loop
    #Int loop variables



    #code here:



    #print time.time() - start_time #optional print time per pass
    runtime_list.append(time.time() - start_time)



print '----- Average runtime: ' + str(sum(runtime_list) / (len(runtime_list))) + ' seconds -----'

    
