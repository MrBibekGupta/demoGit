
#None-none
#int-123
#float -123.12
#bool-True/False
#complex-12344j
#array-('i',[]):(int,float)
#list-[]:(all type)
#tuple-():(all type)
#set-{}
#dict-{'key':value}
from array import array 
import sys
var1=[1,2,3,3,2,1,4] #list -list caan have duplicate 
var2=set(var1) #set -set only provide unique and no deplicate 
print(var1)
print(var2)
del var1
del var2

# print(var1) #acess value
# print(type(var1))
# print(id(var1))
# #how to print memory size 
# print(sys.getsizeof(var1))
# print(len(var1))
# print(max(var1))
# print(min(var1))
# print(sum(var1))
#class-user defined type
#1.singl value
#none , bool , int , float and complex 
#2.mulriple value 
#list , tuple , set ,dict ,and array 
class c1:
     pass
obj1=c1()
print(type(obj1))
print(id(obj1))
print(obj1)