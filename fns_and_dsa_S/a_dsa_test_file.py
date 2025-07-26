import random

# Practice Exercises
# Exercise 1: Write a function to greet the user by name.
# Instructions:
# Define a function called that takes one parameter, (name).
# Inside the function, create a greeting message that includes the name passed as an argument.
# Print the greeting message using the print function.
def greeting(name):
    # name = input("Please enter your name: ")
    # print(f"Your name is {name}.")
    return "Your name is " + name

print(greeting("John"))

# Exercise 2: Create a function to calculate the area of a rectangle.
# Instructions:
# Define a function that takes two parameters, length and width.
# Inside the function, multiply the length and width to calculate the area.
# Use the return statement to return the calculated area.
def area_of_a_rectangle(length, width):
    area = length * width
    return (area)

print("Area of rectangle is" , area_of_a_rectangle(2,5))

# Exercise 3: Develop a function to check if a number is even or odd.
# Instructions:
# Define a function that takes one parameter, number.
# Inside the function,check the remainder after dividing the number by 2 is equal to zero.
# If the remainder is zero, the number is even. Print a message indicating the number is even.
# If the remainder is not zero, the number is odd. Print a message indicating the number is odd.
def even_or_odd(number):
    check = number % 2

    if check == 0:
        return "Your number is even"
    else:
        return "Your number is odd"

print(even_or_odd(12))

count = 2  # Global variable
def increment():
    global count
    count += 1  # This refers to the local count within the function
    print(count,"function count, Local")
increment()
print(count)  # Output: 0 (Global count remains unchanged)

#list
my_list = [1, 2, "three", 4.0, False, 15, 2, 1, 2, "three", 4.0, False, 4.1, False, 2]
print(f"{type(my_list)} of lenght {len(my_list)} = {my_list}")

my_list_slice = my_list[::3]
print(my_list_slice)

#tuple
my_tuple = (4, 5, "six", 7.0, True, "six", 80, "gate")
print(f"{type(my_tuple)} of lenght {len(my_tuple)} = {my_tuple}")

#set
my_set = {9, 10, "eleven", None, 13.0, 9, 9, "eleven"}
# my_set = set(my_tuple)
print(f"{type(my_set)} of lenght {len(my_set)} = {my_set}")

#dictionary
my_dict = {"Ama" : 12, "Kojo" : 25, "Kwame" : 45}
print(f"{type(my_dict)} of length {len(my_dict)} = {my_dict}")
# print(my_dict.keys())
# print(my_dict.items())
# print(my_dict.values())
print(my_dict.get("Kojo"))


# Practice Exercise
# Exercise 1: Create a list to store names of your favorite fruits. Write code to access the second element and print it.
my_fav_fruits = ["Apple", "Pineapple", "Grapes" , "Bananna"]
print(my_fav_fruits[1])

# Exercise 2: Define a dictionary to store information about your favorite book, including title, author, and genre. Use the method to retrieve the genre.
my_fav_book = {"title": "Who ate my cheese?" , "author" : "Someone" , "genre" : "Self-help"}
print(my_fav_book.get("genre"))

# Exercise 3: Write a program to generate a random set of numbers between 1 and ten. Use set operations to remove duplicates and display the unique numbers.
random_numbers = []
for n in range(10):
    # print(n)
    # random_numbers.append(n)
    random_numbers.append(random.randint(1,10))

print(random_numbers)

random_set = set(random_numbers)
print(random_set)