import random
import math
import sys

def primes(n):
    sieve = [True] * (n+1)
    primes = []
    for x in range(2, n+1):
        if sieve[x]:
            primes.append(x)
            for y in range(x*x, n+1, x):
                sieve[y] = False
    return primes

def builder_test(prime, bit):
    max_index = 0
    max_pow = 1
    while prime[max_index] < 2**(bit-1) and max_index < len(prime):
        max_index += 1
    while 2**max_pow < 2**(bit-1):
        max_pow += 1

    m = 1
    q = []
    while True:
        num = random.randint(0, max_index)
        power = random.randint(1, max_pow)
        if m * prime[num]**power < 2**(bit-2):
            m *= prime[num]**power
            q.append(prime[num])
        if m > 2**(bit-2):
            if m >= 2**(bit-1):
                m = 1
                q = []
            else:
                break
    n = 2*m + 1
    return n, q

def test_millera(n, t, q):
    a = []
    while len(a) != t:
        aj = random.randint(2, n-1)
        if aj not in a:
            a.append(aj)
    for aj in a:
        if pow(aj, n-1, n) != 1:
            return 0
            break
    flag = True
    i = 0
    for aj in a:
        if q[i] != 0 and pow(aj, (n-1)//q[i], n) != 1:
            flag = False
            if i < len(q):
                i += 1
    if flag:
        return 0
    return 1

def print_results(res, res_ver_test, otvegnutie):
    print("Prime Numbers\tTest Results\tOccurrences")
    print("----------------------------------------------")
    for i in range(len(res)):
        print(f"{res[i]}\t\t{res_ver_test[i]}\t\t{otvegnutie[i]}")

size_primes = 500
prime = primes(size_primes)
bit = int(input())

res = []
res_ver_test = []
otvegnutie = []
k = 0

while len(res) != 10:
    n, q = builder_test(prime, bit)
    probability = test_millera(n, 10, q)
    if probability == 1:
        if n not in res:
            res.append(n)
            probability = test_millera(n, 1, q)
            if probability == 1:
                res_ver_test.append("+")
            else:
                res_ver_test.append("-")
            otvegnutie.append(k)
            k = 0
        else:
            k += 1

print_results(res, res_ver_test, otvegnutie)
