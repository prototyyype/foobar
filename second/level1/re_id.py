import math
def prime(num):
    if (num % 2 == 0) and (num > 2):
        return False
    return all(num % i for i in range(3, int(math.sqrt(num)) + 1, 2))

primes = ''

for i in range(2,21000):
    if len(primes) < 10005:
        if prime(i):
            primes = primes + str(i)
    else:
        break

def solution(num):
    reid = primes[num:num+5:1]
    return(reid)
