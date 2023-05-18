#list comprehension with numbers

numbers =[1,2,3]

new_numbers =[n+1 for n in numbers]
print(new_numbers)

#list comprehension with letters

name = "Carlos"
new_name=[letter for letter in name]

print(new_name)

# this creates a list comprehension without the initial list.
range_list = [num*2 for num in range(1,6)]
print(range_list)

# you can use it in strings

names =['Alex','Bethany','Caroline','Dave','Eleanor','Freddy.']

short_names = [i[0:3] for i in names]

print(short_names)

# you can use it with conditionals

names_1 =['Alex','Beth','Caroline','Dave','Eleanor','Freddy.']

short_names_1 = [i for i in names_1 if len(i)<5]

print(short_names_1)

# you can use it with methods

names_2 =['Alex','Beth','Caroline','Dave','Eleanor','Freddy.']

short_names_2 = [i.upper() for i in names_2]

print(short_names_2)

# Squared numbers

numbers = [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]

squared_numbers = [i*i for i in numbers]

print(squared_numbers)

#Even and Odds

numbers=[1,1,2,3,5,8,13,21,34,55]

result = [i for i in numbers if i%2==0]

print(result)