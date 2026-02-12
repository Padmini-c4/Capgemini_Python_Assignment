#operators are used to perform a specific operation on operand
#membership operators(in,not in)
lst=[1,2,3,4]
print(2 in lst)
print(5 in lst)
print(5 not in lst)
print(2 not in lst)
#bitwise opeartors(&,|,^,<<,>>)
m=5 #0101
n=3 #0011
print(bin(n))
#why we are only dealing with integer in bitwise
print(m&n) #and
print(m|n)#or
print(~m)#not -(val +1)
print(m^n)#xor
print(m<<1)#left shift
print(m>>1)#right shift


#identity operators(is,is not)
r=[1,2,3]
s=r
t=[1,2,3]
print(r is s)
print(r is t)
print(r is not t) #because of the address it is showing the true but actually the values are same


