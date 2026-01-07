#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
"""user=int(input("Enter your age:"))
if user>18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18-user} more years to learn to drive.")"""

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
"""my_age=19
print("My age is :",my_age)
your_age=int(input("Enter your age:"))
if my_age > your_age:
    print("Im older than you")
else:
    print(f"You are {your_age-my_age} older than me")"""

#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
"""Enter number one: 4
Enter number two: 3
4 is greater than 3

a=int(input("Enter the no a:"))
b=int(input("Enter the no b:"))
if a>b :
    print(f"{a} is greater than {b}")
elif a<b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} and {b} are equal")"""

#Write a code which gives grade to students according to theirs scores:
"""80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
marks=int(input("Enter the marks :"))
if marks>=90:
    print("A")
elif marks>=70 and marks<=89:
    print("B")
elif marks>=60 and marks<=69:
    print("C")
elif marks>=50 and marks<=59:
    print("D")
else:
    print("F")
    """

#Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
"""month=input("Enter the Month:").capitalize()
if month=="September"or month=="October" or month=="November":
    print("Season is Autum")
elif month=="December" or month=="January" or month=="February":
    print("Season is Winter")
elif month=="March" or month=="April" or month=="May":
    print("Season is Spring")
elif month=="June" or month=="July" or month=="August":
    print("Season is Summer")"""

"""if month in ["September", "October","November"]:
    print("Season is Autum")
elif month in ["December", "January","Febrauary"]:
    print("Season is Winter")
elif month in ["March", "April","May"]:
    print("Season is Spring")
elif month in ["June", "July","August"]:
    print("Season is Summer")
else:
    print("Invalid month")"""

#The following list contains some fruits:
#fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
"""fruits = ['banana', 'orange', 'mango', 'lemon']
user=input("Enter the fruit:").lower()
if user in fruits:
        print("That fruit already exist in the list")
else:
        fruits.append(user)
        print("new fruits list:",fruits)"""

#Here we have a person dictionary. Feel free to modify it!
""" * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:"""

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
"""if "skills" in person:
    skills= person['skills']
    mid=len(skills)//2
    print("Middle index is:",skills[mid])
"""

"""if "skills" in person:
    skills=person['skills']
    if "Python" in skills:
        print("Yes he has python skill")
else:
    print("He doesnt have python skill")"""

"""skills=set(person['skills'])
if skills=={'JavaScript', 'React'}:
    print("He is a front end developer")
elif {'Node', 'MongoDB', 'Python'}.issubset(skills):
    print('He is a backend developer')
elif {'React', 'Node', 'MongoDB'}.issubset(skills):
    print('He is a fullstack developer')
else:
    print('unknown title')"""

if person['is_marred']==True and "Finland" in person['country']:
    print(f"{person['first_name']} lives in {person['country']}. He is married.")
else:
    print("Info is false")