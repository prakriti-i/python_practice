#slicing in python
# #accessing characters from a string
name= "ram, sam, sita, gita"
print(name[0:7])

#finding the length of string
a="Hello"
length=len(a) 
print(length)
b="apple"
print(b, "is a", len(b), "letter word" )
print(name[1])
print(b[0:2]) #to access characters from a string (does not access 3rd character)
print(b[:3]) #it automatically starts from 0
print(name[5:8])

#negative slicing
print(a[0:len(a)-2]) #it removes last 2 characters
print(a [0:-2]) #same as last line
print(a[-4:-2]) #from len(a)-4 to len(a)-2 => (5-4=1 to 5-2=3)
print(a[1:3]) #similar to last line

x="computer"
print(x[-4:-2])
print(x[4:6])

