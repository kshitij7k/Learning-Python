#strings
greeting="Hello"
print(greeting)
#New Style String Formatting (str.format)
r=10
pi=3.14
area=pi*r**2
print("for radius {} area of circle is {}".format(r,area))
#String Interpolation / f-Strings (Python 3.6+)
r=10
pi=3.14
area=pi*r**2
print(f"for radius {r} area of circle is {area}")
#Accessing Characters in Strings by Index
language="Python"
Firstletter=language[0]
print(Firstletter)
lastletter=language[-1]
print(lastletter)
#Slicing Python Strings
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three)
last_three = language[3:]
print(last_three)
reverse=language[::-1]
print(reverse)
skip=language[0::2]
print(skip)
#String Methods
"""
capitalize(): Converts the first character of the string to capital letter
count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.
endswith(): Checks if a string ends with a specified ending
expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
find(): Returns the index of the first occurrence of a substring, if not found returns -1
rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
format(): formats string into a nicer output
index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
isalnum(): Checks alphanumeric character
isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
isdecimal(): Checks if all characters in a string are decimal (0-9)
isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
islower(): Checks if all alphabet characters in the string are lowercase
isupper(): Checks if all alphabet characters in the string are uppercase
join(): Returns a concatenated string
strip(): Removes all given characters starting from the beginning and end of the string
replace(): Replaces substring with a given string
split(): Splits the string, using given string or space as a separator
swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
startswith(): Checks if String Starts with the Specified String
"""
fst="Thirty "
snd="days "
trd="of "
frt="Python "
result=fst + snd + trd  + frt
print(result)

#Declare a variable named company and assign it to an initial value "Coding For All".
company="Coding For All"
print(company)
print(len(company))
res=company.upper()
print(res)
resl=company.lower()
print(resl)
print(company.capitalize(),company.title(),company.swapcase())
print(company[7:])
print(company.index("Coding"))
print(company.find("Coding"))
print(company.replace("Coding","Python"))
print(company.split(" "))
cmp="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(cmp.split(","))
print(company[0])
print(company[-1])
print(company[10])
print(company[0]+company[7]+company[11])
print(company.index("C"))
print(company.index("F"))
print(company.find("l"))
sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex("because"))
print(sentence[31:55])
print(sentence.find("because"))
print(company.startswith("Coding"))
print(company.endswith("Coding"))
wrod='   Coding For All      '
print(wrod.strip())
word="30DaysOfPython"
print(word.isidentifier())
libraries= ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result= "# ".join(libraries)
print(result)
print("I am enjoying this challenge.\nI just wonder what is next.")
print("name\t Age\t country\t city\nkshitij\t 24\t India\t Mah")
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius,area))
a=8
b=6
print(f"{a} + {b} =",a+b)
print(f"{a} - {b} =",a-b)
print(f"{a} * {b} =",a*b)
print(f"{a} / {b} =",a/b)
print(f"{a} % {b} =",a%b)
print(f"{a} // {b} =",a//b)
print(f"{a} ** {b} =",a**b)