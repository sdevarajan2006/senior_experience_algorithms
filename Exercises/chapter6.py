#Implementation of algorithms

#1 How long does it take to count to 100,000? Estimate how long the program j:=0; from i:=1 to 100000do j := j+ 1 should take on your programming 
#environment, then run the program to test your estimate 
def count_to_100k():
    j = 0
    for i in range (1,100001):
        j = j + 1
    return(j)
  
#Estimate: ~2 seconds 
#It took less than a second- nearly immediate

#2 Answer the previous question using repeat and while
# There isn't a 'repeat' in Python so I will do while 

def count_to_100k_while():
    i = 1
    j = 0
    while i < 100001:
        j += 1
        i += 1
    return(j)
#This function also ran nearly immediately- from 100,000 iterations, it is hard to say which is more efficient. 

#3 
#By running on small values, estimate how long it would take the sieve of Eratosthenes implementation in Chapter 3 to run with n = 1,000,000
def erat(n):
    dict = {key: True for key in range(1, n+1)}
    dict[1] = False
    for i in range(2, n + 1):
        j = 2 
        if dict[i]:
            while (i * j) <= n:
                dict[i * j] = False
                j += 1
    primes = [key for key, value in dict.items() if value is True]
    return(primes)

#Estimation - ~2 seconds 
#This took about 2 seconds. 10,000,000 took about 13-15 seconds 

#4
def erat_optimized(n):
    dict = {key: True for key in range(1, n+1)}
    dict[1] = False
    for i in range(2, n + 1):
        j = 2 
        if dict[i]:
            while (i * j) <= n:
                dict[i * j] = False
                j += 1
        for key in range(i*2, 0, -1):
            if dict[key]:
                print(key)
                break
