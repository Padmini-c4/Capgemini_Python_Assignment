#oops concepts
#inheritance,Encapsulation,polymorphism,Abstraction
# In inheritance : code reusability,avoid duplication,Easy maintence 
# 5 types 
""" -->Single level inheritance #constructor chaining ,method chaining and for these chaining we use super keyword 
-->Multi level inheritance
-->Single level inheritance
 -->Single level inheritance
-->Single level inheritance
 """
 #disp method is used to display the details
'''class  A:
    a=20
    b=39
    def __init__ (self,c,d):
        self.c=c
        self.d=d
class B(A):
    m=80
    n=0
    b=809
class C(B):
    a=8080
    p=898
print(A.a,A.b)
print(B.a,B.b,B.m,B.n)
print(C.a,C.b,C.p) '''  

# problem statement
# Create RESULT Management System using Multi Level Inheritance
# Requirements :
#     1. Create a class Results 10th
#         Take input:
#             - studnet Name
#             - phone number
#             - email
#             - passing year (10th)
#             - class Name
#         Create a method display() to show all details
#     2. create a class result 12th
#         inherit result 10th
#         use constructor chaining (super().__init__())
#         take input:
#             - passing year 12th
#             - percentage of 12th
#     3.create a class result BE
#         inherit result 12th 
#         use constructor chaining
#         take input
#             -branch
#             -usiniversity
#             -BE percentage


""" class Results10th:
    def __init__ (self,s_name,p_num,email,passing_year10th,class_Name):
        self.s_name=s_name
        self.p_num=p_num
        self.email=email
        self.passing_year10th=passing_year10th
        self.class_Name=class_Name
        
    def display_details(self):
        print("student Name:", self.s_name)
        print("phone number:", self.p_num)
        print("email:", self.email)
        print("Passing year 10th :", self.passing_year10th)
        print("Class name: ",self.class_Name)
class Results12th(Results10th):
    def __init__ (self,s_name,p_num,email,passing_year10th,class_Name,passing_year12th,per_of_12th):
    
        super().__init__(s_name,p_num,email,passing_year10th,class_Name)
        self.passing_year12th=passing_year12th
        self.per_of_12th=per_of_12th
class ResultsBE(Results12th):
    def __init__ (self,s_name,p_num,email,passing_year10th,class_Name,passing_year12th,per_of_12th,branch,University,per_of_BE):
        super().__init__(s_name,p_num,email,passing_year10th,class_Name,passing_year12th,per_of_12th)
        self.branch=branch
        self.University=University
        self.per_of_BE=per_of_BE
        
        
    def display_full_details(self):
        super().display_details()
        
        print("Passing Year 12th:", self.passing_year12th)
        print("12th Percentage:", self.per_of_12th)
        print("Branch:", self.branch)
        print("University:", self.University)
        print("BE Percentage:", self.per_of_BE)
    

#object creation
student=ResultsBE("Padmini",868587680,"padmini@gamil.com",2018,"10th-A",2022,89.6,"IT","JNTUH",89.7)
student.display_full_details() """



    
        
    
    