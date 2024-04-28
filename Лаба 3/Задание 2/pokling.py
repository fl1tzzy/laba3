import random
import math

def resheto(n):
    all_numbers = list(range(2, n + 1))
    primes = []
    while all_numbers:
        current_prime = all_numbers[0]
        primes.append(current_prime)
        all_numbers = [x for x in all_numbers if x % current_prime != 0]
    return primes

def rn(a, n):
    return random.randint(a, n)

def test_pokling(n, delit, t):
    a = []
    while len(a) != t:
        ai = rn(2, n - 1)
        if ai not in a:
            a.append(ai)
    for ai in a:
        res = ai % n
        for _ in range(2, n):
            res = res * ai
            res = res % n
        if res != 1:
            return " - составное число", 0
    n32 = n - 1
    for j in a:
        for d in delit:
            prom = n32 // d
            res2 = j % n
            for _ in range(2, prom + 1):
                res2 = res2 * j
                res2 = res2 % n
            if res2 == 1:
                break
        else:
            return " - простое число", 1
    return " - вероятно, составное число", 0

def build_pokling(bit, c, t):
    glim = 0
    while True:
        z = 1
        f = True
        geted = []
        delit = []
        while f and len(geted) < 1:
            z = 1
            delitt = []
            for i in range(len(c)):
                if c[i] > pow(2, bit // 2 + 1) - 1:
                    break
                max_val = int(math.log(pow(2, bit // 2 + 1), c[i]))
                rpow = rn(1, max_val)
                rnum = rn(0, rpow + 1)
                z *= pow(c[i], rnum)
                if z > pow(2, bit // 2):
                    z //= pow(c[i], rnum)
                    if z >= pow(2, bit // 2):
                        if z not in geted:
                            geted.append(z)
                        z = 1
                        f = False
                        delit = delitt[:]
                else:
                    if rnum:
                        delitt.append(c[i])
        n = rn(pow(2, bit // 2 - 1), pow(2, bit // 2) - 1) * geted[0] + 1
        resultat = test_pokling(n, delit, t)
        oleg = ''
        if resultat[1] == 1:
            res = test_pokling(n, c, 1)
            if res[1] == 1:
                oleg = '+'
            else:
                oleg = '-'
        else:
            res = test_pokling(n, c, 1)
            if res[1] == 1:
                glim += 1
        if resultat[1] == 1:
            return oleg, n, glim

def main():
    bit = int(input("Введите количество бит: "))
    c = resheto(500)
    pokling_res = []
    pokling_res_p = []
    test_pokling(13, [2], 10)
    while len(pokling_res_p) != 10:
        pokling_result = build_pokling(bit, c, 10)
        p = pokling_result[1]
        if p not in pokling_res_p:
            pokling_res_p.append(p)
            pokling_res.append(pokling_result)
    print("+", end="")
    for _ in range(10):
        print("--------+", end="")
    print("\n|", end="")
    for i in range(10):
        print(f"{i + 1:8}|", end="")
    print("\n+", end="")
    for _ in range(10):
        print("--------+", end="")
    print("\n|", end="")
    for i in range(10):
        print(f"{pokling_res[i][1]:8}|", end="")
    print("\n+", end="")
    for _ in range(10):
        print("--------+", end="")
    print("\n|", end="")
    for i in range(10):
        print(f"       {pokling_res[i][0]}|", end="")
    print("\n+", end="")
    for _ in range(10):
        print("--------+", end="")
    print("\n|", end="")
    for i in range(10):
        print(f"{pokling_res[i][2]:8}|", end="")
    print("\n+", end="")
    for _ in range(10):
        print("--------+", end="")
    print()

if __name__ == "__main__":
    main()
