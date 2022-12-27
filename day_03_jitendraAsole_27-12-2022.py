#Lists

#Integer list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_list)

#String + integer list
string_list = [1 , 'Jitendra', 2, 3, 'Asole']
print(string_list)

my_list = [1 , 2, 'Jitendra', 3, 5, 6, 'Asole']
print(my_list)

print(len(my_list))

#Indexing and slicing

print(my_list[0])
print(my_list[1:])
print(my_list[1::2])

#List concatenation 

concatenated_list = my_list + ['Concatenated']

print(concatenated_list)

#Doubling the list 

double_list = my_list * 2

print(double_list)


# List append

new_list = [1, 20, 451, 45, 465, 12, 123, 122, 125]

new_list.append(626)

print(new_list)

new_list.append('Appened')

print(new_list)

# Pop off the index

new_list.pop(10)

print(new_list, 'popped the last string')

# Pop off without index. Take -1 as default input and pops last element

new_list.pop()

print(new_list, 'popped the last string without arg')


#Sort and reverse

alph_list = ['a', 'c', 'd', 'b', 'h', 'f', 'g', 'e']

print(alph_list)

alph_list.reverse()

print(alph_list)

#Nested list 

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

matrix = [list_1, list_2, list_3]

print(matrix)

print(matrix[0][0])
print(matrix[1][0])
print(matrix[2][0])

#Dictionary creation and access

my_dict = {'name': 'Jitendra', 'middle': 'Raju', 'last': 'Asole', 'place': 'Nagpur'}

print(my_dict['name'])
print(my_dict['last'])
print(my_dict['place'])

my_dict = {'name': 'Jitendra', 'middle': 'Raju', 'last': 'Asole', 'place': 'Nagpur', 'age': 21, 'worth': 15000}

print('My age is ',my_dict['age'])
print('My net worth is ',my_dict['worth'])