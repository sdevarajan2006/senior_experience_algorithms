#starting chapter 5

#1 Suppose it is known that the running time of one algorithm is O(N log N) and that the running time of another algorithm is O(N^3). What does
#this say about the relative performance of the algorithms?

'''
As the value of n increases, N^3 will increase at a much faster rate than O(N log N), meaning that O(N log N) is a more efficient algorithm
'''

#2 Suppose it is known that the running time of one algorithm is always about N log N and that the running time of another algorithm is O(N^3). What does
# this say about the relative performance of the algorithms?
'''
It is difficult to predict which algorithm will be the most efficient, as o(N^3) is a worst case scenario, while N(log N) is an average run time. However,
I would still assume that N(log N) executes faster, as N^3 is significantly more costly in terms of time
'''

# 3 Suppose it is known that the running time of one algorithm is N log N and that the running time of another algorithm is O(N^3). What does
#this say about the relative performance of the algorithms?
'''
As the value of n increases, N^3 will increase at a much faster rate than O(N log N), meaning that O(N log N) is a more efficient algorithm
'''

# 4 Explain the difference between O(1) and O(2)
'''
O(2) takes double the amount of time as O(1) in a worst case scenario. However, for both notations, the performance of the algorithm doesn't depend
on the size of the input 
'''

# 5 Solve the recurrence
'''
C(N) = C(N/2) + N^2 
suppose that n = 2^(x)
C(2^(x)) = C(2^(x-1)) + (2^(x))^2
         = C(2^(x-2)) + (2^(x-1))^2
         = 1 + 4 + 16 + 64 + ... + (2^(x))^2

We can calculate this sum as a geometric series 
Using the formula (a(1-r^(n)))/(1-r), we can plug in our values and find that the sum is (1(1-4^(x+1)))/(1-4) = (4^(x+1)-1)/3
Now we solve in terms of N, where X = log(2)(N)
So, out final sum is (4^(log(2)(n) + 1) - 1)/3
'''

#6 For what values of N is 10N lgN > 2N^2
'''
never
'''

#7 Write a program to compute the exact value of C(n) in formula 2, s discussed in Chaoter 5. Compare the results to log(n)
def c(n):
    sum = 0
    if n == 0:
        return(1)
    sum += (n - 1 + float(1/n))
    for k in range(1,n+1):
        sum += c(k -1) + c(n - k)
    return sum
for i in range(1,101):
   print(c(i), math.log(i))

#c(n) grows at a much more rapid pace than log(n). C(n) is exponential, while log(n) is logarithmic growth. 

#8 Prove that the precise solution to formula 2 is lg(N) + O(1)

'''
Formula 2: c(n) = c(n/2) + 1, where c(1) = 0

The number of times that the formula will need to be recured is lg(n) because we are dividing by 2 everytime. 
ex. c(8) = c(4) + 1 = c(2) + 1 + 1 = c(1) + 1 + 1 + 1

Since it always goes down to c(1) which is 0, we are counting the number of 1's that add together to arrive at our answer. 
This ends up being lg(n)

'''

#9 Write a recursive program to compute the largest integer less than log(2)(N). 
def n9(n,exp):
    if 2**(exp) > n:
        return(exp - 1)
    return(n9(n, exp + 1))

def test_n9():
         assert n9(17,0) == 4
         assert n9(9,0) == 3
         assert n9(84,0) == 6

#10 Write an iterative program for the problem in the previous exercise. Then write a program that does the computation using Pascal library subroutines. 
#If possible on your computer system. compare the performance of these three programs. (come back to the pascal stuff)

def n10(n):
   exp = 0
   while True: 
      if 2**(exp) > n:
         return(exp - 1)
      exp += 1

def test_n10():
         assert n10(17) == 4
         assert n10(9) == 3
         assert n10(84) == 6



