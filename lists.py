#empty list
my_list = [ ]
print(my_list)

my_list.append(10)
my_list.append(20)
my_list.append(40)
my_list.append(30)
print(my_list)

#inserting
my_list[1] = 15
print(my_list)

#extending
my_list_2 = [50, 60, 70]
my_list.extend(my_list_2)
print(my_list)

#removing
del my_list[6]
print(my_list)

#sorting
my_list.sort()
print(my_list)

#element index
print(my_list.index(30))
