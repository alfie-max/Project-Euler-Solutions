from math import sqrt

count = 0
n = 1
while count < 10001:
    n = n+1
    prime = True
    if n%2 == 0 and n > 2:
        prime = False
    else:
        for i in xrange(3, int(sqrt(n))+1, 2):
            if n%i == 0:
                prime = False
                break
    if prime:
        count += 1

print "{0}'st Prime number is : {1}".format(count, n)
