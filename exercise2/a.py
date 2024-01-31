#print(10 > 9)
#True

#print(10 == 9)
#False

#print(10 < 9)
#False

#print(bool("abc"))
#True

#print(bool(0))
#False

#print(10*5)
# Output:50

#print(10 /5)
# Output:2

#fruits = ["apple", "banana"]
#if "apple" in fruits:
    #print("Yes, apple is a fruit!")
    # Output:Yes, apple is a fruit!
    
    #if 5!= 10:
  #print("5 and 10 is not equal")
#   Output:5 and 10 is not equal
  
# if 5 == 10 or 4 == 4:
#   print("At least one of the statements is true")
#   Output:At least one of the statements is true
  
# fruits = ["apple", "banana", "cherry"]
# print(fruits[1])
# Output:banana

# fruits = ["apple", "banana", "cherry"]
# fruits[0]= "kiwi"
# print(fruits)
# Output:['kiwi', 'banana', 'cherry']

# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")
# print(fruits)
# Output:['apple', 'banana', 'cherry', 'orange']

# fruits = ["apple", "banana", "cherry"]
# fruits.insert(1,"lemon")
# print(fruits)
# Output:['apple', 'lemon', 'banana', 'cherry']

# fruits = ["apple", "banana", "cherry"]
# print(fruits[-1])
# Output:cherry


# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(fruits[2:5])
# Output:['cherry', 'orange', 'kiwi']

# fruits = ["apple", "banana", "cherry"]
# print(len(fruits))
# Output:3

# fruits = ("apple", "banana", "cherry")
# print(fruits[0])
# Output:apple

# fruits = ("apple", "banana", "cherry")
# print(len(fruits))
# Output:3

#fruits = ("apple", "banana", "cherry")
#print(fruits[-1])"""
#Output:("cherry")

#fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
#print(fruits[2:5]) 
#Output:('cherry', 'orange', 'kiwi')

# fruits = {"apple", "banana", "cherry"}
# if "apple" in fruits:
#   print("Yes, apple is a fruit!")
# Output:Yes, apple is a fruit!

# fruits = {"apple", "banana", "cherry"}
# fruits.add("orange")
# print(fruits)
# Output:{'cherry', 'apple', 'orange', 'banana'}

# fruits = {"apple", "banana", "cherry"}
# more_fruits = ["orange", "mango", "grapes"]
# fruits.update(more_fruits)
# print(fruits)
# Output:{'cherry', 'orange', 'banana', 'apple', 'mango', 'grapes'}

# fruits = {"apple", "banana", "cherry"}
# fruits.remove("banana")
# print(fruits)
# Output:{'apple', 'cherry'}

# fruits = {"apple", "banana", "cherry"}
# fruits.discard("banana")
# print(fruits)
# Output:{'apple', 'cherry'}

# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(car.get("model"))
# output:Mustang


# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car["year"]=2020
# print(car)
# Output:{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car["color"]="red"
# print(car)
# Output:{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.pop("model")
# print(car)
# Output:{'brand': 'Ford', 'year': 1964}


# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.clear()
# print(car)
# Output:{}

# a = 50
# b = 10
# if a >b:
#     print("Hello World")
# Output:Hello World

# a = 50
# b = 10
# if a !=b:
#     print("Hello World")
# Output:Hello World

# a = 50
# b = 10
# if a ==b:
#     print("Yes")
# else:
#     print("No")
#     Output:No

# a = 50
# b = 10
# if a ==b:
#     print("1")
# elif a >b:
#     print("2")
# else:
#     print("3")
# Output:2

# if a == b and c == d:
#   print("Hello")
#   Output:Hello

#  if a == b or c == d:
#   print("Hello")
#   Output:Hello

# if 5 > 2:
#  print("YES")
#  Output:YES

# a = 2
# b = 5
# print("YES") if a==b else print("NO")
# Output:NO

# a = 2
# b = 50
# c = 2
# if a==c or b==c:
#   print("YES")
#   Output:YES

# i = 1
# while i < 6:
#     print(i)
#     i += 1
#     Output:
# 1
# 2
# 3
# 4
# 5

# i = 1
# while i < 6:
#   if i == 3:
#     break
# i += 1


# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
# print(i)
# Output:6

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")
# Output:
#     1
# 2
# 3
# 4
# 5
# i is no longer less than 6

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     Output:
# apple
# banana
# cherry

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
# print(x)
# Output:cherry

# for x in range(6):
#     print(x)
#     Output: 
#         0
# 1
# 2
# 3
# 4
# 5

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
# print(x)
# Output:banana

