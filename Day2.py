#Built-in functions
# print(), len(), type(), int(), float(), str(), input(), list(), dict(), min(), max(), sum(), sorted(), open(), file(), help(), and dir()
a = "Hello World"
print(a) #prints the given string 
print(len(a)) #gives length 
print(type(a)) #gives data type
b=100
print(str(b)) #converts no to string
print(float(b)) #converts into float
d=10,11,16,9,20
print(max(d))      #prints max no from d
print(min(d))      #prints min no from d
print(max(10,20,60,11,26,90))
print(min(10,20,60,11,26,90))
print(sum([10,20,60,11,26,90])) #takes only list as an arg and return the sum

#Getting user input using the input() built-in function. Let us assign the data we get from a user into first_name and age variables. Example:
"""first_name=input("Enter your name:")
age=int(input("Enter the age:"))
print("your first name is",first_name)
print("your age is",age)"""

#Data Types
print(type("hello"))
print(type(100))
print(type(10.5))
print(type(2+10j))
print(type(False))
print(type((10,11,20,13)))
print(type([10,9,"leaf","tree"]))
print(type({"name":"Sandip","Roll no":200}))
print(type(zip([1,2],[3,4,5,6])))

#Casting: Converting one data type to another data type.
#int into float
a=10
print(float(a))

#float into int
b=100.50
print(int(b))

#int to str
d=120
print(str(d))

#str to int
e='190'
print(int(e))

#str to list
strng="hello bro"
print(list(strng))

"""Number data types in Python:
1) Integer : -ve,zero,+ve (-1, -2, 0, 1, 2,....)
2) Float : Decimal numbers (-12.34, -2.0, 5.0, 3.14)
3) Complex : 1+i, 2-1j"""

"""Exercises: Level 1
Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
Write a python comment saying 'Day 2: 30 Days of python programming'
Declare a first name variable and assign a value to it
Declare a last name variable and assign a value to it
Declare a full name variable and assign a value to it
Declare a country variable and assign a value to it
Declare a city variable and assign a value to it
Declare an age variable and assign a value to it
Declare a year variable and assign a value to it
Declare a variable is_married and assign a value to it
Declare a variable is_true and assign a value to it
Declare a variable is_light_on and assign a value to it
Declare multiple variable on one line"""

#Day 2: 30 Days of python programming
first_name="Rax"
last_name="Adam"
full_name="Rax Adam"
country="India"
city="Pune"
age=19
year=2026
is_married = False
is_true = False
fst,lst,full,cnt,cty,ag,year="rax","adam","rax adam","Japan","Tokyo",20,2027
print(fst,lst,full,cnt,cty,ag,year)

"""Exercises: Level 2
Check the data type of all your variables using type() built-in function
Using the len() built-in function, find the length of your first name
Compare the length of your first name and your last name
Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords"""

print(type(first_name))
print(len(first_name))
print(len(first_name)==len(last_name))
num_one=5
num_two=4
total=num_one+num_two
print(total)
diff=num_two-num_one
print(diff)
product=num_one*num_two
print(product)
division=num_one/num_two
print(division)
mod=num_two%num_one
print(mod)
exp=num_one**num_two
print(exp)
floor_division=num_one//num_two
print(floor_division)
#The radius of a circle is 30 meters.
radius=30
area_of_circle=3.14*radius*radius #A=πr^2
print(area_of_circle)

circum_of_circle=2*3.14*radius
print(circum_of_circle)

rad=int(input("Enter the radius:"))
area=3.14*rad**2
print(area)

fname=input("Enter the first name")
lname=input("Enter the last name")
coun=input("Enter the country name")
age=int(input("Enter the age"))
print(fname,lname,coun,age)