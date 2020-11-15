name = 'Marcos'
age = 21

#Concatenate
print('hello' + name + str(age))

#Arguments by position
print('{1},{2},{0}'.format('a','b','c'))

#Arguments by name
print('My name is {name}'.format(name=name))

#F-strings
print(f'My name is {name} and i am {age}')

#String methods

s = 'this is a test sentence'

#Replace
print(s.replace('test','idk'))

#Count
print(s.count('i'))

#Split into a list
print(s.split())

#Find position
print(s.find('s'))


#Reverse a list
elements = [5,8,6,4]

elements.reverse()

print(elements)

#tuples

#you can not change the order or the values

tup = ('yellow','red','green')

del tup 

#Sets
# a set is a collection that is unordered and unindexed
#no duplicate members allowed

new_set = {5,7,6,8,1,0}

print(new_set)

#check if in set
print(4 in new_set)


#simple dictionary

new_dic = {'name':'marcos','age':20}

print(new_dic['name'])

#list of dictionaries

peopĺe = [
    {'name':'marcos','age':21},
    {'name':'flor'  ,'age':21}
]

print(peopĺe[1]['name'])

# a lambda function is a small anonymus function
# it can take any number of arguments, but can only have one expression         

getsum =lambda num1,num2: num1+num2
print(getsum(5,6))

#in

numbers = [1,2,4,5,8]

x=2

if x in numbers:
    print('hello')

#continue jumps to the next iteration

from functions import sum
value = sum(9,8)
print(f'the result is {value}')


#classes

class User:
    #Constructor
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age

    def greeting(self):
        return f'My name is {self.name}'

    def has_birthday(self):
        self.age +=1

class Customer(User):
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age
        self.balance=0

    def set_balance(self,balance):
        self.balance=balance


#Init user object
user1 = User('Marcos Leon','marcos@gmail.com',21)
user1.has_birthday()

print(user1.age)

user2 = Customer('Jess','jess@gmail.com',23)

user2.set_balance(500)

print(user2.greeting())

import json

userJSON = '{"first_name":"Marcos","age":21}'

#parse to a dictionary
userj = json.loads(userJSON)

print(userj)

