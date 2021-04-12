# 1. Create three variables in a single line and assign values to them in such a manner that each one of
#them belongs to a different data type.

a,b,pi = 13,"word",3.14

#2. Create a variable of type complex and swap it with another variable of type integer.

comp = 3+4j
num = 6
comp,num=num,comp

#3. Swap two numbers using a third variable and do the same task without using any third variable.

a = 3
b = 4
temp = b
b = a
a = temp

a,b = b,a

#4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
#Version.

#python 3.x
data = input("Enter anything to print it: ")
print(data)

# python 2.x
data = raw_input("Enter anything to print it: ")
print input2

#5. Write a program to complete the task given below:
#Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
#another variable called z. Add 30 to z and store the output in variable result and print result as the
#final output.

num1 = eval(input("Enter number between 1-10: "))
num2 = eval(input("Enter number between 1-10: "))

z = num1 + num2
result = z + 30

print(result)

#6. Write a program to check the data type of the entered values.
#HINT: Printed output should say - The data type of the input value is : int/float/string/etc

data = eval(input("Enter valur for datatype check: "))

print("The data type of the input value is: {}".format(type(data)))

#7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
#UPPERCASE.
#(Refer: https://capitalizemytitle.com/camel-case/)

lowerCamel = "helloWorld"
UpperCamel = "HelloWorld"
snake_case = "hello_world"
UPPERCASE = "HELLOWORLD"


#8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
#again. Will it change the value? If Yes then Why?

# Yes, It will change the value because Python is a dynamic language which has the ability to interpret 
# the data type of the variable and reinstate same variable that has different data type.