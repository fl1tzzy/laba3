import math

def main():
    print("+----------+----------+")
    print("|         x|         y|")
    print("+----------+----------+")

    toch = 10000.0
    delta = 0.5

    cont = []

    for x in [round(x * toch) / toch for x in [i * delta for i in range(int(-9 / delta), int(5 / delta) + 1)]]:
        y = 0.0
        if x <= -5:
            y = 0.5 * x ** 2 + 7 * x + 24.5
        elif x <= -4:
            y = 2
        elif x <= 0:
            y = -0.5 * x
        elif x <= 3.14:
            y = math.sin(x / 3.14 * math.pi)
        elif x <= 5:
            y = x - math.pi
        y = round(y * toch) / toch
        cont.append((x, y))

    for point in cont:
        print("|%10.4f|%10.4f|" % point)
        print("+----------+----------+")

if __name__ == "__main__":
    main()
