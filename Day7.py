# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print(len(it_companies))
#Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
#Insert multiple IT companies at once to the set it_companies
new={"TCS","Infosys","Meta"}
it_companies.update(new)
print(it_companies)
#Remove one of the companies from the set it_companies
it_companies.remove("TCS")
print(it_companies)
#What is the difference between remove and discard
#it_companies.remove("AWS")
print(it_companies) #Raises an error if the element does not exist
it_companies.discard("AWS")
print(it_companies)#Does NOT raise an error if the element is not found
#Join A and B
C=A.union(B)
print(C)
#Find A intersection B
D=A.intersection(B)
print(D)
#Is A subset of B
E=A.issubset(B)
print(E)
#Are A and B disjoint sets
F=A.isdisjoint(B)
print(F)
#What is the symmetric difference between A and B
G=A.difference(B)
print(G)
#Delete the sets completely
del it_companies
del A
del B
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ageset=set(age)
print(ageset)
print(len(age))
print(len(ageset))
#Explain the difference between the following data types: string, list, tuple and set
"""
String: Written in "", Immutable, Ordered ,Indexing is possible
List: Written in [] ,Collection of multiple data types, Mutable , Ordered, Indexing is possible, Allow Duplicate values
Tuple: Written in (),Collection of multiple data types, Immutable ,Ordered, Indexing is possible, Allow Duplicate Values
set: Written in {}, Mutable, Unordered, Does not allow duplicates
"""
#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence="I am a teacher and I love to inspire and teach people"
words=sentence.split()
unique=set(words)
print("Unique words are:",unique)
print(len(unique))