'''import copy
a=[1,2,3]
b=copy.copy(a)
a.append(4)
print(a)
print(b)'''
#slicing is only done on collection datatype
s="BVRIT COLLGE OF ENGINEERING"
'''print(s[0:5])
print(s[-13:-8])
print(s[:-8])
print(s[-12:-7])'''
'''print(s[-11:])
print(s[-12:0])#the compiler will be confused and return the empty list
print(s[-12:-1])#it will consider the space and not return the last character 
print(s[-12:len(s)])
print(s[:-12:-1])
print(s[::-1])
print(s[-11:])'''
#output
#print(2,3,4,sep='@') #sep is seperator 
#print(1,2,3,4,5,end='#')#end is used to return the last character
#print(1,2,3,4,sep='\t',end='#')
#print(1,2,3,4,sep='\t',end='\n')
#print(1,2,3,4,end='#')
'''x=print("hello")
print(x)
#comprehension will increase the efficiency of program
lst=[i for i in range(1,11)]
print(lst)
old_lst=[i for i in range(1000,1501) if i%2 !=0]
print(old_lst)
res=[i**2 if i% 2 == 0 else i**3 for i in range(1,11)]#lst where number is even we are doing square if not cube
print(res)'''
#word legth 
#input = python is very very easy language
#output = [("python",6)]# length of the word 
'''str="Python is very very easy language"
output=[(i[0:],len(i))for i in str.split()]
print(output)
output=[(word.lower(),len(word)) for word in str.split()]
print(output)
#natural numbers as key and their squares as values
d={i:i**2 for i in range (1,101 )}
d1={i:i**2 for i in range (1,101 )if i%2==0}
d2={i:i**2 if i%2==0 else i**3  for i in range (1,101 )}#as key is always same 
print(d)
print(d1)
print(d2)
input="Hai HeLLO"
#output={'H':72}
output={i:ord(i) for i in input if i.isupper()}
print(output)'''
'''import re
s="python is very easy"
print(re.search ("easy",s))#used find the pattern anywhere
print(re.match("python",s))#used to find the pattern only at the beginning
m=re.search(r"\d+","Age is 21")#covert the special behaviour to normal behaviour
print(m.group())
c=re.search(r"(\d+)-(\d+)_(\d+)","2025-02234513_366")
print(c.groups())
c=re.search(r"(\d+)-(\d+)_(\d+)","2025-02234513_366")
print(c.group())

c=re.search(r"\d+-\d+_\d+","2025-02234513_366")
print(c.group())#group=takes the single match,groups = takes the multiple sub-maches'''
import re
print(re.search(r"ab*","a"))
print(re.search(r"ab+","abbb"))
print(re.search(r"colou?r","color"))
print(re.search(r"\d{4}","Year 2025"))
print(re.search(r"\d{2,4}","ID: 123"))
#matches two to four digits (12,123,1234)
#n=minimum times,m=maximum times




