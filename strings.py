print("today is a good day .")
print("now we are printing .")
print('we can do' + " like this also .")
print("'we can print in this way also .'")
# we can use variables to store the strings values.
name ="ROHIT"
surname = "CHATURVEDI"
print( name + " " + surname + " " + 'BYE !!!!!')

# WE CAN ALSO USE INPUT FUNCTION TO ACCEPT OUR DESIRED NAME .
var = input("Please enter your desired name :- ".upper())
print("My name is " + var.upper()) # " " double quotes  denotes spaces.

# Displaying that Python is a STRONGLY TYPED LANGUAGE.
value = "hello world"
print(type(value)) ## it's type is STRING.
age = 21
print(type(age)) # it's type is INTEGER.
no =23.55
print(type(no))

# An integer value must be converted to string to work with string sentence .
print(name +" "+ surname + " is " + str(age) + " years old .")
#here in this example we have to convert age in the string format to use it with string.

#you didnt mention f-string usage..So just adding little bit f-string..

str_0 = "Your code is awesome and "
str_1 = "I want to appreciate your work"

final_str = f"{str_0}{str_1}"
print(final_str)

#Just a simple example>>> :)
