def f1(str1:str,str2:str):
    if str1 in str2:
        return True
    return False

print(f1("ONE","ONECHAN"))

def f2(oppo:float,adjus:float):
    hypo = oppo**2+adjus**2
    return(hypo**0.5)

print(f2(3,4))

def f3(num:list):
    num = sorted(num)
    secsmall = num[1]
    count=0

    for i in range(len(num)):
        if count>1:
            return None
        if secsmall==num[i]:
            count+=1
    return secsmall

print(f3([20,30,10,19,20]))
# minimum




def f4(num:list,check):
    count = 0
    for i in range(len(num)):
        if check(num[i])==True:
            count+=1
    return count




print(f4([20,3,21,10,10,10],lambda x : x==10))