num = 600851475143

i = 2

while i*i < num:
    while num%i == 0:
        num = num / i
    i = i+1 if i == 2 else i+2

print num
