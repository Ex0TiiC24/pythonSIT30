


def double(i:int)-> int:
    return i*2

print(double(23))


f:callable[[int],int] = double

print(f(22))