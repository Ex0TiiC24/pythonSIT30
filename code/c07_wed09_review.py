# c07 Review 2024-09-25 Group Wed No.09
# 005 Jackapong Karapinwong
# 009 Nattaphan Phoomiphak
# 010 Natthasith Boonheng
# 011 Taiyo yamamoto
# 028 Phakaphol Dherachaisuphaki

def km_to_miles(km):
    if not isinstance(km,(int,float)):
        raise TypeError("Only int or float")
    if (km<0):
        raise ValueError("Only non negative number")
    miles=km*0.62137119
    return miles

def testkm():
    try:
        km_to_miles("-3")
        print("km_to_miles failed")
    except TypeError:
        print("km_to_miles pass1")
    except:
        print("km_to_miles failed1")
    try:
        km_to_miles(-3)
    except ValueError:
        print("km_to_miles pass2")
    except:
        print("km_to_miles failed2")

def consecutive(msg):
    i=0
    if not isinstance(msg,str):
        raise TypeError("Only String")

    for i in range(len(msg)-1):
        if msg[i] == msg[i + 1]:
            return(True)
        else:
           i+=1
    return(False)
def testconsec():
    try:
        consecutive(12)
        print("consecutive failed")
    except TypeError:
        print("consecutive pass")
    except:
        print("concescutive failed")



def duplicate(msg):
    i = 0
    if not isinstance(msg, str):
        raise TypeError("Only String")
    while (i < len(msg) - 1):
        k=i+1
        while(k<len(msg)): #always start on [1] so -1 ไม่จำเป็น
            if msg[i]==msg[k]:
                return(True)
            k+=1
        i+=1
    return (False)
def testdup():
    try:
        duplicate(12)
        print("duplicate failed")
    except TypeError:
        print("duplicate pass")
    except:
        print("duplicate failed")




def max_value(x,y,z):
    if not (isinstance(x, int) and isinstance(y,int) and isinstance(z,int)):
        raise TypeError("Only int")
    #check x y
    if (x>=y):
        fmax=x
    else:
        fmax=y
    #compare (check x y) with z
    if fmax>=z:
        return(fmax)
    else:
        return(z)
    
def testmax():
    try:
        max_value("2",0.1,2)
        print("max_value failed")
    except TypeError:
        print("max_value pass")
    except:
        print("max_value failed")

def main():
    
    testkm()
    testconsec()
    testdup()
    testmax()

main()