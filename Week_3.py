# Functions
#Defining it (A function is a reusable block of code designed to perform a specific task.)

def greet(name):
    return f"Hello,{name} !"
print(greet("AI"))



def greet(name):
    print("Hello",name, "! Welcome.")

name = input("Enter Name :")
greet(name)
#Part	Meaning
#def	      Keyword used to define a function
#greet	      Function name
#()	          Parameters go here
#:	          Starts the function body
#Indented code	Function body


#Multiple parameters

#Greeting with name and age
def greet(name,age):
    print("Hello",name,"!")
    print("You are",age,"years old.")
    
name = input("Enter name :")
age = int(input("Enter your age :"))

greet(name,age)

#Default arguments (A default parameter is a parameter that already has a value. If the user doesn't provide a value, Python uses the default value.)

def greet(name="User"):
    print("hello",name)

greet()


#Keyword arguments
#Local vs global variables
#*args
#**kwargs
#Lambda functions


#2. Strings
#Indexing & slicing


#upper(), lower(), capitalize()
#strip()
#replace()
#split()
#join()
#find()
#count()
#startswith() / endswith()
#f-strings
#String formatting
