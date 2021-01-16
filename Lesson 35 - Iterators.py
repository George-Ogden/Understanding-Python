import math


def isPrime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, math.floor(math.sqrt(x))+1, 2):
            if x % i == 0:
                return False
        return True


class PrimeIterator:
    def __iter__(self):
        self.value = 2
        return self
    def __next__(self):
        value = self.value
        if self.value == 2:
            self.value = 3
        else:
            for i in range(self.value+2, self.value*2,2):
                if isPrime(i):
                    self.value = i
                    break

        return value

iterator = iter(PrimeIterator())
print(iterator)
for prime in iterator:
    print(prime)