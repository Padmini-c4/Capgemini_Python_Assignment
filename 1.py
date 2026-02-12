#help("keywords") show all the 35 identifiers in the python 3.14.3
'''import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))'''
"""a=5
print(a)
b=False
c=None
print (id(5))
print(id(a))"""
'''a,b,c,d=2,3,4,5
print(a,b,c,d)'''
# why only underscore is one of the exception?? HOMEWORK
#accordinf to isr we can declare upto 72 characters only
'''all variables(container) are identifiers but all the identifiers are all variables'''
#type is a inbuilt function which tells about the datatype of info or the value we give
'''a=5.6
print(type(a))'''
'''a=4
print(float(a))'''
'''a=6.75+4j
print(complex(a))
print(complex())
print(int())'''
'''a=True
print(type(a))
print(bool())'''
'''a='aditya'
b="aditya"
c=''''''aditya''''''
print(type(a))
print(type(b))
print(type(c))'''
#extracting the wanted char from the address
'''a='aditya'
print(a[4])
print(a[-4])'''
#mutable datatype is also called as hashable datatype and immutable datatype is also called as unhashable datatype
#hexadecimal value of an address will not change because of its mutablity
#upper
'''print("hello1&".upper())
#lower
print("HELLO1&".lower())
#capitalize
print("HELLO1& aditya".capitalize())
print("HELLO1& aditya".title())
print("hello1&".isupper())
print("HELLO1&".isupper())
print("hello1&".islower())
print('123'.isdigit())

print('123a'.isdigit())
print('123a'.isalpha())
print('a'.isalpha())
#count
a='banana'
print(a.count("ban"))
print(a.count("a"))
#replace
b="hello world"
print(b.replace("world","python"))
print(b)
b=b.replace("world","python")
print(b)
#split
c="I am aditya"
print(c.split())
d="I am-aditya"
print(d.split())
e="I am-aditya"
print(e.split("-"))
#strip:removes spaces
f="      IAm - aditya  "
print(f.strip())
#list
ls=[1,33.7,"jjf"]
print(type(ls))
print(list[ls])
#append : we can add only one argument inside it
ls.append(45)
print(ls)
ls.extend((45,35,45,34))
print(ls)
#collections are also called as iterables
#insert : based on the index value we insert the  values
ls.insert(1,"knksd")
print(ls)
lsd=[2,4,6,7,5,1,2,1,2,3,3]
lsd.remove(1)#removes first occurance
print(lsd)
lsd.pop(3)
print(lsd)#based on the index the nukber is removed if argument is provided if not last element is removed
lsd.pop()
print(lsd)
lsd.clear()
print(lsd)'''
'''ls=[1,2,3,4,2,4,5,2]
print(ls.index(4))
a=[3,5,1]
a.sort()
print(a)
a.reverse()
print(a)
a.sort(reverse=True)
print(a)
#tuple is immutable datatype
#how many methods?
print(dir(list))
print(dir(str))'''
"""diction={"a":1,"b":2,"c":3}
print(diction)
diction={"a":1,"b":2,"c":3,"a":4}
print(diction)"""
#list is mutable
'''diction={"a":1,"b":2,(1,2,3):4}
print(diction)
diction={"a":1,"b":2,"c":3}
print(diction["c"])'''
#METHODS OF dICTIONARY
'''diction={"a":1,"b":2,"c":3}
print(diction["c"])
print(diction.get ("c"))
print(diction.get ("ccc"))

print(diction.get ("ccc","NOT PRESENTr"))'''
'''print(diction.keys("c"))
print(diction.values("c"))
print(diction.items())'''
'''s1={1,2,3}
dict={}
set={}
print(type(dict))
print(type(s1))

#set is a un ordered collection of immutable values
s1={1,1,1,1,1,1}
s1.add(2)
print(s1)
s2=s1.copy()
print(s1)
print(s2)
s1.add((1,2,3))
print(s1)''' #this type of copiyng is shallow copy 
#diff of shallow,general,deep copies
#in set we dont have indexes
#if the values in set are homo it deletes from first if they are hetero then it can delete any element in the set
'''s1={1,2,3}
s1.remove(20)
print(s1)'''

#to over come the disadvantage of the remove we use discard
s1={1,2,3}
s1.discard(20)
print(s1)





