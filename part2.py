
class Int:
    dict = {
            "один": 1,
            "два": 2,
            "три": 3,
            "четыре": 4,
            "пять": 5,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5
        }

    def __init__(self, value):
      self.value = value

    def __add__(self, other):
        if not isinstance(other, str):
            raise TypeError
        if other not in self.dict:
            raise TypeError(
                "TypeError: справа от знака " + " непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.")
        return self.value + self.dict[other]
    #
    # def make_sum(self, other):



# использование
x = Int(5)
print(x + '5')  # 10
print(x + 'один')  # 6
print(x + 'пять')  # 10
# print(x + 'шесть')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
# print(x + 'a')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
# print(x + (1,))  # TypeError: unsupported operand type(s) for +: 'Int' and 'tuple'