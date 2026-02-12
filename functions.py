'''def fname(args):
    # stmt block
    return value
#dunction calling
 fname(vals)'''

'''def greet():
    print("hello world")
greet()
#wap to create a function that prints the sum of two numbers(user input)
def add():
    a=int(input())
    b=int(input())
    print("SUM=",a+b)
add()

def add(a,b):
    return a+b
result=add(10,20)
print(result)
#function with args and without return values
#waf that takes a name and prints a welcome msg
def welcome(name):
    print("Welcome",name)
welcome("padmini")#these values are called as actual arguments
#function without argumnets and with return values
#wap to print palindrome number without using slicing and function type should with args and return values 
#wap to find n no.of prime numbers and function type is with args and return types ,n values is from user side'''
'''def palindrome(a):
    o_num = a
    rev = 0
    while a > 0:
        s = a % 10        
        rev = rev * 10 + s
        a = a // 10      
    return o_num == rev

a = int(input())
print(palindrome(a))'''

'''def palindrome(value):
    value = str(value)  
    rev = ""
    for ch in value:
        rev = ch + rev
    return "Palindrome" if value == rev else "Not a palindrome"

a= input("Enter input: ")
print(palindrome(a))


def first_n_primes(n):
    primes = []
    num = 2

    while len(primes) < n:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1

    return primes


n = int(input("Enter: "))
result = first_n_primes(n)

print("First", n, "prime numbers:")
print(result)
#*n is uded to take the values into the form of tuple,double astrick for key and values'''
'''even_odd = lambda n: "Even" if n%2==0 else "odd"
print(even_odd(5))'''
#wap to check whether the given data is float or not

id_float=lambda x: "Float" if type(x) == float else "NOt float"
print(id_float(10.8))

#wap to find sum of 3 numbers
sum=lambda a,b,c:a+b+c
print(sum(1,2,3))




        


    