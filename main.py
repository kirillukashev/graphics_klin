import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

INF = 1e18
cnt = 0
def paint():
    global parabola_x, parabola_y
    global x_val, y_val
    global height
    global lines
    # Создаем график
    plt.figure(figsize=(10, 10))

    # Рисуем параболу
    plt.plot(parabola_x, parabola_y, label='y = a * x^2')

    #Рисуем горизонтальную линию
    plt.axhline(y=height, color='r', linestyle='--')

    # Рисуем отрезки
    for line in lines:
        plt.plot([line[0], line[1]], [line[2], line[3]], marker='o')

    # Настройка осей
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.xlim(0, x_val)
    plt.ylim(0, y_val)

    # Добавляем подписи и заголовок
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Движения луча')
    plt.legend()
    plt.grid(True)
    plt.show()

def get_k_lakmus(x1, y1, x2, y2):
    if y1 > y2:
        return y1 / x1
    else:
        return y2 / x2

x_val, y_val = map(float, input('Укажите пределы осей Ox и Oy:\n').split())

a, height = map(float, input('Введите параметр a и height, где y = a * x^2\n').split())

parabola_x = np.linspace(0, 10, 400)
parabola_y = a * (parabola_x**2)

x1, y1, x2, y2 = map(float, input('Введите координаты луча в формате: x1 y1 x2 y2\n').split())
lines = []

lines.append([x1, x2, y1, y2])
paint()

x1, x2, y1, y2 = lines[-1][0], lines[-1][1], lines[-1][2], lines[-1][3]
position = -1 # 1 - parabola, 0 - vertical line

if abs(x1 - x2) < 0.0001:
    new_x, new_y = x2, a * (x2 ** 2)
    k = INF
else:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1

    k_lakmus = get_k_lakmus(x1, y1, x2, y2)

    tg_angle = (k - k_lakmus) / (1 + k * k_lakmus)
    if tg_angle <= 0:
        position = 0
        new_x, new_y = 0, b
    else:
        position = 1
        new_x = (k + sqrt(k * k + 4 * a * b)) / (2 * a)
        new_y = a * (new_x ** 2)

lines.append([x2, new_x, y2, new_y])
flag = input("Нажмите Enter")
paint()
cnt += 1

check_flag = 0

if k == INF:
    new_x = 0
    new_y = 1 / (4 * a)
    x1, x2, y1, y2 = lines[-1][0], lines[-1][1], lines[-1][2], lines[-1][3]
    lines.append([x2, new_x, y2, new_y])
    flag = input("Нажмите Enter")
    paint()
    cnt += 1

    position = 0

    x1, x2, y1, y2 = lines[-1][0], lines[-1][1], lines[-1][2], lines[-1][3]
    k = (1 - 4 * (x1**2) * (a**2)) / (4 * x1 * a)
    b = 1 / (4 * a)

    check_flag = 1

while max(lines[-1][2], lines[-1][3]) <= height:
    flag = input("Нажмите Enter")
    x1, x2, y1, y2 = lines[-1][0], lines[-1][1], lines[-1][2], lines[-1][3]
    if position == 1: #now on parabola
        if (1 - 4 * (x2**2) + 4 * x2 * k) == 0 or  (4 * k * sqrt(y2) - 4 * y2 + 1) == 0: #line road to up
            lines.append([x2, x2, y2, height])
            paint()
            break
        new_k = (4 * x2 - k + 4 * (x2**2) * k) / (1 - 4 * (x2**2) + 4 * x2 * k)
        new_b = (k * sqrt(y2) - 4 * (y2**2) - 3 * y2) / (4 * k * sqrt(y2) - 4 * y2 + 1)
        k = new_k
        b = new_b

        k_lakmus = get_k_lakmus(x2, y2, x2, y2)

        tg_angle = (k - k_lakmus) / (1 + k * k_lakmus)
        if k <= 0:
            position = 0
            new_x, new_y = 0, b
        elif tg_angle <= 0:
            position = 0
            new_x, new_y = 0, b
        else:
            position = 1
            new_x = (k + sqrt(k * k + 4 * a * b)) / (2 * a)
            new_y = a * (new_x ** 2)
    else: #now on line
        if check_flag == 1:
            check_flag = 0
        else:
            new_k = -k
            new_b = b
            k = new_k
            b = new_b

        position = 1
        new_x = (k + sqrt(k * k + 4 * a * b)) / (2 * a)
        new_y = a * (new_x ** 2)
    lines.append([x2, new_x, y2, new_y])
    paint()
    cnt += 1
print("Количество отражений:", cnt)
