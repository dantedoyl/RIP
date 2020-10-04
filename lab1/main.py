import math
import sys
print("Торжков Максим ИУ5-51Б")
while True:
    if (len (sys.argv) == 1) or (len (sys.argv) == 0):
        print("Введите коэффициенты для уравнения")
        print("ax^4 + bx^2 + c = 0:")
        while True:
            try:
                a = float(input("a = "))
            except ValueError:
                print("Некорекктные данные. Введите повторно:")
                continue
            else:
                break
        while True:
            try:
                b = float(input("b = "))
            except ValueError:
                print("Некорекктные данные. Введите повторно:")
                continue
            else:
                break
        while True:
            try:
                c = float(input("c = "))
            except ValueError:
                print("Некорекктные данные. Введите повторно:")
                continue
            else:
                break
            
    elif len (sys.argv) == 4:
        try:
            a = float(sys.argv[1])
        except ValueError:
            print("Некорекктные данные. Введите повторно:")
            a = float(input("a = "))
        try:
            b = float(sys.argv[2])
        except ValueError:
            print("Некорекктные данные. Введите повторно:")
            b = float(input("b = "))
        try:
            c = float(sys.argv[3])
        except ValueError:
            print("Некорекктные данные. Введите повторно:")
            c = float(input("c = "))
        sys.argv.clear()

    else:
        print('Некоректный ввод коэффициентов.')
        sys.argv.clear()
        continue

    discr = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % discr)
    if (a == 0) and (b == 0) and (c == 0):
        print("Корень уравнения - любое число.\n")
    elif (c != 0) and (b == 0) and (a == 0):
        print("Нет решений\n")

    elif (b!= 0) and (a == 0):
        x = -c / b
        if x < 0:
            print("Уравнение не имеет рациональных корней.\n")
        elif x == 0:
            print("Корни уравнения:\n0")
        else:
            print("Корни уравнения:\n", math.sqrt(x), -math.sqrt(x))
    else:
        if discr < 0:
            print("Дискрименант меньше нуля. Уравнение не имеет рациональных корней.\n")
        else:
            x = ((-1 * b) - math.sqrt(discr)) / (2 * a)
            y = ((-1 * b) + math.sqrt(discr)) / (2 * a)
            if (x < 0) and (y < 0):
                print("Уравнение не имеет рациональных корней.\n")
            else:
                print("Корни уравнения: ")
                if x > 0:
                    x_1 = math.sqrt(x)
                    x_2 = -1 * x_1
                    print(x_1, x_2)
                elif x == 0:
                    print(x)
                if (y > 0) and (x != y):
                    y_1 = math.sqrt(y)
                    y_2 = -1 * y_1
                    print(y_1, y_2)
                elif (y == 0) and (x != y):
                    print(y)    
