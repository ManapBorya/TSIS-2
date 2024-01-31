#1
#In programming you often need to know if an expression is True or False.
#You can evaluate any expression in Python, and get one of two answers, True or False.
#When you compare two values, the expression is evaluated and Python returns the Boolean answer:

"""print(10 > 9)
print(10 == 9)
print(10 < 9)"""

#2
#Print a message based on whether the condition is True or False:

"""a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")"""

#3
#The bool() function allows you to evaluate any value, and give you True or False in return,

#Example
#Evaluate a string and a number:

"""print(bool("Hello"))
print(bool(15))"""

#4
#Evaluate two variables:

"""x = "Hello"
y = 15
print(bool(x))
print(bool(y))"""

#5
#Almost any value is evaluated to True if it has some sort of content.
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.
#Example
#The following will return True:

"""print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))"""

#6
#In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
#Example
#The following will return False:

"""print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))"""

#7
#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
#Example

"""class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))"""

#8
#Functions can Return a Boolean
#You can create functions that returns a Boolean Value:
#Example
#Print the answer of a function:

"""def myFunction() :
  return True
print(myFunction())"""

#9
#Example
#Print "YES!" if the function returns True, otherwise print "NO!":

"""def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")"""

#10
#Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
#Example
#Check if an object is an integer or not:

"""x = 200
print(isinstance(x, int))"""

#11
#Python Operators
#Operators are used to perform operations on variables and values.
#In the example below, we use the + operator to add together two values:

"""print(10 + 5)"""

#12
#Example
#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

"""print((6 + 3) - (6 + 3))"""

#13
#Example
#Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:

"""print(100 + 5 * 3)"""

#14
#Example
#Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:

"""print(5 + 4 - 7 + 3)"""

#15
#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets:
#Create a List:

"""thislist = ["apple", "banana", "cherry"]
print(thislist)"""

#16
#Allow Duplicates
#Since lists are indexed, lists can have items with the same value:
#Example
#Lists allow duplicate values:

"""thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)"""

#17
#To determine how many items a list has, use the len() function:
#Example
#Print the number of items in the list:

"""thislist = ["apple", "banana", "cherry"]
print(len(thislist))"""

#18
#List items can be of any data type:
#Example
#String, int and boolean data types:

"""list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)"""

#19
#A list with strings, integers and boolean values:

"""list1 = ["abc", 34, True, 40, "male"]
print(list1)"""

#20
#From Python's perspective, lists are defined as objects with the data type 'list':
#Example
#What is the data type of a list?

"""mylist = ["apple", "banana", "cherry"]
print(type(mylist))"""

#21
#It is also possible to use the list() constructor when creating a new list.
#Example
#Using the list() constructor to make a List:

"""thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)"""

#22
#List items are indexed and you can access them by referring to the index number:
#Example
#Print the second item of the list:

"""thislist = ["apple", "banana", "cherry"]
print(thislist[1])"""

#23
#Negative indexing means start from the end
#-1 refers to the last item, -2 refers to the second last item etc.
#Example
#Print the last item of the list:

"""thislist = ["apple", "banana", "cherry"]
print(thislist[-1])"""

#24
#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new list with the specified items.
#Example
#Return the third, fourth, and fifth item:

"""thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])"""

#25
#This example returns the items from the beginning to, but NOT including, "kiwi":

"""thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])"""

#26
#By leaving out the end value, the range will go on to the end of the list:
#Example
#This example returns the items from "cherry" to the end:

"""thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])"""

#27
#Specify negative indexes if you want to start the search from the end of the list:
#Example
#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

"""thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])"""

#28
#To determine if a specified item is present in a list use the in keyword:
#Example
#Check if "apple" is present in the list:

"""thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")"""

#29
#To change the value of a specific item, refer to the index number:
#Example
#Change the second item:

"""thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)"""

#30
#To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
#Example
#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

"""thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)"""

#31
#Change the second value by replacing it with two new values:

"""thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)"""

#32
#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
#Example
#Change the second and third value by replacing it with one value:

"""thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)"""

#33
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
#The insert() method inserts an item at the specified index:
#Example
#Insert "watermelon" as the third item:

"""thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)"""

#34
#o add an item to the end of the list, use the append() method:
#Example
#Using the append() method to append an item:

"""thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)"""

#35
#To insert a list item at a specified index, use the insert() method.
#The insert() method inserts an item at the specified index:
#Example
#Insert an item as the second position:

"""thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)"""

#36
#To append elements from another list to the current list, use the extend() method.
#Example
#Add the elements of tropical to thislist:

"""thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)"""

#37
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
#Example
#Add elements of a tuple to a list:

"""thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)"""

#38
#he remove() method removes the specified item.
#ExampleGet your own Python Server
#Remove "banana":

"""thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)"""

#39
#If there are more than one item with the specified value, the remove() method removes the first occurance:
#Example
#Remove the first occurance of "banana":

"""thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)"""

#40
#The pop() method removes the specified index.
#Example
#Remove the second item:

"""thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)"""

#41
#If you do not specify the index, the pop() method removes the last item.
#Example
#Remove the last item:

"""thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)"""

#42
#The del keyword also removes the specified index:
#Example
#Remove the first item:

"""thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)"""

#43
#The del keyword can also delete the list completely.
#Example
#Delete the entire list:

"""thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)"""
#this will cause an error because you have succsesfully deleted "thislist".

#44
#The clear() method empties the list.
#The list still remains, but it has no content.
#Example
#Clear the list content:

"""thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)"""

#45
#You can loop through the list items by using a for loop:
#Example
#Print all items in the list, one by one:

"""thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)"""

#46
#You can also loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
#Example
#Print all items by referring to their index number:

"""thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])"""

#47
#You can loop through the list items by using a while loop.
#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
#Remember to increase the index by 1 after each iteration.
#Example
#Print all items, using a while loop to go through all the index numbers

"""thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1"""

#48
#List Comprehension offers the shortest syntax for looping through lists:
#Example
#A short hand for loop that will print all items in a list:

"""thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]"""

#49
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#Example:
#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#Without list comprehension you will have to write a for statement with a conditional test inside:
#Example

"""fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)"""

#50
#With list comprehension you can do all that with only one line of code:
#Example
"""fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)"""

#51
#The condition is like a filter that only accepts the items that valuate to True.
#Example
#Only accept items that are not "apple":

"""fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)"""

#52
#The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
#The condition is optional and can be omitted:
#Example
#With no if statement:

"""fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)"""

#53
#The iterable can be any iterable object, like a list, tuple, set etc.
#Example
#You can use the range() function to create an iterable:

"""newlist = [x for x in range(10)]
print(newlist)"""

#54
#Same example, but with a condition:
#Example
#Accept only numbers lower than 5:

"""newlist = [x for x in range(10) if x < 5]
print(newlist)"""

#55
#The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
#Example
#Set the values in the new list to upper case:

"""fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)"""

#56
#You can set the outcome to whatever you like:
#Example
#Set all values in the new list to 'hello':

"""fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)"""

#57
#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
#Example
#Return "orange" instead of "banana":

"""fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)"""

#58
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
#ExampleGet your own Python Server
#Sort the list alphabetically:

"""thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)"""

#59
#Sort the list numerically:

"""thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)"""

#60
#To sort descending, use the keyword argument reverse = True:
#Example
#Sort the list descending:

"""thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)"""

#61
#Sort the list descending:

"""thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)"""

#62
#You can also customize your own function by using the keyword argument key = function.
#The function will return a number that will be used to sort the list (the lowest number first):
#Example
#Sort the list based on how close the number is to 50:

"""def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)"""

#63
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
#Example
#Case sensitive sorting can give an unexpected result:

"""thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)"""

#64
#Luckily we can use built-in functions as key functions when sorting a list.
#So if you want a case-insensitive sort function, use str.lower as a key function:
#Example
#Perform a case-insensitive sort of the list:

"""thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)"""

#65
#What if you want to reverse the order of a list, regardless of the alphabet?
#The reverse() method reverses the current sorting order of the elements.
#Example
#Reverse the order of the list items:

"""thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)"""

#66
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
#There are ways to make a copy, one way is to use the built-in List method copy().
#Example
#Make a copy of a list with the copy() method:

"""thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)"""

#67
#Another way to make a copy is to use the built-in method list().
#Example
#Make a copy of a list with the list() method:

"""thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)"""

#68
#here are several ways to join, or concatenate, two or more lists in Python.
#One of the easiest ways are by using the + operator.
#Example
#Join two list:

"""list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)"""

#69
#Another way to join two lists is by appending all the items from list2 into list1, one by one:
#Example
#Append list2 into list1:

"""list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)"""

#70
#Or you can use the extend() method, where the purpose is to add elements from one list to another list:
#Example
#Use the extend() method to add list2 at the end of list1:

"""list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)"""

#71
#Tuples are used to store multiple items in a single variable.
#Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
#A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets.
#Example
#Create a Tuple:

"""thistuple = ("apple", "banana", "cherry")
print(thistuple)"""

#72
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
#Ordered
#When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#Unchangeable
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#Allow Duplicates
#Since tuples are indexed, they can have items with the same value:
#Example
#Tuples allow duplicate values:

"""thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)"""

#73
#Tuple Length
#To determine how many items a tuple has, use the len() function:
#Example
#Print the number of items in the tuple:

"""thistuple = ("apple", "banana", "cherry")
print(len(thistuple))"""

#74
#Create Tuple With One Item
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
#Example
#One item tuple, remember the comma:

"""thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))"""

#75
#Tuple items can be of any data type:
#Example
#String, int and boolean data types:

"""tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)"""

#76
#A tuple can contain different data types:
#Example
#A tuple with strings, integers and boolean values:

"""tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)"""

#77
#From Python's perspective, tuples are defined as objects with the data type 'tuple':
#<class 'tuple'>
#Example
#What is the data type of a tuple?

"""mytuple = ("apple", "banana", "cherry")
print(type(mytuple))"""

#78
#It is also possible to use the tuple() constructor to make a tuple.
#Example
#Using the tuple() method to make a tuple:

"""thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)"""

#79
#You can access tuple items by referring to the index number, inside square brackets:
#Example
#Print the second item in the tuple:

"""thistuple = ("apple", "banana", "cherry")
print(thistuple[1])"""

#80
#Negative indexing means start from the end.
#-1 refers to the last item, -2 refers to the second last item etc.
#Example
#Print the last item of the tuple:

"""thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])"""

#81
#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new tuple with the specified items.
#Example
#Return the third, fourth, and fifth item:

"""thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])"""

#82
#By leaving out the start value, the range will start at the first item:
#Example
#This example returns the items from the beginning to, but NOT included, "kiwi":

"""thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])"""

#83
#By leaving out the end value, the range will go on to the end of the tuple:
#Example
#This example returns the items from "cherry" and to the end:

"""thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])"""

#84
#This example returns the items from index -4 (included) to index -1 (excluded)

"""thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])"""

#85
#To determine if a specified item is present in a tuple use the in keyword:
#Example
#Check if "apple" is present in the tuple:

"""thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")"""

#86
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
#Example
#Convert the tuple into a list to be able to change it:

"""x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)"""

#87
#Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
#1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
#Example
#Convert the tuple into a list, add "orange", and convert it back into a tuple:

"""thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)"""

#88
#2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
#Example
#Create a new tuple with the value "orange", and add that tuple:

"""thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)"""

#89
#Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
#Example
#Convert the tuple into a list, remove "apple", and convert it back into a tuple:

"""thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)"""

#90
#The del keyword can delete the tuple completely:

"""thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists"""

#91
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
#Example
#Packing a tuple:

"""fruits = ("apple", "banana", "cherry")
print(fruits)"""

#92
#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
#Example
#Unpacking a tuple:

"""fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)"""

#93
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
#Example
#Assign the rest of the values as a list called "red":

"""fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)"""

#94
#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
#Example
#Add a list of values the "tropic" variable:

"""fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)"""

#95
#You can loop through the tuple items by using a for loop.
#Example
#Iterate through the items and print the values:

"""thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)"""

#96
#You can also loop through the tuple items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
#Example
#Print all items by referring to their index number:

"""thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])"""

#97
#You can loop through the tuple items by using a while loop.
#Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.
#Remember to increase the index by 1 after each iteration.
#Example
#Print all items, using a while loop to go through all the index numbers:

"""thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1"""

#98
#To join two or more tuples you can use the + operator:
#Example
#Join two tuples:

"""tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)"""

#99
#If you want to multiply the content of a tuple a given number of times, you can use the * operator:
#Example
#Multiply the fruits tuple by 2:

"""fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)"""

#100
#Sets are written with curly brackets.
#Example
#Create a Set:

"""thisset = {"apple", "banana", "cherry"}
print(thisset)"""

#101
#Sets cannot have two items with the same value.
#Example
#Duplicate values will be ignored:

"""thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)"""

#102
#True and 1 is considered the same value:

"""thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)"""

#103
#False and 0 is considered the same value:

"""thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)"""

#104
#To determine how many items a set has, use the len() function.
#Example
#Get the number of items in a set:

"""thisset = {"apple", "banana", "cherry"}
print(len(thisset))"""

#105
#Set items can be of any data type:
#Example
#String, int and boolean data types:

"""set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)"""

#106
#A set with strings, integers and boolean values:

"""set1 = {"abc", 34, True, 40, "male"}
print(set1)"""

#107
#From Python's perspective, sets are defined as objects with the data type 'set':
#<class 'set'>
#Example
#What is the data type of a set?

"""myset = {"apple", "banana", "cherry"}
print(type(myset))"""

#108
#It is also possible to use the set() constructor to make a set.
#Example
#Using the set() constructor to make a set:

"""thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)"""

#109
#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
#Example
#Loop through the set, and print the values:

"""thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)"""

#110
#Check if "banana" is present in the set:

"""thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)"""

#111
#To add one item to a set use the add() method.
#Example
#Add an item to a set, using the add() method:

"""thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)"""

#112
#To add items from another set into the current set, use the update() method.
#Example
#Add elements from tropical into thisset:

"""thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)"""

#113
#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
#Example
#Add elements of a list to at set:

"""thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)"""

#114
#To remove an item in a set, use the remove(), or the discard() method.
#Example
#Remove "banana" by using the remove() method:

"""thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)"""

#115
#Remove "banana" by using the discard() method:

"""thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)"""

#116
#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
#The return value of the pop() method is the removed item.
#Example
#Remove a random item by using the pop() method:

"""thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)"""

#117
#The clear() method empties the set:

"""thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)"""

#118
#The del keyword will delete the set completely:

"""thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)"""

#119
#Loop through the set, and print the values:

"""thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)"""

#120
#There are several ways to join two or more sets in Python.
#You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
#Example
#The union() method returns a new set with all items from both sets:

"""set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)"""

#121
#The update() method inserts the items in set2 into set1:

"""set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)"""

#122
#The intersection_update() method will keep only the items that are present in both sets.
#Example
#Keep the items that exist in both set x, and set y:

"""x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)"""

#123
#The intersection() method will return a new set, that only contains the items that are present in both sets.
#Example
#Return a set that contains the items that exist in both set x, and set y:

"""x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)"""

#124
#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
#Example
#Keep the items that are not present in both sets:

"""x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)"""

#125
#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
#Example
#Return a set that contains all items from both sets, except items that are present in both:

"""x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)"""

#126
#True and 1 is considered the same value:

"""x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)"""

#127
#Dictionaries are written with curly brackets, and have keys and values:
#Example
#Create and print a dictionary:

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)"""

#128
#Dictionary items are ordered, changeable, and does not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
#Example
#Print the "brand" value of the dictionary:

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])"""

#129
#Dictionaries cannot have two items with the same key:
#Example
#Duplicate values will overwrite existing values:

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)"""

#130
#To determine how many items a dictionary has, use the len() function:
#Example
#Print the number of items in the dictionary:

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))"""

#131
#The values in dictionary items can be of any data type:
#Example
#String, int, boolean, and list data types:

"""thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)"""

#132
#From Python's perspective, dictionaries are defined as objects with the data type 'dict':
#<class 'dict'>
#Example
#Print the data type of a dictionary:

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))"""

#133
#It is also possible to use the dict() constructor to make a dictionary.
#Example
#Using the dict() method to make a dictionary:

"""thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)"""

#134
#You can access the items of a dictionary by referring to its key name, inside square brackets:
#Example
#Get the value of the "model" key:

"""thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)"""

#135
#There is also a method called get() that will give you the same result:
#Example
#Get the value of the "model" key:

"""thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)"""

#136
#The keys() method will return a list of all the keys in the dictionary.
#Example
#Get a list of the keys:

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)"""

#137
#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
#Example
#Add a new item to the original dictionary, and see that the keys list gets updated as well:

"""car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change"""

#138
#The values() method will return a list of all the values in the dictionary.
#Example
#Get a list of the values:

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)"""

#139
#The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
#Example
#Make a change in the original dictionary, and see that the values list gets updated as well:

"""car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change"""

#140
#Add a new item to the original dictionary, and see that the values list gets updated as well:

"""car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change"""

#141
#The items() method will return each item in a dictionary, as tuples in a list.
#Example
#Get a list of the key:value pairs

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)"""

#142
#Make a change in the original dictionary, and see that the items list gets updated as well:

"""car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change"""

#143
#Add a new item to the original dictionary, and see that the items list gets updated as well:

"""car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change"""

#144
#To determine if a specified key is present in a dictionary use the in keyword:
#Example
#Check if "model" is present in the dictionary:

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")"""

#145
#You can change the value of a specific item by referring to its key name:
#Example
#Change the "year" to 2018:

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018"""

#146
#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.
#Example
#Update the "year" of the car by using the update() method:

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)"""

#147
#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
#Example

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)"""

#148
#The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
#The argument must be a dictionary, or an iterable object with key:value pairs.
#Example
#Add a color item to the dictionary by using the update() method:

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)"""

#149
#The pop() method removes the item with the specified key name:

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)"""

#150
#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)"""

#151
#The del keyword removes the item with the specified key name:

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)"""

#152
#The clear() method empties the dictionary:

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)"""

#153
#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
#There are ways to make a copy, one way is to use the built-in Dictionary method copy().
#ExampleGet your own Python Server
#Make a copy of a dictionary with the copy() method:

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)"""

#154
#Another way to make a copy is to use the built-in function dict().
#Example
#Make a copy of a dictionary with the dict() function:

"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)"""

#155
#Nested Dictionaries
#A dictionary can contain dictionaries, this is called nested dictionaries.
#Example
#Create a dictionary that contain three dictionaries:

"""myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
"""

#156
#Or, if you want to add three dictionaries into a new dictionary:
#Example
#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

"""child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)"""

#157
#To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
#Example
#Print the name of child 2:

"""myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])"""

#158
#Python supports the usual logical conditions from mathematics:
#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b
#These conditions can be used in several ways, most commonly in "if statements" and loops.
#An "if statement" is written by using the if keyword.
#Example
#If statement:

"""a = 33
b = 200
if b > a:
  print("b is greater than a")"""

#159
#Elif
#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
#Example

"""a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")"""

#160
#Else
#The else keyword catches anything which isn't caught by the preceding conditions.
#Example

"""a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")"""

#161
#In this example a is greater than b, so the first condition is not true, also the elif condition is not true, so we go to the else condition and print to screen that "a is greater than b".
#You can also have an else without the elif:
#Example

"""a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")"""

#162
#Short Hand If
#If you have only one statement to execute, you can put it on the same line as the if statement.

"""a = 200
b = 33
if a > b: print("a is greater than b")"""

#163
#Short Hand If ... Else
#If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
#Example
#One line if else statement:

"""a = 2
b = 330
print("A") if a > b else print("B")"""

#164
#You can also have multiple else statements on the same line:
#Example
#One line if else statement, with 3 conditions:

"""a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")"""

#165
#AND
#The and keyword is a logical operator, and is used to combine conditional statements:
#Example
#Test if a is greater than b, AND if c is greater than a:

"""a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")"""

#166
#OR
#The or keyword is a logical operator, and is used to combine conditional statements:
#Example
#Test if a is greater than b, OR if a is greater than c:

"""a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")"""

#167
#NOT
#The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
#Example
#Test if a is NOT greater than b:

"""a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")"""

#168
#Nested If
#You can have if statements inside if statements, this is called nested if statements.
#Example

"""x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")"""

#169
#The pass Statement
#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
#Example

a = 33
b = 200
if b > a:
  pass

#170
#The while Loop
#With the while loop we can execute a set of statements as long as a condition is true.
#Example
#Print i as long as i is less than 6:

"""i = 1
while i < 6:
  print(i)
  i += 1"""

#171
#The break Statement
#With the break statement we can stop the loop even if the while condition is true:
#Example
#Exit the loop when i is 3:

"""i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1"""

#172
#The continue Statement
#With the continue statement we can stop the current iteration, and continue with the next:
#Example
#Continue to the next iteration if i is 3:

"""i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)"""

#173
#The else Statement
#With the else statement we can run a block of code once when the condition no longer is true:
#Example
#Print a message once the condition is false:

"""i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")"""

#174
#Python For Loops
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
#Example
#Print each fruit in a fruit list:

"""fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)"""

#175
#Looping Through a String
#Even strings are iterable objects, they contain a sequence of characters:
#Example
#Loop through the letters in the word "banana":

"""for x in "banana":
  print(x)"""

#176
#The break Statement
#With the break statement we can stop the loop before it has looped through all the items:
#Example
#Exit the loop when x is "banana":

"""fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break"""

#177
#Example
#Exit the loop when x is "banana", but this time the break comes before the print:

"""fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)"""

#178
#The continue Statement
#With the continue statement we can stop the current iteration of the loop, and continue with the next:
#Example
#Do not print banana:

"""fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)"""

#179
#The range() Function
#To loop through a set of code a specified number of times, we can use the range() function,
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

#Example
#Using the range() function:

"""for x in range(6):
  print(x)"""

#180
#The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
#Example
#Using the start parameter:

"""for x in range(2, 6):
  print(x)"""

#181
#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
#Example
#Increment the sequence with 3 (default is 1):

"""for x in range(2, 30, 3):
  print(x)"""

#182
#Else in For Loop
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
#Example
#Print all numbers from 0 to 5, and print a message when the loop has ended:

"""for x in range(6):
  print(x)
else:
  print("Finally finished!")"""

#183
#Example
#Break the loop when x is 3, and see what happens with the else block:

"""for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")"""

#184
#A nested loop is a loop inside a loop.
#The "inner loop" will be executed one time for each iteration of the "outer loop":
#Example
#Print each adjective for every fruit:

"""adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)"""

#185
#The pass Statement
#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
#Example

"""for x in [0, 1, 2]:
  pass"""

#END.

