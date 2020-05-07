#ctrl + / will comment or uncomment block of code in pychrm
print ("hi")
print ("all")

string_1 = 'P'
string_2 = "\U00000050"
print(string_1)
print(string_2)

num_1 = 1.22
str_1 = str(num_1)
print(num_1)
print(type(num_1))
print(str_1)
print(type(str_1))
num_2 = int(num_1)
print(num_2)
print(type(num_2))

result = input("What's your name?")
print(result)
print(type(result))

str_2 = "\U0001f609"
print(str_2)

result_1 = input("how many cup of coffee did you have today?")
result_1 = int(result_1)
print(result_1)
print(type(result_1))

# string operations
# x in s
# x not in s
poem = "roses are red and violets are blue"
string_1 = "Roses"
str_result = string_1 in poem
print(str_result)

#string times integer to print the same string # of times and find out the length & type
str_res_1 = string_1 * 3
print(str_res_1)
print(len(str_res_1))
print(type(len(str_res_1)))

#count how many times substring is part of string
poem_2 = "today is sunny day it is a good day"
string_2 = "day"
str_2_len = len(poem_2)
print(str_2_len)
str_2_res = poem_2.count(string_2)
print(str_2_res)
print(type(str_2_res))
str_2_type = str(str_2_res)
print(str_2_type)
print(type(str_2_type))
str_2_in_res = str(str_2_res) not in str_2_type
print(str_2_in_res)

#ctrl + / together to comment in window
poem_3 = "twinkel twinkel little stars"
print(poem_3)

#string concatenation = join two string in to make one string
str_3 = "i"
str_4 = "like"
str_5 = "python"
full_str = str_3 + " " + str_4 + " " + str_5

fname = 'dimple'
lname = 'patel'
fullname = fname +" "+lname
print(fullname)

fulline = "I am " + fullname + " and " + full_str
print(fulline)

#backsalsh before letter - \n is a new line within quotes
str_6 = "\n i also like \"harry potter\" books"
print(str_6)

big_line = fulline + str_6
print(big_line)

#formatting an existing string with f'{add the formatted part}
str_7 = "Washington"
str_8 = f'{str_7} state is beautiful'
print(str_8)

str_9 = "new york"
str_11 = "but small"
str_10 = f"{str_9} is an IT hub \n" + str_11
print (str_10)

str_12 = "i dont like"
str_13 = 'snakes {}'.format(str_12)
print(str_13)

str_14 = "texas state"
str_result = str_14.capitalize()
print(str_result)

str_15 = "new jersey"
str_result_2 = str_15.upper()
print(str_result_2)

str_16 = "WE ARE A FAMILY"
str_result_3 = str_16.lower()
print(str_result_3)

print ('hello this is our first program. we will covert miles to km')
str_17 = "today"
miles = input("how many miles did you run?")
print ("great " + miles + " miles {}".format(str_17) + "!")
#1 mile = 1.6 km
km = float(miles) * 1.6
print(f'you have run {km} kilometers')


