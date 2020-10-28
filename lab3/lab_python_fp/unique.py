# Итератор для удаления дубликатов

from lab_python_fp.gen_random import gen_random
import types

class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        self.index = 0
        self.data = items
        self.used_elements = set()
        for key in kwargs:
            if key == 'ignore_case':
                self.ignore_case = kwargs[key]
            else:
                self.ignore_case = False
        pass

    def __next__(self):
        # Нужно реализовать __next__
        while True:
            if(type(self.data) == types.GeneratorType):
                current = next(self.data)
            else:
                if self.index >= len(self.data):
                    raise StopIteration
                current = self.data[self.index]
                if (type(current) == str and self.ignore_case == True):
                    current = current.lower()
                self.index = self.index + 1
            if current not in self.used_elements:
                 # Добавление в множество производится
                 # с помощью метода add
                self.used_elements.add(current)
                return current
        pass

    def __iter__(self):
        return self

data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
# data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
# data = gen_random(10, 1, 3)
# for i in Unique(data, ignore_case=True):
#     print(i)