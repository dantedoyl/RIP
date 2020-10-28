import json
import sys
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.unique import Unique
from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
# Сделаем другие необходимые импорты

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

path = "data_light.json"
with open(path, encoding='utf-8') as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return list(Unique(sorted(field(arg,'job-name'), key=str), ignore_case=True))
        #raise NotImplemented


@print_result
def f2(arg):
    return list(filter(lambda x: 'программист' in x, arg))
    #raise NotImplemented


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))
    #raise NotImplemented


@print_result
def f4(arg):
    return list(map(lambda x: x + ", зарплата " + str(*gen_random(1, 100000, 200000)) + " руб", arg))
    #raise NotImplemented


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))