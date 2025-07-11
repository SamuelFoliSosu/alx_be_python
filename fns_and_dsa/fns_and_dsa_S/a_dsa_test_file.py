#list
my_list = [1, 2, "three", 4.0, False, 15, 2, 1, 2, "three", 4.0, False, 4.1, False, 2]
print(f"{type(my_list)} of lenght {len(my_list)} = {my_list}")

my_list_slice = my_list[::3]
print(my_list_slice)

#tuple
my_tuple = (4, 5, "six", 7.0, True, "six", 80, "gate")
print(f"{type(my_tuple)} of lenght {len(my_tuple)} = {my_tuple}")

#set
# my_set = {9, 10, "eleven", None, 13.0, 9, 9, "eleven"}
my_set = set(my_tuple)
print(f"{type(my_set)} of lenght {len(my_set)} = {my_set}")

#dictionary