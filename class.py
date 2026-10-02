# class BankAccount:
#     def __init__(self,acountnumber,acountname,acountifsccode,balance):
#         self.acountnumber=acountnumber
#         self.acountname=acountname
#         self.acountifsccode=acountifsccode
#         self.balance=balance
#     def display(self):
#         print(self.acountnumber,self.acountname,self.acountifsccode,self.balance)

# object1=BankAccount(9876543234,"anil","iob098424",10000)
# object1.display()


# amt is a parameter that receives the argument passed to the method.”

# class bankacount:
#     def __init__(self,actnum,actname,ifscode,bal):
#         self.actnum = actnum
#         self.actname = actname
#         self.ifscode = ifscode
#         self.bal = bal
#     def deposit(self,amt):
#         self.bal += amt
#     def withdraw(self,amt):
#         self.bal -= amt
#     def checkbal(self):
#         print(self.bal)
# obt1 = bankacount(9876543987,"anil","iob7656",10000)
# obt1.checkbal()
# obt1.deposit(5000)
# obt1.checkbal()
# obt1.withdraw(1000)
# obt1.checkbal()


# Class= A class is like a blueprint or a template.It defines the properties and behaviors that an object should have. 
# For example, BankAccount can be a class with account number, name, and balance as properties, 
# and deposit and withdraw as methods.

# Object = “An object is an instance of a class. It is used to access the properties and methods defined
# inside the class. For example, if BankAccount is a class, account1 can be an object of that class.”




# print 1 to 100 prime numbers 

# for n in range(2,101):
#     count=0
#     for i in range(1,n+1):
#         if n % i==0:
#             count+=1
#     if count==2:
#         print(n,end=" ")



# write a code of particular number?

# num=23
# count = 0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print("prime")
# else:
#     print("not prime")
    


# for n in range(10,51):
#     count =0
#     for i in range(1,n+1):
#         if n % i ==0:
#             count+=1
#     if count==2:
#         print(n,end=" ")

