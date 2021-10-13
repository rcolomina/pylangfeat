import random
import time

def get_clock(start_time,p=1000):
    print(f"elapse time from {start_time}")
    return int(p*(time.time()-start_time))

l_times=[]
for size in [10**n for n in [5,6,7,8,9]]:

    print(f"Creating list of size {size}")
    mylist  = list(range(size))
    print("Creating tuple from list")
    mytuple = tuple(mylist)
    
    start_time= time.time()
    print("Sum from list is",sum(mylist))
    time_taken1 = get_clock(start_time)
    print("adding on list",time_taken1,"miliseconds")

    start_time = time.time()
    print("Sum from tupe is",sum(mytuple))
    time_taken2 = get_clock(start_time)
    print("adding on tuple",time_taken2,"miliseconds")
    
    l_times.append((time_taken1,time_taken2))



print(l_times)


