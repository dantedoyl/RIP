# Здесь должна быть реализация декоратора

def print_result(func_to_decorate):
    def decorated_func(*args, **kwargs):
        print(func_to_decorate.__name__)
        arg = func_to_decorate(*args, **kwargs)
        if(type(arg) == dict):
            for key in arg:
                print('{} = {}'.format(key, arg[key]))
        elif (type(arg) == list):
            for i in arg:
                print('{}'.format(i))
        else:
            print(arg)
        return arg
    return decorated_func


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
