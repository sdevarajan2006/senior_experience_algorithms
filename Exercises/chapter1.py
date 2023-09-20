# 1. Implement the classical version of Euclids algorithm as described in the text.
def euclid(u, v):
  if u > v:
    b = u
    s = v
  else:
    b = v
    s = u
  if ((b % s) == 0):
    return (s)
  else:
    return (euclid(s, b % s))


# 2. Check what values your pascal system computes for u mod v
# when u and v are not necessarily positive.
# 7 % 4 = 3
# -7 % 4 = 1
# 7 % -4 = -1
# -7 % -4 = -3


# 3. Implement and procedure to reduce a given fraction to lowest terms, using a type fraction = record numerator  denominator: integer end.
def frac(x, y):
  gcf = euclid(x, y)
  return ((int(x / gcf), int(y / gcf)))


#4. Write a function convert: integer that reads a decimal number one # character(digit) at a time, terminated by a blank, and returns the  # value of that number.
def convert(n):
  sum = 0
  counter = 0
  while n != 0:
    sum += ((2**counter) * (n % 10))
    n = n // 10
    counter += 1
  return (sum)


#5. Write a function procedure binary (x: integer) that prints out the inary equivalent of a number.


def bin(x):
  s = ""
  quot = x
  while quot > 1:
    rem = quot % 2
    quot = quot // 2
    s = str(rem) + s
  s = "1" + s
  return (s)


#6. Give all the values that u and v take on when gcd is invoked with the intial call gcd(12345, 56789)
def gcf(u, v):
  if u > v:
    b = u
    s = v
  else:
    b = v
    s = u
  if ((b % s) == 0):
    return (s)
  else:
    print(s, b % s)
    return (gcf(s, b % s))


#7. Exactly how many pascal statements are executed for the call in the pervous exercise.
# 28


# 8. Write a program to compute the greatest common divisor of 3 numbers, u, v, and w
def n8(u, v, w):
  gcf1 = euclid(u, v)
  gcf2 = euclid(gcf1, w)
  return (gcf2)


#9 Find the largest pair of numbers representable as integers in your pascal system whose greatest common divisor is 1
# lets say that the largest number was 2*10000


def lpn():
  maxn = 2**10000
  gcf = 5
  while gcf != 1:
    gcf = euclid(maxn, maxn - 1)
    maxn -= 1
  print((maxn, maxn - 1))


#10
'''INPUT "Enter the First Number: " U
INPUT "Enter the Second Number: " V
IF U > V THEN
  B = U
  S = V
ELSE
  B = V
  S = U
END IF

IF (B MOD S = 0) THEN
  PRINT "The GCF is : "; S
  END
ELSE
  GOSUB 20 
END IF

END

REM Euclid's Algorithm
T = S
S = B MOD S
B = T
RETURN
  '''
