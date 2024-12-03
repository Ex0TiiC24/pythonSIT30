"""
INT140 Problem and Solution for Final Exam Preparation
Part II - Functional - consists of 10 problems
"""

from functools import reduce

""" ===============================================================
Problem_01: Write a function 'func01' that receives a list of integers.
This function counts the number of even numbers in the list.
(ฟังก์ชันนี้ นับจำนวนเลขคู่ ที่มีอยู่ในลิสต์)
Even numbers are the number that is divisible by 2. (even_number % 2 == 0)
This function does not validate its parameter.
Write this function in functional style.
e.g., 
func01([3, -2, 7, 0, 12, 6, -9]) -> 4
"""
# from functools import reduce
def func01(ls:list) -> int:
   return len(list(filter(lambda x : x%2==0,ls)))


""" ===============================================================
Problem_02: Write a function 'func02' that receives a list of values 
(the first parameter) and a value (the second parameter).
This function counts the number of values in the list (the first parameter) 
that is less than the value (the second parameter).
(ฟังก์ชันนี้ นับจำนวนค่าในลิสต์ ที่มีค่าน้อยกว่าค่าของพารามิเตอร์ตัวที่สอง)
This function does not validate its parameters.
The values in the list and the value of the second parameters may be 
integers, floats, strings, or any type that can be compared using < (less than).
Write this function in functional style.
e.g.,
func02([], 10) -> 0
func02(['hate', 'love', 'angry', 'fun', 'hunger'], 'happy') -> 2
func02([6, -12.5, 71, 4, 10], 9.9) -> 3
"""
# from functools import reduce
def func02(ls:list, value) -> int:
    #return len(list(filter(lambda x: x<value ,ls)))
    return reduce(lambda c,_: c+1,filter(lambda x : x<value,ls),0)


""" ===============================================================
Problem_03: Write a function 'func03' that receives an integer
and returns a list containing all integers starting from 0 to that integer.
The parameter can be positive, negative, and zero.
This function does not validate its parameter.
Write this function in recursive style.
e.g.,
func03(0) -> [0]
func03(4) -> [0, 1, 2, 3, 4]
func03(-3) -> [0, -1, -2, -3]
"""
def func03(num: int) -> list[int]:
    return [0] if num==0 else func03(num-1)+[num] if num>0 else func03(num+1)+[num]


""" ===============================================================
Problem_04: Write a function 'func04' that receives a list of strings
and returns the summation of the length of all strings in the list.
This function does not validate its parameter.
Write this function in functional style.
e.g., 
func04(['one', 'two', 'three', 'four', 'five']) -> 19
"""
# from functools import reduce
def func04(ls: list[str]) -> int:
    return reduce(lambda x,y :x+y,map(lambda x :  len(x),ls),0)


""" ===============================================================
Problem_05: Write a function 'func05' that receives a list of strings
and returns a string concatenating the first letter of each string in the list.
An empty string is returned if the list is empty or the list contains only empty strings.
This function does not validate its parameter.
Write this function in functional style.
e.g., 
func05(['Strength', 'Weakness', 'Opportunity', 'Threat']) -> 'SWOT'
"""
# from functools import reduce
def func05(ls: list[str]) -> str:
    return reduce(lambda x,y: x+y,map(lambda x: x[0],filter(lambda x: len(x)>0,ls)),'')



""" ===============================================================
Problem_06: Write a function 'func06' that receives a list containing values.
The values may be int, float, str, or any type that can be compare with < and ==. 
This function counts the number of values in the list that are equal to 
the smallest value in the list.  This function returns the count.
(ฟังก์ชันนี้ นับจำนวน ของค่าในลิสต์ ที่มีค่าเท่ากับ ค่าที่ต่ำที่สุดในลิสต์)
For example, if the list is [5, -3, 7, 6, -3, 5, -1, 5], the result is 2
because the smallest value in the list is -3 and there are 2 values in the list equals to -3.
If the list is ['is', 'am', 'are', 'do', 'am', 'is', 'have', 'am', 'are'], the result is 3
because the smallest value is 'am' and there are 3 'am' in the list.
If the list is an empty list (containing no values), then there is no smallest value, 
it returns 0.  This function does not validate its parameter.
Write this function in recursive style.
"""
def func06(ls: list, smallest=None, count=0):
    if ls == []:
        return count
    current = ls[0]
    if (smallest==None) or current < smallest:
        smallest = current
        count =1
    elif current == smallest:
        count+=1
    return func06(ls[1:],smallest,count)


""" ===============================================================
Problem_07: Write a function 'func07' that receives a list containing values 
and a boolean function (that receives a value and returns a bool).
This 'func07' function applies the boolean function to each value in the list, 
counts the result from the boolean function that is True, and returns the count.
This 'func07' function does not validate its parameter.
Write this function in functional style.
e.g.,
func07([6, 7, 8, 5, 4, 2, 9, 6, 3], lambda i: i % 2 == 0) -> 5
"""
from typing import Callable,Any
def func07(ls: list, f:Callable[[Any],bool]) -> int:

    return reduce(lambda c,_: c+1,filter(lambda x: f(x),ls),0)

# solution in imperative style --------------------
def func07im(ls: list, f:Callable[[Any],bool]) -> int:
    count = 0
    for i in range(len(ls)):
        if f(ls[i]):
            count+=1
    return count

""" ===============================================================
Problem_08: Write a function 'func08' that receives a list containing values 
(which may be int, float, str, or any value that can be compared with == and <).
This function returns the second-smallest value in the list.  This function returns None 
if there is less than 2 values in the list or all values in the list are all equal.
Do not to use sorting techniques or duplicate removal techniques (e.g. set/dict).
This function does not validate its parameter.
Write this function in recursive style.
e.g.,
func08([]) -> None
func08(['x']) -> None
func08(['a', 'a']) -> None
func08(['a', 'b']) -> 'b'
func08(['b', 'a']) -> 'b'
func08([300, -11, -20, -11, 300, -20, 50000, 300, 4000]) -> -11
"""
def func08(ls: list[Any]) -> Any|None:
    if (ls == []) or ():
        return None
