# GroupName in LEB2: c11_wed17
# FileName: c11_wed17_employee.py
# member list in the file
# 005 Jackapong Karapinvong
# 009 Nattaphan Pumipak
# 010 Natthasith Boonheng
# 011 Taiyo Yamamoto
# 028 Phakaphol Dherachaisuphakij

class Employee:
    def __init__(self,eid:int,name:str,salary:float): 
        self._eid = eid
        self._name = name
        self._salary = salary

    def __repr__(self) -> str:
        return f"eid: {self._eid} name: {self._name} salary: {self._salary}"

    def get_eid(self,):
        return self._eid

    def get_name(self):
        return self._name
    
    def set_name(self,new_name:str):
        self._name = new_name

    def get_salary(self):
        return self._salary
    
    def set_salary(self,new_salary:float):
        self._salary = new_salary
    
    def compare(self,another):
        if self._eid < another._eid:
            return -1
        if self._eid == another._eid:
            return 0 
        if self._eid > another._eid:
            return 1

o = Employee(67,"tick",15000)

s = Employee(68,"PK",16000)

k = Employee(69,"Sun",20000)
print(o)
print(s)
print(k)

o.set_name("Mix")
print("tick has been changed to",o.get_name())
print(o)

print(k.compare(s))