weather = input("how's the weather today?")
print("you entered that weather is", weather, 'today')
if weather == "sunny":
    print("have a nice day")
elif weather == "rainy":
    print("take an umbrella")
elif weather == "cold":
    print("put on a jacket")
else:
    print("stay at home")

x = int(input("enter a number"))
if x < 10:
    print("x is less than 10")
elif 10 <= x <= 15:
    print("x is less than or equal to 15 ")
else:
    print("x is greater than 15")

"apple" > "banana"
"banana" > "apple"
"apple" != "banana"
"Apple" == "apple"
"string1" != "string2"

var_1 = int(input("enter var_1 value"))
var_2 = int(input("enter var_2 value"))
if var_1 > var_2:
    print('var_1 is greater')
elif var_1 < var_2:
    print("var_2 is greater")
else:
    print("both var_1 and var_2 are same")

var_3 = 1
var_4 = False
if var_3 == int(var_4):
    print('true')
else:
    print("false")
print(type(var_3))
print(type(var_4))
print(int(var_4))

var_5 = "true"
var_6 = str(True)
#var_7 = True
#print(var_7)
#print(var_6)
if var_5 == var_6:
    print("true")
else:
    print("false")

var_6 = str(True)
var_7 = True
var_7 != var_6
#print(var_7)
#print(var_6)

x = None
#x = input("enter the value of x")
if x:
    print("true")
else:
    print('false')

x = ("so")
y = ()

if x != () and y != ():
    print ("x and y are not null")
elif x == () and y == ():
    print("x and y are null")
else:
    print("either x or y is null")



