# def print_test():
#     """This will print a test of 2 separate text"""
#     print("This is a test")
#     print("My first function in python")
#
# # --We have to invoke the function in the bottom of the file
#
# print_test()
# def print_value(value):
#     """This function prints the value passed in"""
#     print ("Your value is:", value)
#
# print_value(5)
# print_value("number")
#
# name = "Pat"
# print_value(name)

# def change_value(value):
#     """This function changes the value passed in to 1"""
#     print ("Inside, value is:", value)
#     value = 1
#     print ("Inside, value is changed to:", value)
#
# number = 5
# print ("Outside, number is:", number)
# change_value(number)
# print ("Outside, number is now:", number)

# def change_number():
#     """This function changes the value passed in to 1 (global)"""
#     global number
#     number = 1
#
# number = 5
# print ("Outside, number is:", number)
# change_number()
# print ("Outside, number is now:", number)

# def square(num):
#     """This function calculates the square of a number"""
#     result = num * num
#     return result
#
#
# for i in range(1, 11):
#     print(square(i))

# def prompt_user(prompt, num_tries = 2):
#     """This function prompts the user a certain number of times"""
#     answer = input(prompt)
#
#     while (answer != "yes" and answer != "no" and num_tries > 1):
#        num_tries = num_tries - 1
#        print ("Try again")
#        answer = input(prompt)
#
#
# prompt_user("Enter yes or no: ")
# prompt_user("Enter yes or no: ", 4)


# Practice this syntax to learn the function outline
# def convert_to_farenheit(celsius):
#     """This function converts celsius to fahrenheit"""
#     fahrenheit = 9.0 / 5.0 * celsius + 32
#     return fahrenheit
# for cel in range(0,101,10):
#     # The \t her is used ot insert a tab into the output
#
#      print(cel , "\t" , convert_to_farenheit(cel))

