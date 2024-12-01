

def no1():
    print("แม่ให้เงินคุณเท่าไหร่")
    todaymoney = int(input())
    moneyalive = todaymoney
    while moneyalive>0:
        item = int(input("ซื้อของราคาเท่าไหร่ -1 เพื่อ go home"))
        if item <0:
            break
        if moneyalive < item:
            print("money mai po mai hai buy")
            print("kon jon")
            
        else:
            moneyalive = moneyalive-item
        print("เหลือเงิน",moneyalive)


    print("วันนี้คุณเริ้มด้วย",todaymoney,"คุณจน",moneyalive)


def no2(): #2.5%
    print("deposit money")
    money = int(input())
    balance = money
    interest = 0.025
    year = 1
    while year<=10:
        currentinterest = balance*interest
        balance += currentinterest
        print(f"yaer {year} Interest is {"%.2f"%currentinterest} you have {"%.2f"%balance}")
        year+=1



def no3():
    starthr = int(input())
    startmn = int(input())
    endhr = int(input())
    endmn = int(input())
    hrminute = (endhr-starthr)*60 + endmn-startmn
    print(hrminute)
    timeofwork = 45

    hrreamin = hrminute//60
    mnremain = hrminute%60
    print(hrreamin,"Hour",mnremain,"minutes")


    work = hrminute//timeofwork
    print(work)

def prime():
    num = int(input("Check is this number prime? "))
    if num==1 or num==0:
        print("prime")
        return
    state = True
    for i in range(2,num):
        
        if num%i==0:
            state=False
            break
        else:
            state=True
            
    if state==True:
        print("Prime")
    if state==False:
        print("not prime")


def allprime():
    n = int(input())
    if n>=2:
        print(2)
    for i in range(n):
        for k in range(2,i):
            if i%k ==0:
                break
            else:
                print(i)
                break
        

                

        



def mae():
    maxx = 12
    for mae in range(2,25):
        i=1
        k=1
        num=0
            
        print("mae",mae)
        while i<=maxx:
            
            while k <= i:
                num=num+mae
                print(f"{mae} * {k} = ",num)
                k+=1
            i+=1
    

def yok():
    i=1
    k=1
    num=1
    a= int(input("A"))
    b= int(input("B"))
    
    
    while k <=  b:
        num=a*num
        print(f"{a} power of {k} is ",num)
        k+=1

def log():
    count=0
    a= int(input("log: "))
    b = int(input("base: "))
    
    
    while a>1:
        a = a/b
        count+=1
    print(count)




def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-2)+fib(n-1)
    
log()