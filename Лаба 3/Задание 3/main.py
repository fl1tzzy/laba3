import math

apox_vector = []

def korrel(temperatures, mean_y, t, time_limit):
    sum_xy = 0
    sum_x2 = 0
    sum_y2 = 0
    mean_x = (time_limit - 1) / 2.0
    for i in range(t + 1):
        sum_xy += (i - mean_x) * (temperatures[i] - mean_y)
        sum_x2 += (i - mean_x) * (i - mean_x)
        sum_y2 += (temperatures[i] - mean_y) * (temperatures[i] - mean_y)
    return sum_xy / math.sqrt(sum_x2 * sum_y2)

def aprox(x_vector, y_vector):
    sum_x = sum(x_vector)
    sum_y = sum(y_vector)
    sum_xy = sum(x * y for x, y in zip(x_vector, y_vector))
    sum_x2 = sum(x ** 2 for x in x_vector)
    n = len(x_vector)

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    b = (sum_y - a * sum_x) / n

    return a, b

def coffee(T, Ts, r, time_limit):
    temperatures = []
    times = []
    temp_corr = []

    for t in range(time_limit + 1):
        temperature = Ts + (T - Ts) * math.exp(-r * t)
        temperatures.append(temperature)
        times.append(t)

    a, b = aprox(times, temperatures)
    apox_vector.extend([a, b])

    mean_y = sum(temperatures) / len(temperatures)
    for t in range(time_limit + 1):
        corr = korrel(temperatures, mean_y, t, time_limit)
        temp_corr.append((temperatures[t], corr))

    return temp_corr

def main():
    print("Введите начальную температуру кофе: ")
    T = float(input())
    print("Введите температуру окружающей среды: ")
    Ts = float(input())
    print("Введите коэффициент остывания: ")
    r = float(input())
    print("Введите итоговое время: ")
    time_limit = int(input())

    results = coffee(T, Ts, r, time_limit)

    print(f"Коэффициенты аппроксимирующей прямой a - {apox_vector[0]}, b - {apox_vector[1]}")
    print("+------+------------+---------------+")
    print("| Время| Температура| Коэф.кореляции|")
    print("+------+------------+---------------+")

    for t, result in enumerate(results):
        print(f"|  {t:6}| {round(result[0], 2):10}| {round(result[1], 2):13}|")
        print("+------+------------+---------------+")

if __name__ == "__main__":
    main()
