my_set = {1, 2, 3, 4}
my_set_2 = {3, 4, 5, 6}
print(my_set.union( my_set | my_set_2)
print(my_set & my_set_2)
print(my_set - my_set_2)
print(my_set ^ my_set_2)
my_set.clear()
print(my_set)