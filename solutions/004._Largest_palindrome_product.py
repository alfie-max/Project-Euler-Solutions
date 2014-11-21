largest_pal = 1

for a in xrange(999, 100, -1):
    for b in xrange(a, 100, -1):
        x = a*b
        if str(x) == str(x)[::-1] and x > largest_pal:
            largest_pal = x

print largest_pal
