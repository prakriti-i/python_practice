name="Prakriti"
surname= 'Subedi'
print("hello, "+name)
print("My name is "+name +surname)
print("My name is ",name,surname)
print(name[0]) #It prints the first letter of name
print(name[1])
#In python, string is like an array of characters

print("\n") #line break

#Using for loop to print characters
for charcter in name:
    print(charcter)
print("\n")

 
alphabets="ABCDEFg"
for a in alphabets:
    print(a)
    
for b in alphabets:
    print(b)
print("\n") #breaks line after completing loop (runs outside loop)

for x in alphabets:
    print("\n")
    print(x) #breaks line after each alphabets (runs inside loop)

a="I want to eat \'apple\'"
print(a)
b="I want to eat \"mango\" "
print(b)
c='He said,"Hi"'
print(c)
d="She said,'hello' "
print(d)

# We cannot use double quote inside double quote OR single quote inside single quote.

# \" \" is used to enclose anything inside double quote inside a string.

#For multi line triple string we use triple quote or triple double quote.

aa=''' Hi!
How are you?
I am good'''
print(aa)

# bb="hi
# how are you"
# print(bb)  (This is not correct)
