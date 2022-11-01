def decorate(method):
    def wrapper(self, other):
        int_dict = {
            'один': 1, '1': 1,
            'два': 2, '2': 2,
            'три': 3, '3': 3,
            'четыре': 4, '4': 4,
            'пять': 5, '5': 5
        }
        if isinstance(other, (int, float)):
            return method(self, other)
        elif isinstance(other, str):
            if other in int_dict:
                x = int_dict[other]
                return method(self, x)
            else:
                raise TypeError('справа от знака "+" непонятный текст. '
                                'Если что, я понимаю текстом цифры с 1 по 5.')
        else:
            return method(self, other)
    return wrapper


class Int(int):

    @decorate
    def __add__(self, other):
        return super().__add__(other)


# использование
x = Int(5)
print(x + '5')  # 10
print(x + 'один')  # 6
print(x + 'пять')  # 10
# print(x + 'шесть')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
# print(x + 'a')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
# print(x + (1,))  # TypeError: unsupported operand type(s) for +: 'Int' and 'tuple'