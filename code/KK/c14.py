class Person:
    _exist: dict = {}
    count = 1

    def __init__(self,name,height,weight) -> None:
        #if pid in Person._exist or height <= 0 or weight <= 0:
        #    raise ValueError("Invalid")
        self._pid = Person.count 
        Person.count+=1
        self._name = name
        self._weight = weight
        self._height = height
        Person._exist[self._pid] = self._name
    
    def __repr__(self) -> str:
        return (f"pid:{self.pid} Name:{self.name} Weight:{self._height} Height:{self._weight}")

    @property
    def name(self):
        return self._name
    @property
    def pid(self):
        return self._pid
    @property
    def weight(self):
        return self._weight
    
    def pidadd(self,amount):
        if amount <0 :
            raise ValueError("Invalid")
        self._pid += amount
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    
lol = Person("Awa",175,70)
pop = Person("Aw",175,70)


print("\n")

print(lol)
print(pop)


class PersonGroup:

    instance = []

    class GroupWalk:
        def __init__(self,values) -> None:
            self.values = values
            self._key = list(values.key())
            self._current = 0

        def __iter__(self):
            return self
        def __next__(self):
            if self._current >= len(self.values):
                raise StopIteration
            result = self.values[self._current]
            self._current += 1
            return result
            
    def __init__(self) -> None:
        self._group = {}
        PersonGroup.instance.append(self)
    
    def add(self,person):
        self._group[person.pid] = person.name

    def __repr__(self):
        return str(self._group)
   
    


one = PersonGroup()
one.add(lol)
one.add(pop)


print("\n",one)

