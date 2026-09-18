# List -->    List is mutable which means can be changed.It can perform function like Append(),Insert(),Remove

# 1.Creating and accessing list (All list store multiple value in on variable)
a = [2,4,6,8,10]
print(a)       #created

fruits =["Apple","Mango","Papaya","Watermelon"]
print(fruits[0])         #Accessing
print(fruits[1])
print(fruits[2])

#2. Indexing and Slicing
a = [2,4,6,8,10]                               #Indexing - Means getting one specific item
print(a[0])
print(a[3]) 

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])                            #Slicing - Means getting multiple items
print(numbers[ :4])                            #End is not included
print(numbers[-4:-1])                          #-1 start from last



#  3. append(), insert(), remove(), pop()

a = [2,4,6,8,10]
a.append(12)            # append
print(a)
print(type(a))

fruits =["Apple","Mango","Papaya","Watermelon"]
fruits.insert(1,"Melon") 
print(fruits)             #insert


fruits =["Apple","Mango","Papaya","Watermelon"]
fruits.remove("Mango") 
print(fruits)             #remove - Remove item by its value

fruits =["Apple","Mango","Papaya","Watermelon"]
fruits.pop(3)
print(fruits)             #pop - removes item by its index 



#Tuple - Immutable means cannot change 

#1. Creating a Tuple

fruits =("apple","banana","citrus orange","guava")
print(fruits)

#2. Accessing a tuple
fruits =("apple","banana","citrus orange","guava")
print(fruits[0])
print(fruits[2])

#3. Slicing 

a = (10,20,30,40)
print(a[1:3])
print(a[:3])

#4.Immutable
a = (10,20,30,40)
#a.append(50)         #Not changable

#5. Tuple Methods (Tuples have fewer methods because you can't modify them)

#Count
a = (10,20,10,30,40,10)
print(a.count(10))

#index
a = (10,20,10,30,40,10)
print(a[2])
