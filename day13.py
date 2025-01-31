#strings are immutable

a="String"
print(len(a))
print(a.upper())
print(a.lower())


b="new!!!!!!"
print(b.rstrip("!"))  #rstrip() removes what is inside the paranthesis

c="!!new!"
print(c.rstrip("!"))  #but it does not removes it if it is present infront of string

print(a.replace("String", "hello")) #replace "String" with "hello"

d="hola mundo"
print(d.split(" "))  #create list of words separtaed by space
e="manzana platanos naranja"
print(e.split(" "))

f="intRoduction to pytHOn"
print(f.capitalize())  #makes the first letter capital and all other letters small

str="Welcome to python!"
print(str.center(50))  #it adds 50 spaces (keeps th string at the centre)
print(len(str))
print(len(str.center(50)))

s= "sheep are on the ship of sheep owner"
print(s.count("sheep")) #counts the no of "sheep" in s

print(s.endswith("owner"))  #displays "True" if the string ends with owner and "False" if not

str2= "Welcome to console!!"
print(str2.endswith("to", 4,10)) #checks from 5th character to 11th character only
 
str3="She is Sita. She is a student "
print(str3.find("is")) #finds the position of first apperence of "is". returns -1 if it does not find
# print(str2.index("ishhh")) #it searches for the first occurence of the given value and return th index where it is present. If given value is absent from the string, then it raises an exception

str4="holamundo1"
print(str4.isalnum()) #checks if the string only consist of A-Z, a-z, 0-9 (returns false if the string contain space) 

print(str4.isalpha())  #only alphabets no numbers

print(str4.islower()) #true if all the characters are in lowercase

str5=("linebreak\n")
print(str5.isprintable()) #true if everything is printable else false (\n is non-printable)

str6="      "
print(str6.isspace())  #true if it contain white space

str7="Hi Everyone"
print(str7.istitle())  #true if the first letter of each word is capitlaized

str8="Python is a Interperated language"
print(str8.startswith("Python"))

print(str8.swapcase()) #swaps uppercase and lowercase

print(str8.title())  #converts the string into title (converts first letter of each word into uppercase)

