### Day 1 Assignement 


""""
1. The list in Python is ordered collection of elemnets . It is mutable which means its values can be changed . They are written using sqaure brackets.It can hold both duplicate values and mixed values also . Example :- fruits = ['guava', 'banana', 'papaya']

2. The tuple in Python is also ordered collection of elements . It is immutable which means its values cannot be changed . They are written using the enclosed paranthesis.  Example :- my_profile = ('Mayank', '29', 'True')

3. Tuple :- Immutable , Ordered ,  Duplicates are allowed , Enclosed by () , Less Functional , Uses less memory due to immutability , Faster in nature as compared to list
   List :- Mutable, Ordered , Duplicates are allowed , Enclosed by [] , More Functional , Uses more memory due to mutablity , Slower in nature as compared  to tuple .
""""

### 4. Program to find the largest element in the list.
def find_largest_elements(list):
    if not list:
        return "List is empty"
    return max(list)
num = [12 , 14, 15, 17, 19]
print(" The largest elements is: ", find_largest_elements(num))

### 5. Program to interchange first and last elements in a list.
def inter_first_last(list):
    if len(list)>= 2:
        list[0] , list[-1] = list[-1] , list[0]
    return list
num = [12 , 14 , 15 , 17 , 19]
print("Number before interchange", num)
print("Number after interchange", inter_first_last(num))

###6. Program to swap two elements in a list
def swap_two(lst, one , two):
    if 0 <= one < len(lst) and 0 <= two < len(lst):
        lst[one], lst[two] = lst[two] , lst[one]
    else:
        print("One or both position are out of index")
    return lst
num = [12 , 14 , 15 , 17 , 19]
print("Number before swap", num)
print("Number after swap", swap_two(num, 1, 3))

###7. Program to Reverse a List
def rev_lst(lst):
    if len(lst) == 0:
        print("List is empty")
    else:
        return list(reversed(lst))
num = [12 , 14 , 15 , 17 , 19]
print("Number before reverse", num)
print("Number after reverse", rev_lst(num))

###8. Program to count occurrences of an element in a list
def count_occur(lst, elmnt):
    if len(lst) == 0:
        print("List is empty")
    else:
        return lst.count(elmnt)
num = [12 , 14 , 15 , 17 , 19, 12]
print("Occurence of 12 in this list is ", count_occur(num, 12))

###9. Program to find the sum of elements in the list
def sum_list(lst):
    if len(lst) == 0:
        print("List is empty")
    else:
        return sum(lst)
num = [12 , 14 , 15 , 17 , 19, 12]
print("Sum of the numbers in this list is  ", sum_list(num))

###10. Program to Multiply all numbers in the list
import math
def mul_list(lst):
    if len(lst) == 0:
        print("List is empty")
    else:
        return math.prod(lst)
num = [12 , 14 , 15 , 17 , 19, 12]
print("Sum of the numbers in this list is  ", mul_list(num))


###11. What are the ways to find the length of a list?
"""
1. Built in Function way len()
2. The Custom Functional way using loop.
3. Internal Object way of using __len__()
4. Functional way of using sum() and a list Comprehension
"""

### 12. Program to find the smallest and largest number in a list (Without min-max function
def find_extreme(lst):
    if not lst:
        return None, None
    smallest = lst[0]
    largest = lst[0]

    for num in lst[1:]:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    return smallest , largest

num = [12 , 14 , 15 , 17 , 19, 12]
print("Smallest and largest in this list is ", find_extreme(num))

###13. Program to find the area of a circle
import math

def cal_area_cicle(radius):
    area = math.pi * (radius **2)
    return area 

radius = 3 
area = cal_area_cicle(3)
print("The area of circle of radius 3 is ", area)

###14. Take inputs from the user to make a list. Again take one input from the user and delete that element from a list.
inputs = int(input("Enter the number of elements:"))

lst = []

for i in range(inputs):
    elements = input("Enter elements: ")
    lst.append(elements)

elements = input("Enter the element to delete: ")
if elements in lst:
    lst.remove(elements)
    print("Updated list", lst)
else:
    print("Elements not found")


###15. You are given a list of integer elements. Make a new list that will store a square of elements
###of the previous list. (With and without list comprehension)
###● Input_list = [2,5,6,12]
###● Output_list = [4,25,36,144]

input_list = [2,5,6,12]
output_list = []

for element in input_list:
    output_list.append(element **2)

print("Input List: ", input_list)
print("Output List: ", output_list)


####16. WAP to create two lists, one containing all even numbers and the other containing all odd numbers between 0 to 151.
even = []
odd = []

for i in range(151):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even Numbers: ", even)
print("Odd Numbers: ", odd)

####18. WAP to make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7, and 9 in separate lists for range(0,151)
divisors = [4,6,8,10,3,5,7,9]

lists = []
for divisor in divisors:
    new_lst = [num for num in range(151) if num % divisor == 0]
    lists.append(new_lst)
for i in range(len(divisors)):
    print("Divisible by", divisors[i]," :" , lists[i])

"""
####20.What’s The Difference Between The Python append() and extend() Methods?
append() => The append() method adds one element at the end of a list. If we append another list , the entire list is added as single elements.
    Example :- lst = [1,2,3]
               lst.append([4,5])
               print(lst)
extend() => The extend() method adds each element of another list or iterable to the existing list.
    Example :- lst = [1,2,3]
               lst.extend([4,5])
               print(lst)
"""

####21.Write a Python program to append a list to the second list
lst1 = [1,2,3]
lst2 = [4,5,6]

lst2.append(lst1)
print("First list:", lst1)
print("Second List:", lst2)

####22.Write a Python program to find the third-largest number in a list
num = [10,25,8,45,32,18,50]

num.sort()
print("Third-largest number:", num[-3])


####23.Write a Python program to check whether a list contains a sublist
lst = [1,2,3,4,5,6]
sublst = [3,4,7]

result = True 
for x in sublst:
    if x not in lst:
        result = False
        break
if result:
    print("List contains the sublist")
else:
    print("List does not contains the sublist")

####25.Write a Python program to find common items from two lists
lst1 = [1,2,3,4,5,6]
lst2 = [4,5,6,7,8]

common = []

for item in lst1:
    if item in lst2:
        common.append(item)

print("Common Items:", common)

####26.How to flatten a list in Python?
#Flattening refers to converting a nested list into the single list
#For example:- [[1,2],[3,4],[5,6]]
#After doing flatten 
           #:- [1,2,3,4,5,6]

lst = [[1,2],[3,4],[5,6]]
flat_lst = []
for sublst in lst:
    for item in sublst:
        flat_lst.append(item)

print("Flatten List:", flat_lst)


####27.How to sort a list in ascending and descending order without using the sort function?
numbers = [5,2,8,9,3]
# Ascending order
for i in range(len(numbers)):
    for j in range(len(numbers)-1):
        if numbers[j]> numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("Ascending Order:", numbers)

# Descending order
for i in range(len(numbers)):
    for j in range(len(numbers)-1):
        if numbers[j]< numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("Descending Order:", numbers)



####28.How to sort a tuple?
### Tuple is immutable we cannot directly modify it . We can use the sorted(() function , which returns news list containing the sorted elements.

numbers = (5,2,8,1,9,3)
sorted_tuple = tuple(sorted(numbers))
print("original tuple", numbers)
print("new tuple", sorted_tuple)


sorted_tuple = tuple(sorted(numbers, reverse=True))
print("original tuple", numbers)
print("new tuple", sorted_tuple)

####29.Write a Python program to convert a list of multiple integers into a single integer
numbers = [1,2,3,4,5,6,7]
res = ""
for num in numbers:
    res = res + str(num)
res = int(res)

print("Single integer", res)

####30.What is the difference between del and clear?
#Both are used to remove elements from the list 
#del it can delete the particular element , a range of element or the entire list
num = [1,2,3,4,5,6]
del num[1]
print(num)
del num

#clear() method removes all elements from the list , but the list will still exists.
num = [1,2,4,5,6]
num.clear()
print(num)

####31.What is the difference between remove and pop?
# Both remove() and pop() are used to delete elements from a list , but they work differently 
#remove() methods delete an element by its value
numbers = [10,20,30,40]
numbers.remove(30)
print(numbers)

#The pop() method deletes an element by its index and returns the removed elements
numbers = [10,20,30,40]
x = numbers.pop(2)
print(numbers)
print("Removed :", x)

####32. Difference between Indexing and Slicing 
# Both Indexing and slicing are used to access elements from a list 
# Indexing used to access a single element from a list
numbers = [10,20,30,40,50]
print(numbers[2])

#Slicing is used to accesss multiple elements from a list
numbers = [10,20,30,40,50]
print(numbers[1:4])

####33. Difference between sort() and sorted()
#Both sort() and sorted() are used to arrange elements in ascending and descending order 
# sort() is used with a list and changes the original list
numbers = [20,30,40,50,60]
numbers.sort()
print(numbers)

#sorted() function creates sorted list and does not change the original list

numbers = [10,20,30,40,50,60]
new = sorted(numbers)
print("Original List:", numbers)
print("Sorted List:", new)

####34. Difference between reverse() and reversed()
# Both are used to reverse the order of elements 
# reverse() is used with a list and it change the original list
numbers = [10,20,30,40,50]
numbers.reverse()
print(numbers)

#reversed() function returns reverse iterator without changing the original list
numbers = [10,20,30,40,50,60]
new_list = list(reversed(numbers))
print("Original List:", numbers)
print("Sorted List:", new_list)

####35.Difference between copy() and Deep Copy

# Copy() method creates a shallow copy which means nested objects are still shared
import copy 
list1 = [[1,2],[3,4]]
list2 = list1.copy()

list2[0][0] = 100

print("Original list:", list1)
print("Copied List:", list2)

#Deep Copy creates a completely independent copy inclding all nested objects
import copy 
list1 = [[1,2],[3,4]]
list2 = copy.deepcopy(list1)

list2[0][0] = 100

print("Original List", list1)
print("Copied List", list2)


####36. How to check whether a list is empty for not 
numbers = []
if not numbers:
    print("List is empty")
else:
    print("List is not empty")


####37. How to Concatenate two list?
list1 = [1,2,3]
list2 = [4,5,6]

list3 = list1 + list2

print("First List:",list1)
print("Second List:", list2)
print("Concatenated List:", list3)

####39. Reverse Elements within each tuple
def reverse_tuple(tuples):
    result = []
    for t in tuples:
        result.append(t[::-1])
    return result

tuples = [(1,2),(3,4),(4,5),(5,6)]
print("Output:", reverse_tuple(tuples))


####40. Add Coresponding Elements of Tuples
def add_tuples(list1,list2):
    results = []
    for t1 , t2 in zip(list1,list2):
        results.append((t1[0] + t2[0], t1[1] + t2[1]))
    return results

list1 = [(1,2) , (3,4)]
list2 = [(5,6) , (7,8)]
print("Output:", add_tuples(list1, list2))