# def some_function():
#     try:
#         age = eval(input('Please enter your age: '))
#         ten_years = age + 10
#         print("In 10 years, you'll be", ten_years)
#     except NameError:
#         print("Name Error")
#     except Exception:
#         print("Something unexpected has happened")
#
#
# some_function()
# print("Have a nice day. Goodbye.")


# try:
#     my_list = [0, 1, 2]
#     print(my_list[4])
# except IndexError as ie:
#     print(ie)

try:
    infile = open('myfile.txt', 'r')
    infile.write("hello")

    infile.close()
except IOError as ioe:
    print(ioe.filename)
    print(ioe.strerror)

try:
    user_num = eval(input("Please enter a number: "))
    result = 10 / user_num
except (NameError, SyntaxError):
    print("The value you entered was not a number")
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print("The result of dividing 10 by your number is", result)

# The last block that I want to address here is the finally block.
# This block is where you'll place code that you want to be run whether an exception occurs or not.

# try:
#     infile = open('myfile.txt', 'r')
#     try:
#         value = infile.readline()
#         number = int(value)
#         print(number)
#     finally:
#         infile.close()
#         print("the data file was closed")
# except IOError as io:
#     print("Could not open file:", io.filename)
# except ValueError:
#     print("Could not convert", value, "to a number")
