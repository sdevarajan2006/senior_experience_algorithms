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



