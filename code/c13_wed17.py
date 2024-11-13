from typing import Callable  # Import Callable from the typing module

def double(i: int) -> int:
    return i * 2

print(double(23))

# Use Callable with a capital 'C' and correct typing
f: Callable[[int], int] = double
print(f(35))


def high(fc:Callable[[int],int],v:int):
    return fc(v)


print(high(f,12))
print(high(double,31))