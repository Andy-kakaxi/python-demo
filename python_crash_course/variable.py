# -*- coding:utf-8 -*-

first_name='albert'
last_name='einstein'
full_name=first_name+' '+last_name
full_name=full_name.title()
message='"A person who never made a mistake never tried anything new"'
#print(full_name+' once said, '+message)
#print('Languages:\nPython\nC\nJavaScript')

favorite_language=' Python '
favorite_language=favorite_language.lstrip()
#print(favorite_language)

# 剔出字符串开头的空白：lstrip();剔出字符串末尾的空白：rstrip();剔出字符串两端的空白：strip()
# str(),字符串转换函数；int()，数值转换函数

age=23
message='Happy '+str(age)+"rd Birthday!"
#print(message)

# 负数索引：-1代表列表最后一个元素，以此类推，-2代表列表倒数第二个元素
# append()方法可用于动态生成列表，例如先创建一个空列表，运用循环和append()方法生成列表元素
# insert()方法有2个输入参数
# del方法需要指定删除元素的索引
# pop()方法默认删除列表末尾元素，pop()方法删除的列表元素可以赋值给变量
# remove()方法用于删除列表指定元素，同时只删除列表中第一个指定的元素
# sort()是列表方法，用于列表永久排序；sorted()是函数，用于列表临时排序
# 字母顺序相反顺序排序，输入参数：reverse=True
# 反转列表元素顺序的方法：reverse()
# len()方法用于计算列表元素个数
# range()函数：生成序列值
# 数值列表函数：max(),min(),sum()

bicycles=['trek','cannodale','redline','specialized']
bicycles[0]='Honda'
bicycles.append('Toyota')
bicycles.insert(0,'BMW')
del bicycles[0]
popped_bicycle=bicycles.pop()
removed_bicycle='redline'
bicycles.remove(removed_bicycle)
#print(sorted(bicycles,reverse=True))
bicycles.reverse()
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)

# 列表解析
squares=[value**2 for value in range(1,11)]
#print(squares)

# 列表切片与复制

bicycles[0:2]
Bicycles=bicycles[:]

cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

#example1:

avaliable_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in avaliable_toppings:
        print('Adding '+requested_topping+'.')
    else:
        print("Sorry,we don't have"+requested_topping+'.')
#print("\nFinished making your pizza!")

#example2:

numbers=list(range(1,10))
for number in numbers:
    if number == 1:
        print(str(number)+'st\n')
    elif number == 2:
        print(str(number)+'nd\n')
    elif number == 3:
        print(str(number)+'rd\n')
    else:
        print(str(number)+'th\n')

#example3:

alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print("Original x_positon:"+str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment=1
elif alien_0['speed'] == 'medium':
    x_increment=2
else:
    x_increment=3

alien_0['x_position']=alien_0['x_position']+x_increment
print('New x-position: '+str(alien_0['x_position']))

# items()方法提取字典的键值对；keys()方法提取字典的键;values()方法提取字典的值；遍历字典时默认遍历所有的键

#example4:

aliens=[]
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: "+str(len(aliens)))

#example5:

users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
    }
for username,userinfo in users.items():
    print('\nUsername: '+username)
    full_name = userinfo['first']+" "+userinfo['last']
    location = userinfo['location']

    print("\tFull name: "+full_name.title())
    print("\tLocation: "+location.title())

# input()函数可以某个变量作为输入参数
# break语句可用于所有Python循环，包括for循环

#example6:

prompt = "\nTell me something,and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
active = True
while active == True:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)


#example7:

unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
active = True

while active == True:
    current_user = unconfirmed_users.pop()
    print("Verifying user: "+current_user.title())
    confirmed_users.append(current_user)

    if len(unconfirmed_users) == 0:
        active = False

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#example8:

responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response
    repeat = input("Would like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name,response in responses.items():
    print(name+" would like to climb "+response+'.')


# 函数参数传递类型：位置参数、关键字参数；函数参数定义了默认值时，有默认值的参数需要放置在未定义默认值的参数后面
# *kw:将函数调用传递的参数封装到一个元组中；**kw:将函数调用传递的参数封装到一个字典中

#example9:
def get_formatted_name(first_name,last_name):
    full_name = first_name+' '+last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name =='q':
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, "+formatted_name+"!")



#example10:

def make_pizza(size,*toppings):
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra chees')

#模块导入：import module_name
#使用别名导入模块：import module_name as mn
#模块导入函数：from module_name import function_0,function_1,function_2
#使用别名导入函数：from module_name import funciton_name as fn
#导入模块中的所有函数：from module_name import *


#example11:

class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer !")

    def increment_odometer(self,miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer !")

class Battery():
    def __init__(self,battery_size):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):

    def __init__(self,make,model,year,battery_size = 70):
        super().__init__(make,model,year)
        self.battery = Battery(battery_size)

my_tesla = ElectricCar('tesla','model s',2019,85)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()



#example12:

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    #for line in file_object:
        #print(line.rstrip())
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#example13:

filename = 'programming.txt'
with open(filename,'w') as file_object:
     file_object.write("test file.\n")

with open(filename,'a') as file_object:
    file_object.write("add text.\n")


#example14:

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

message = "Give me two numbers,and I'll divide them."
message += "\nEnter 'q' to quit."
print(message)

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("\nSecond number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
        

#example15:

import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)

with open(filename) as f_obj:
    json.load(f_obj)

print(numbers)


#example16：

import json

filename = 'username.json'
def get_stored_username():
    """如果存储了用户名，就获取它"""
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input('What is your name ?')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back," + username + "!")
    else:
        username = get_new_username()
        print("We'll remeber you when you come back," + username + "!")

greet_user()


#example16:

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name(
            'wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

unittest.main()

#example17:

from survey import AnonymousSurvey

"""定义一个问题，并创建一个表示调查的AnonymousSurvey对象"""
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Languge: ")
    if response == 'q':
        break
    my_survey.store_response(response)

#显示调查结果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

#example18:

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']

    def test_sotre_single_response(self):
        """测试单个答案会被妥善存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

unittest.main()


