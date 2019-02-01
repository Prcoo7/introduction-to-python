# program no. 01
print(5**2)

#PROGRAM NO .02
print(4**0.5)

#PROGRAM NO. 03
print(4%3)

#PROGRAM NO. 04
print(abs(-5))

#PROGRAM NO .05
print(pow(5,4))

#PROGRAM NO. 06
print(max(3,4,5,66))

#PROGRAM NO. 07
print(min(3, 8, -0.4))

#PROGRAM NO. 08
print(round(2.9))
print(round(12.3))

#PROGRAM NO. 09
from math import*
print(sqrt(25))
# print(sqrt(-25)) gives value error

#PROGRAM NO. 10
from math import*
print(ceil(2.3))
print(ceil(2.7))
print(ceil(-3.5))
print(ceil(-3.2))
print(floor(4.8))
print(floor(-4.9))


#program on lists

#PROGRAM NO. 11 : ceating list and print it

friends = ["Roy", 'Nagamotiso', "Duke", "Anima"]

print(friends)


#PROGRAM NO. 12

friends = ["A", "B", "C", "D", "E"]

print(friends[0])       # [A]
print(friends[1])       # [B]
print(friends[-1])      # [E]
print(friends[-2])      # [D]
print(friends[1:])      # [B, C, D, E]
print(friends[:1])      # [A]
print(friends[:0])      # []
print(friends[-1:])     # [E]
print(friends[-2:])     # [D, E]
print(friends[:-1])     # [A, B, C, D]

print(friends[1:4])     # [B, C, D]
print(friends[-4:-1])   # [B, C, D,]



#program no . 13

item = ['m', 'n', 'o', 'p']
item.insert(0, 'l')
print(item)
item.remove('o')
print(item)


#program no. 14: Extension

#item = ['w', 'x', 'y', 'z']
#item.remove('w', 'x')
#print(item)
#gives a syntactical error



#program no 15: format specifiers

num = 2
real_num = 2.3
lf_num = 2.63987
name = "string"
character = 'c'

print("The format specifiers : %d, %f, %lf, %s, %c" %(num, real_num, lf_num, name, character))


#program no. 16: programm on tupples

coordiante = (4, 6, 8)

print(coordiante)
print(coordiante[0])

print(coordiante[1:])

coordiante2 = ()
cordinate2 = coordiante
print(coordiante2)

#program no. 17: string problem

string = "this is a string"

print(string[1])
print(string[1:])

#using functions

#program no. 18: function

def function(name):
    print('Hello ' + name + ' !')

function("mike")

#program no. 19
def cube(num):
    return (num**3)

num = int(input("Enter a number : "))

print(cube(num))


#program no. 20

def coffee(num):
    print("Hello")
    return num*num
result = coffee(3)
print(result)

# conditional program

#program no. 21

is_male = False
is_tall = True

if is_male and is_tall :
    print("you are male and tall")
elif not(is_male) and is_tall :
    print("you are not a male but you are tall")
elif is_male and not(is_tall) :
    print("you are a short male")
else :
    print("you are not male and not tall")


#program no. 22

num1 = float(input("Enter a no. : "))
op = input("Enter operator : ")
num2 = float(input("Enter another no. : "))

if op == "+":
    print("Addition of %f and %f is : %f" %(num1, num2, num1 + num2))
elif op == "-":
    print("Subtraction of %f and %f is : %f" %(num1, num2, num1 - num2))
elif op == "/":
    print("Divison of %f and %f is : %f" %(num1, num2, num1 / num2))
elif op == "*":
    print("Multiplication of %f and %f is : %d" %(num1, num2, num1 * num2))
else:
    print("invalid operator")


