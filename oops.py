#class is a blue print
#creation
'''class ClassName:
    properties #variables
    functions #characters'''
'''class Mobile:
    brand="Samsung"#brand and price are the static properties for example school name,location is same for evrey studnet in the school
    price=20000
m1=Mobile()
m2=Mobile()
print(m1.brand)
print(m2.price)
print(m1.price)
Mobile.price="13000" 
print(m1.brand)
print(m2.brand)
print(m1.price)
print(m2.price)'''


#object is an instance in the class 
#creation
'''object_name=ClassName(arguments)'''
#modification using objects
#types of properties/states
#static properties for example school name,location is same for evrey studnet in the class
#specific properties for exaple studnet name,roll no is different for all the studnets in the school
'''class School:
    sname="parg school"
    loc="srd"
    time="9 Am - 3pm"
    website="www.prag.com"

st1=School()
st1.name="Aditya"
st1.sid=1
st1.age=14
st1.clas=5
print(st1.sname)

st2=School()
st2.name="Adihi"
st2.sid=3
st2.age=18
st2.clas=8
print(st2.name,st2.sid,st2.age,st2.clas)'''

#create a bank class
#it should have 4 static (class)members
#create 5 objects
#each object should have 5 object(specific) members
'''class Bank:
    bname="canara"
    manager_name="tara"
    b_num=8079654745
    loc="hyd" 
    def set_details(obj,ac_holder_name,per_ac,zero_ac,pho_num,address):
        obj.ac_holder_name=ac_holder_name
        obj.per_ac=per_ac
        obj.zero_ac=zero_ac
        obj.pho_num=pho_num
        obj.address=address
b1=Bank()
Bank.set_details(b1,"hari","234-687-789","787-868-690",9857798969,"srd")
Bank.set_details(b1,"hara","968-968-746","077-965-857",8785758578,"delhi")
Bank.set_details(b1,"hema","785-853-765","868-965-768",9657475879,"kerala")
Bank.set_details(b1,"hero","245-256-634","554-253-245",7057758689,"nkd")
Bank.set_details(b1,"heth","970-973-898","979-786-964",7966869700,"goa")
print(b1.ac_holder_name)'''



'''b1=Bank()
b1.ac_holder_name="hari"
b1.per_ac="234-687-789"
b1.zero_ac="787-868-690"
b1.pho_num=9857798969
b1.address="srd"

b2=Bank()
b2.ac_holder_name="hara"
b2.per_ac="968-968-746"
b2.zero_ac="077-965-857"
b2.pho_num=8785758578
b2.address="delhi"

b3=Bank()
b3.ac_holder_name="hema"
b3.per_ac="785-853-765"
b3.zero_ac="868-965-768"
b3.pho_num=9657475879
b3.address="kerala"

b4=Bank()
b4.ac_holder_name="hero"
b4.per_ac="245-256-634"
b4.zero_ac="554-253-245"
b4.pho_num=7057758689
b4.address="nkd"

b5=Bank()
b5.ac_holder_name="heth"
b5.per_ac="970-973-898"
b5.zero_ac="979-786-964"
b5.pho_num=7966869700
b5.address="goa" '''

class Bank:
#static/class members
    bname:"SBI"
    branch="Hyderabad"
    ifsc="SBIN000123"
    helpline="1800-11-2211"
#constructor to initialize object members
    def __init__(self,name,age,phone,pan,balance):#self take object value
        self.name=name
        self.age=age
        self.phone=phone
        self.pan=pan
        self.balance=balance
    def withdraw (self,amount):
        if amount<=0:
            print("invalid amount")
            return
        if self.balance>=amount:
            self.balance -= amount
        else:
            print("no sufficient balance")
#creating objects (5 objects with 5 object members
c1=Bank("h",22,99007779,"akhuh",500000)
c2=Bank("j",27,34686532,"nkbbj",350000)
c3=Bank("l",29,54665565,"nhhik",520000)
c4=Bank("o",26,68655356,"iuguj",100000)
c5=Bank("p",23,73464654,"jyugi",790000)
#object method
'''def display (self):
    print(self.name,self.phone,self.balance)
def change_phone(self,new_phone):
    self.phone=new_phone'''

c1.withdraw(-5000)
print(c1.balance)











