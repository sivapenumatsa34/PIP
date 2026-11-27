# # # # list methods
 
# # # # 1. append() - Add one element
# # # numbers = [10, 20, 30, 40]
# # # numbers.append(50)
# # # print("1. Append:", numbers)
 
# # # # 2. extend() - Add multiple elements
# # # numbers.extend([60, 70])
# # # print("2. Extend:", numbers)
 
# # # # 3. insert() - Insert at a specific index
# # # numbers.insert(2, 25)
# # # print("3. Insert:", numbers)
 
# # # # 4. remove() - Remove a specific value
# # # numbers.remove(30)
# # # print("4. Remove:", numbers)
 
# # # # 5. pop() - Remove an element by index
# # # numbers.pop(1)
# # # print("5. Pop:", numbers)
 
# # # # 6. index() - Find the index of an element
# # # print("6. Index:", numbers.index(40))
 
# # # # 7. count() - Count occurrences of an element
# # # numbers.append(40)
# # # print("7. Count:", numbers.count(40))
 
# # # # 8. sort() - Sort in ascending order
# # # numbers.sort()
# # # print("8. Sort:", numbers)
 
# # # # 9. reverse() - Reverse the list
# # # numbers.reverse()
# # # print("9. Reverse:", numbers)
 
# # # # 10. copy() - Copy the list
# # # new_numbers = numbers.copy()
# # # print("10. Copy:", new_numbers)
 
# # # # 11. clear() - Remove all elements
# # # numbers.clear()
# # # print("11. Clear:", numbers)
 
 
 
 
 
# # # # tuple methods
 
 
# # # # Creating a tuple
# # # numbers = (10, 20, 30, 20, 40, 20)
 
# # # # 1. count() - Count occurrences of an element
# # # print("1. Count:", numbers.count(20))
 
# # # # 2. index() - Find the index of an element
# # # print("2. Index:", numbers.index(30))
 
# # # # Other useful tuple operations
 
# # # # 3. len() - Find the length
# # # print("3. Length:", len(numbers))
 
# # # # 4. max() - Find the maximum value
# # # print("4. Maximum:", max(numbers))
 
# # # # 5. min() - Find the minimum value
# # # print("5. Minimum:", min(numbers))
 
# # # # 6. sum() - Calculate the total
# # # print("6. Sum:", sum(numbers))
 
# # # # 7. sorted() - Sort the tuple elements
# # # print("7. Sorted:", sorted(numbers))
 
# # # # 8. Reversing using slicing
# # # print("8. Reverse:", numbers[::-1])
 
# # # # 9. Convert tuple into list
# # # new_list = list(numbers)
# # # print("9. Tuple to List:", new_list)
 
# # # # 10. Convert list into tuple
# # # new_tuple = tuple(new_list)
# # # print("10. List to Tuple:", new_tuple)
 
# # # # 11. Check whether an element exists
# # # print("11. Check 30:", 30 in numbers)
 
 
 
 
 
# # # # ------------------------------------------
 
 
# # # # Slicing in Python
 
 
# # # numbers = [10, 20, 30, 40, 50, 60, 70]
 
# # # print(numbers[1:4])
# # # print(numbers[:3])
# # # print(numbers[3:])
# # # print(numbers[-3:])
# # # print(numbers[:-2])
# # # print(numbers[::2])
# # # print(numbers[::3])
# # # print(numbers[::-1])
# # # print(numbers[:])
# # # print(numbers[4:1:-1])

# # l1=[10, 20, 30, 40, 50]
# # max=0
# # # sum=0
# # # for i in l1:
# # #     sum = i+sum
# # # print("Sum of list elements:", sum)
# # # largest
# # # print(max(l1))
# # for i in l1:
# #     if max < i:
# #         max = i
# # print("Largest element in the list:", max)

# ##Dictionaries
# # candidate = {"name": "Siva", "score": 72}

# # print(candidate["name"])      

# # candidate["score"] = 80       
# # candidate["city"] = "Vizag"   

# # print(candidate.get("email", "Missing"))

# scores = {"Siva": 72, "Adithya": 48, "Ravi": 90}

# for name,score in scores.items():
#     if score >= 50:
# #         print(name, "has passed with score:", score)

# student = {"name": "Siva", "age": 25, "marks": 80}
# print(student["name"])
# student["marks"] = 30
# print(student["marks"])
# student["city"]="hyderabad"
# print(student)
# print("age" in student)
# print(len(student))
# del student["age"]
# print(student)
# for key,value in student.items():
#     print(key, ":", value)

#sets
set_a={1, 2, 3, 4, 5}
 
set_a.add(6)              
set_a.remove(3)           
print(set_a)
 
b={4, 5, 6, 7, 8}
print(set_a.union(b))      
print(set_a.intersection(b)) 
print(set_a.difference(b))   
print(set_a.symmetric_difference(b)) 
 
 
c={1, 2, 3, 4, 5}
print("c = " , c)
 
c.discard(3)  # discard element
print(c)
 
 
numbers = {10, 20, 30, 40} #clearing all elements from the set
numbers.clear()
 
print(numbers)
 
 
numbers_1 = {10, 20, 30} #copying all elements from the set
 
new_numbers = numbers_1.copy()
 
print(new_numbers)