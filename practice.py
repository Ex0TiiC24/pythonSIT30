import functools

def pyramid():
    for i in range(6):
        for k in range(i):
            print("*",end=" ")
        print("\n")


def power(x,n):
    num = 1
    for i in range(n):
        num = num*x
    return num


def powerr(x,n):
    if n==0:
        return 1
    return x*power(x,n-1)

def fac(x):
    if x ==0:
        return 1
    
    return x*fac(x-1)

def palindrome(kum:str):
    
    kum = list(kum)
    if len(kum)==1 or len(kum)==0:
        return True
    if kum[0] == kum[-1]:
        kum.pop(0)
        kum.pop()
        return palindrome(kum)
    return False

def func(num:list):
    return functools.reduce(lambda x,y: x+y,num)

def hello()->any:
    return "hello"



print(func([2,3,4,5]))