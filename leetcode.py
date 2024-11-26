

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

no3()