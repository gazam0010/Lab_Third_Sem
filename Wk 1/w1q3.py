def isPrime(n):
    if n <= 1:
        return False
    if (n % 2 == 0) or (n % 3 == 0):
        return False
    for i in range(5, n, 2):
        if(n % i == 0):
            return False
    return True

for i in range(1, ran):
    if isPrime(i):
        print(i, end = " ")