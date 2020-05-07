print("sum of two numbers and type of sum")
num_1 = 7
num_2 = 5
print(num_1 + num_2)
print(type(num_2))

print("sum of two numbers and type of sum")
num_2 = 10
print(num_2)
result = num_1 + num_2
print(result)
print(type(result))

print("sum of two numbers (one negative number) and type of sum")
num_3 = 2
print(num_3)
num_4 = -2
result_1 = num_3 - num_4
print(result_1)
print(num_4)

print("multiplication of float numbers")
num_5: float = .2
num_6 = 1.2
result_2 = num_5 * num_6
print(result_2)

num_7 = 5
num_8 = 2
result_3 = num_7 / num_8
print(result_3)
result_4 = num_7 // num_8
print(result_4)
result_5 = num_7 % num_8
print(result_5)

num_9 = 2
num_10 = 3
result_6 = -(num_9 ** num_10)
print(result_6)

num_11 = -3
result_7 = -num_11
print(result_7)

num_12 = 33333
num_13 = 22
result_8 = num_12 / num_13
print(result_8)
result_9 = round(result_8, 3)
print(result_9)
result_10 = round(result_9)
print(result_10)

import math
num_14 = 123.56989
result_11 = math.floor(num_14)
print(result_11)

num_12 = 33333
num_13 = 22
result_8 = num_12 / num_13
print(result_8)
result_12 = math.floor(result_8)
print(result_12)

result_13 = math.ceil(result_8)
print(result_13)

# how to use round, floor and ceil
num_15 = 8.991233
print(round(num_15,3))
print(math.floor(num_15))
print(math.ceil(num_15))

# how to use round, floor and ceil
num_num = 0.0111000
print(round(num_num, 4))
print(math.floor(num_num))
print(math.ceil(num_num))

# find out the type and change the type to integer
type_num15 = type(num_15)
print(type_num15)
print(num_15)
int_1 = int(num_15)
print(type(int_1))
print(int_1)

num_16 = 4
result_float = float(num_16)
print (result_float)