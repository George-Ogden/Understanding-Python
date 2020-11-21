class Special_Number:
    def __init__(self, number):
        self.number = number
        self.digit_sum = 0
        for digit in list(str(number)):
            self.digit_sum += int(digit)
        # while number > 0:
        #     self.digit_sum += number % 10
        #     number //= 10

    def __str__(self):
        return "Number: {number}\nDigit Sum: {digit_sum}".format(**self.__dict__)

    def __add__(self, another):
        return Special_Number(self.number + another.number)

    def __eq__(self, another):
        return self.digit_sum == another.digit_sum

    def __bool__(self):
        return self.digit_sum != 0
        # return self.number != 0


a = Special_Number(255)
b = Special_Number(256)
c = Special_Number(39)

print(a)
print(a.digit_sum)

print(a + b)

print(a == b)
print(a == c)

print(bool(a))