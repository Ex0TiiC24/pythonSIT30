class Employee:
    def __init__(self,eid,name,salary) -> None:
        self._eid = eid
        self._name = name
        self._salary = salary
    def get_eid(self):
        return self._eid
    def get_name(self):
        return self._name
    def get_salary(self):
        return self._salary
    def set_eid(self,new_eid):
        self._eid = new_eid
    def set_name(self,new_name):
        self._name = new_name
    def set_salary(self,new_salary):
        self._salary = new_salary
    def __repe__(self):
        return f"Employee(eid={self._eid}, name={self._name}, salary={self._salary})"


siam = Employee(1,"Siam",670000000)
olarn = Employee(2,"Olarn",20)
lol = Employee(3,"kok",1000)
banana = Employee(4,"Kluay",200)
pop = Employee(5,"opoi",1600)
peep = Employee(6,"peep",12345)

all = [siam,olarn,lol,banana,pop,peep]


def salary(employee):
    return employee.get_salary() > 1000

def name(employee):
    return employee.get_name()

def average(employees):
    return 

filtered_employees = filter(salary, all)

print(list(filtered_employees))

mapped_employees = map(name,all)
print(list(mapped_employees))

print("sad")