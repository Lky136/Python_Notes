""""
#print('Lokesh yadav # this is my first program')
a="hello"
print(a)
print("a")#it will only prints a

Name="lokesh yadav"
#print(name) it will not work because in python it is case sensitive
#Even num="2" this will not work because in python there will be no space between these
Evennum="3"

print(Name)
print(Evennum)
#print(Even num) this will show error
# 3rd in python there is nothing will start from any number like
#1num="2"
#print(1num)

name= input("Enter your name")#this is for input any thing name or anything
print(name)

age=int(input("Enter your age"))
print(age)#here we can entre only an integer because we give int

length=float(input("Enter your length"))
print(length)# in float we can entre an integer it will not show any error but it will not vice versa

exp1= eval(input("Enter your expression"))
print(exp1) #it will also evaluate any python key words like hello

print(type(name))# these will tell us that which data type we enter
print(type(age))
print(type(length))
print(type(exp1))

a=123 #in this we can use type casting it will change any type of to another
b=1.23#like in this example we add an int and float it will give us float value
print(type(a))
print(type(b))
c=a+b
print(c)
print(type(c))

c="123"# this is an explicit data casting because we use double quotation so it is an string not an int
d=1.23 # so we have to change that manually in float or int
print(type(c))
print(type(d))

c=float(c)#like this
c=int(a)
print("after conversion",type(c))
e=c+d
print(e)
print(type(e))

x=12 # this is for swaping the variables value
y=13
temp=x
x=y
print(x)
y=temp
print(y)

w=30 #this is second method for variable swaping
z=40
w,z=z,w
print(w)
print(z)

print(8+2)# arthimetic operators
print(8//3) #floor division
print(2**10) #exponentiation

#comparison operatiors
print(3==6) #equal to
print(3<4)# greater than
print(3!=4)# not equal to

#logical operators
print(3<4 and 35<36) #and
print(3<4 or 35>36) #or
print(not 3<4 or 35>36)#not it is the operator which convert true form into false
print(not 3<4 and 35<36)

#Assignment operator
f=6
f+=6
f-=6
f*=6
print(f)

#identity operator
g=123
h=123
print(g is h) #is
print(h is not g)# is not

#bitwise operators
print(bin(10))
i=10
j=8
print(i & j) #and bitwise operation
print(i | j)  #or bitwise opertor
print(i ^ j)  #Xor bitwise operator
print(10>>1)  #>> zero fill right shift
print(10<<1)  # << zero fill left shift

#Membership operator
k="hello"
print("h" in k)
print("h" not in k)

#conditional statements
marks=97 #if statement
if marks>=90:
    print('you  will get a mobile phone')

print("thank you")

marks=80 #if else
if marks>=90:
    print('you  will get a mobile phone')
else :
    print('you will get a notebook')
print("thank you")

marks=70 #if-elif-else statement
if marks>=90:
if marks>=90:
    print('you  will get a mobile phone')
elif marks>=80:
    print('you  will get a notebook')
else :
    print('no vacation this week')
print("thank you")

marks=40 #nested statement
if marks>=90:
    print('you  will get a mobile phone')
if marks>=80:
    print('you  will get a notebook')
else :
    print('you will be out of class')

marks=91 # short hand if statement
if marks>=90: print("you  will get a mobile phone")

marks=81 #short hand if else statement
print(" you will go to a trip") if marks>=90 else print("no vacation this week")

#write a program to check if a number is positive
num=int(input("Enter a number here:"))
if num>=0:
    print("this num is positive")
else :
    print("this num is negative")

#write a program to check whether a numer is odd or even
num=int(input("Enter a number here:"))
if num/2==0:
    print("number is odd")
else:
    print("number is even")


#write a program to create area calculator
print("area claculator")
print("press 1 to get the area of square"
      "press 2 to get the area of rectangle"
      "press 3 to get the area of triangle")
choice=int(input("Enter your choice:"))
if choice==1:
    side =float(intput("enter the length of the side:"))
    area=side*side
    print("the area of square is",area)
elif choice==2:
    lenght=float(input("enter the length of the length:"))
    breadth=float(input("enter the breadth of the length:"))
    area=lenght*breadth
    print("the area of square is",area)
elif choice==3:
    base=float(input("enter the base of the length:"))
    height=float(input("enter the height of the length:"))
    area=0.5*height*base
    print("the area of triangle is",area)
else:
    print("please enter a valid choice")

#wite a program check whether the passed letter is a vowel or not
letter=input("enter a letter")
if letter in "aeiou" or letter in "AEIOU":
    print("it is a vowel")
else:
    print("it is a consonant")

#write a program to check if a number is a single digit number, 2-digit number and so on up to 5-digit number
num=int(input("Enter a number here up to 5 digit:"))
if num>=0 and num<=9:
    print("it is a single digit number")
elif num>=10 and num<=99:
    print("it is two digit numbers")
elif num>=100 and num<=999:
    print("it is three digit numbers")
elif num>=1000 and num<=9999:
    print("it is four digit numbers")
elif num>=10000 and num<=999999:
    print("it is five digit numbers")
else :
    print("it is six digit numbers")

#Loops
for i in range(1,6): #for loop
    print(i)

for k in range(1,6):
    print("hello world")

for j in range(1,6,2):
    print(j)

n=int(input("Enter a number here:"))
for a in range(1,11):
    print(n,"x",a,"=",n*a)

n=0 # while loop
while n<=10:
     print(n)
     n=n+1

n=1
a=int(input("Enter a number here:"))
while n<=10:
    print(a,"x",n,"=",n*a)
    n=n+1

while True:     #in this t always capital #it is while true loop
    print("hello") #while true

n=1
while True:
    print(n)
    n=n+1

while True:
    number=input("Enter a number here:")
    number2=input("Enter another number here:")
    print(number+number2)
    repeat=int(input("Enter a number here:"))
    if repeat==number:
        break

#nested loop
for i in range (1,6):# outer always count rows
    for j in range (1,11):#inner always count columns
        print(j, end="")
    print()

#nested loop
for i in range (1,6):
    for j in range (1,i+1):
        print(j, end="")
    print()

for i in range (1,6):
    for j in range (5,i,-1):
        print(" ", end=" ")
    for k in range(i):
        print("*", end="")
    print()

for i in range (1,6):
    for j in range (i,0,-1):
        print(j, end=" ")
    print( )

#For loop with conditional statement
for i in range (1,11):
    if i==3:
        print("add this song to the favs")
    else:
        print(i)

for i in range(1,101): #this is the number which was multiple of 8 and 12 b/w 1 to 100
    if i%8==0 and i%12==0:
        print(i)

n=1 # while loop with conditional statement
while n<=10:
    if n==3:
        print("add this sonng to the favs")
    else:
        print(n)
    n=n+1

#continue statement it is used when we want to skip anything
for i in range(1,11):
    if i ==5:
            continue
    else:
        print(i)

#Break statement it is used when we want to  break the loop at certain number or thing
for i in  range(1,11):
    if i==5: # in this 5 will also  be deleted from  this
        break
    else:
        print(i)

#Write a program to find a sum of all the even numbers up to 50
sum=0
for i in range(1,51):
    if i%2==0:
        sum += i
print(" the sum of all the even numbers is", sum)

#Write a program to write first 20 numbers and their squared numbers.
for i in range(1,21):
    print(i,i*i)

#Write a program to find the sum of first 10 odd numbers by using while loop
sum=0
n=0
while n<=20:
    if n%2 !=0:
        sum += n
    n +=1
print("sum of first 10 odd numbers is", sum)

#Write a program to check if a number is divisible by 3 and 9 upto 100
for i in range(1,101):
    if i%3==0 and i%9==0:
        print(i)

#Write a program to create a billing system at supermarket
while True:
    name= input("enter customer's name")
    total=0

    while True:
        print("enter the amount and quantity")
        amount=float(input("enter the amount:"))
        quantity=float(input("enter the quantity:"))
        total +=amount*quantity
        repeat=input("do you want to add more items? (yes/no):")
        if repeat=="no" or repeat=="No":
            break
    print("-"*40)# this is used for making an line of these "-"
    print ("Name:",name)
    print("Amount to be paid:",total)
    print("-"*40)
    print("*****Happy Shopping*****")

    repeat1=input("do you want to go to next customer? (yes/no):")
    if repeat1=="no" or repeat1=="No":
        break

#Write a program to find the length of the following
a="Why fit in, when you are born to stand out!"
b=(len(a))
print(b)

# write a program to check how many times alphabet o is occurring.
a="Why fit in, when you are born to stand out!"
b=(a.count("o"))
print(b)

# Write a program to convert the whole string into lower and upper case.
a="Why fit in, when you are born to stand out!"
x=a.lower()
print(x)
y=a.upper()
print(y)

#Write a program to convert the following  string into a tittle
a="Why fit in, when you are born to stand out!"
z=a.title()
print(z)

#Write a program to find  the index value of "fit in".
a="Why fit in, when you are born to stand out!"
print(a.find("fit in"))

#string methods
a="Harry potter and the goblet of fire"
print(a)
print(len(a)) #length of the string
print(a.count("o")) #count the particular letter in the whole sentence
print(a.upper())
print(a.lower())
print(a.index("o"))# position of o where it is
print(a.index("o",15,34))#give range to find o from where to where you want to search  it
print(a.capitalize()) # to convert first letter to capital
print(a.casefold()) # to convert all capital letter to smaller case
print(a.find("of")) # to find the index number of any character
name="Lokesh yadav"# this is format method
age=24
b="my name is {}. and my age is {}"
print(b.format(name,age))
print(name.center(20)) #it fills the given characters and centralizes a string

a="hello"
b="Hello123"
c="123456"
d="HELLO"
e=" "
f="Hello 123"
g="1.23"
h="Lokesh Yadav"
i="lokesh yadav"
print(a,a.isalnum())  #return true if all characters in the string are alphanumeric
print(b,b.isalnum())
print(a,a.isalpha())  #return true if all characters in  the string are alphabet
print(b,b.isalpha())
print(g,g.isdecimal())  #return  true if all characters in the string ara decimal
print(c,c.isdigit()) # returns true if all characters in the string are only digit
print(g,g.isdigit())
print(b,b.isnumeric()) #return true if all characters in the string are numeric
print(c,c.isnumeric())
print(e,e.isnumeric())
print(a,a.islower())# return true if all characters in the string are in lower case
print(b,b.islower())
print(d,d.isupper()) #return true if all characters in  the string are in upper case
print(e,e.isspace()) #retrun true if all characters in the string are whitespaces
print(f,f.isspace())
print(h,h.istitle())#return true if first letter of all alphabet is capital
print(i,i.istitle())

a="Harry Potter"
b="    harry potter"
c="***Harry Potter ....."
d="oofd#brb#pmw#tb"

print(a.endswith("r")) #return true if the string ends with the specified value
print(a.endswith("P"))
print(a.endswith("t",6,9))
print(a.startswith("H"))  #return true if the string start with the specified value
print(a.startswith("P"))
print(a.startswith("P",6,11))
print(a.swapcase()) #swaps cases lower case becomes upper case  and vice versa
print(b.strip()) #returns a trimmed version of the string
print(c.strip("*,."))
print(d.split("#")) #splits the string at the specified separator and returns a list
x=a.ljust(20,"*")  #returns a left justified version of the string
print(x,"is my fav movie")   #it will make 20space b/w certain statement
x=a.rjust(20,"*") #it will make 20space at the start of the sentence
print(x,"is my fav movie")
print(a.replace("Harry","Lokesh")) #it replace a certain letter or number to anything else
print(a.rindex("Potter")) #it will mention where this letter  belong
print(a.rfind("Potter")) #same as rindex

#String slicing
a="Harry Potter and the goblet of fire"
b="0123456789"
print(a)
print(a[0:5])
print(a[:5])
print(a[5:])
print(a[6:12])
print(a[:12])
print(b[::2]) #it will cut things in gaps
print(b[:7:2])

#Write a program to get Fibonacci series up to 10 numbers
a=0
b=1
print(a)
print(b)
for i in range(2,11):
    c=a+b
    a=b
    b=c
    print(c)

a=0
b=1
n=int(input("Enter a number: "))
if n==1:
    print(1)
else:
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)

#check if number is prime or not
num=int(input("Enter a number: "))
if num<=1:
    print("it is not prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("it is not prime number")
            break
    else:
        print("it is a prime number")

#Problems
a="OOTD.YOLO.ASAP.BRB.GTG.OTW"

#1)Write a program to separate the following  string into coma(,) separated values.
b=a.split(".")
print(b)

#2)Write a program to sort(ascending order) strings alphabetically inn python
b=sorted(a)
print(b)

#3) Write a program to remove a given character from a string
b=a.replace("O","")
print(b)

#4) Write a program to remove dot from the following string
z="F.R.I.E.N.D.S."
b=z.replace(".","")
print(b)

#5)Write a program to check the number of occurrence of a substring in a string.
b=a.count("O")
print(b)

#Take a input from user as a string then reverse it
a=input("enter anything here")
print(a[::-1])

#Lists
fruits=["apple","banana","orange","strawberry,12,13"]
print(fruits)
print(type(fruits)

#Slicing list
a=["Ironman","Thor","Catain America","Hulk"]
print(a[2])
print(a[-2])
print(a[1:])
print(a[:2])
print(a[1:3])

#list iteration

#Iteration using for loop
a=["Hulk","Thor","Catain America","Ironman"]
for i in a:
    print(i)

#Iteration  using for loop with range and length function
a=["Hulk","Thor","Catain America","Ironman"] #It will count the index number
for i in range(len(a)):
    print(i)
    print(a[i])
    print(a[2])
#By while loop
i=0
while i<len(a):
    print(a[i])
    i+=1


#Short hand for loop
a=["Hulk","Thor","Catain America","Ironman"]
[print(i) for i in a]  #IF we do not write it in square bracket it will show error

#List functions
a=["Hulk","Thor","Catain America","Ironman"]
#to find the length of a list
print(len(a))

#to count an occurance of a particular element
print(a.count("Hulk"))

#To add to the list
a.append("Spiderman")  #it will always add any value to the end  of the list
print(a)
a.insert(0,"Spiderman") #It will add according to you where you  want to add
print(a)

#To remove from a list
a.remove("Hulk")
print(a)

#TO remove from a certain  location
print(a.pop(1))

a=["Hulk","Thor","Catain America","Ironman"]

#To create a copy of a list
b=[]
print(b)
b=a.copy()
print(b)

#To access an element
print(a.index("Thor"))

#To entend  the  list
c=["Vision","Superman"]
a.extend(c)
print(a)

#To reverse the list
a.reverse()
print(a)

#To sort the list  (It will arrange acc. to alphabet)
a.sort()
print(a)

#To clear all the data from the list
a.clear()
print(a)

#List Comprehension
l1=[30,40,50,60]

l2=[]
for i in l1:
    if i>45:
        l2.append(i)
print(l1,"\n",l2)

l3=[i for i in l1]
print(l3)
l4=[i for i in l1 if i>45]
print(l4)

#Problems
a=["Rose","Rachel","Monica","Joe"]

#Write a program  to swap first and forth element
a[0],a[3]=a[3],a[0]
print(a)

#Write a program to add a new value at second position
a.insert(1,"Lokesh")
print(a)

#Write a program to delete a value from  3rd position
a.pop(2)
print(a)

b=[13,7,12,10]

#Write a program to multiply all the numbers in the list
mul=1 #here it is 1 because  if we multiply by 0 to something than everything will be 0
for i in (b):
    mul*=i
print(mul)

#Write a program to get the largest number from the list
b.sort()
print(b)
print("The largest value in the given  list is",b[-1])

#Write a program to get the smallest number from the list
b.sort()
print(b)
print("The smallest value in the given  list is",b[0])

#Tuples
a="apple","mango",1,67
print(type(a))
b="Ironmame", #If you want one word to be tuple then put a coma after that word
print(type(b))

#Slicing and Iteration in Tuples:-
a="Oneplus","vivo","realme","samsung","redmi"
print(a[1:3])
print(a[:3])
print(a[-1:])
print(a[::2])  #double :: is used for gaping

#With for loop
for i in a:
    print(i)

#along with range and length in for loop
for i in range (len(a)):
    print(i)
    print(a[i])

#With while loop
i=0
while i<len(a):
    print(a[i])
    i+=1

#Conversion of Tuples and Tuple Functions
a="Oneplus","vivo","realme"
print(type(a))
a=list(a)
print(type(a))
a.append("Vivo")
print(a)
a=tuple(a)
print(type(a))

print(a.count("Vivo"))
print("the index of realme",a.index("realme"))

#Convert the following dictionary into JSON format
    #Student_data={"name":"David","age":13,"marks":87}


#Access the value of age from the fiven data.
import json
Student_data={"name": "David","age":13,"marks":87}
data=json.dumps(Student_data);
print(data)
print(type(data))

#Pretty Print following JSON data.



data1=json.loads(data)
print(data1["age"])

#Sort the following JSON keys and write them into a file.
    #Student_data={"name":"David","age":13,"marks":87}"""

#Dictionary
Employee_data={"name":"Lokesh","age":21,"gender":"male"}
print(Employee_data["age"])
print(Employee_data["gender"])


