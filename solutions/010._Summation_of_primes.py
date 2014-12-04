MAX = 2000000
total = 2

def isPrime(i):
    for j in xrange(3, int(i**.5) + 1, 2):
        if i%j == 0:
            return False
    return True

for i in xrange(3, MAX, 2):
    if isPrime(i):
        total += i

print total
