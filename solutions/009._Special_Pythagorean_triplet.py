def prod_triplet_w_sum(n):
    for i in xrange(1, n, 1):
        for j in xrange(1, n-i, 1):
            k = n-i-j
            if i**2 + j**2 == k**2:
                return i*j*k
    return 0
 
print prod_triplet_w_sum(1000)
