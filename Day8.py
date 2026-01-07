#Create an empty dictionary called dog
dog={}

#Add name, color, breed, legs, age to the dog dictionary
dog={
    "name":"lika",
    "color":"White",
    "legs":4,
    "age":18
    }
print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={"first_name":"Durvas",
         "last_name":"Harkulkar",
         "gender":"Male",
         "age":20,
         "marital_status":True,
         "skills":["SW tester","Engineer"],
         "country":"India",
         "city":"Pune",
         "address":"Chikhli"}

#Get the length of the student dictionary
print(len(student))

#Get the value of skills and check the data type, it should be a list
"""skll=student.get("skills")
print(type(skll))"""

#Modify the skills values by adding one or two skills
student["skills"].append("JS")
print(student)

#Get the dictionary keys as a list
keys=student.keys()
print(keys)

#Get the dictionary values as a list
vals=student.values()
print(vals)

#Change the dictionary to a list of tuples using items() method
lst=student.items()
print(lst)

#Delete one of the items in the dictionary
student.popitem()
del student["age"]
print(student)

del dog
