# number = 1
# while number <= 20:
#          print (number)
#          number = number + 1
# print ("goodbye!")


# while loop syntax and example

# number = 1
# answer = 'yes'
# while answer == 'yes':
#          print (number)
#          number = number + 1
#          answer = input(
#                 "Do you want the next number? ")


# for number in range(58, 48, -2):
#       print (number)


# Example of a for loop averaging numbers inputed by user
# num_of_nums = eval(input(
#          "How many numbers do you want to average? "))
#
# sum = 0.0
#
# for count in range (num_of_nums):
#          value = eval(input("Enter a value: "))
#          sum = sum + value
#
# average = sum / num_of_nums
# print ("The average is:", average)

# Break in a loop example
# for number in range(1, 11):
#          if number == 4:
#                    break
#          print (number)
# print ("Thanks!")

# Continue statement you can omit a portion of the loop based on a condition being met
# for number in range(1, 11):
#          if number == 4:
#                    continue
#          print (number)
# print ("Thanks!")

# The else clause //  if break is enacted it doesn't run normally
# for number in range(1, 11):
#          if number == 4:
#                    break
#          print (number)
# else:
#          print ("Exited normally")

# phrase = input("Enter a phrase: ")
# letter = input("Enter a letter: ")
# length = len(phrase)
#
# for index in range(0, length):
#          if phrase [index] == letter:
#                   break
# else:
#          print ("Your letter wasn't found")

user_nums = eval(input('How many number would you like to average today?'))
total = 0.0

for count in range(user_nums):
    numbers = eval(input("Enter a Number: "))
    total = total + numbers

average = total / user_nums
print("The average is:", average)

# count = 0
# sum = 0.0
# average = 0.0
# value = eval(input("Please enter a number (-1 quits): "))
#
# while (value != -1):
#     sum = sum + value
#     count = count + 1
#
#     value = eval(input("Please enter a number (-1 quits): "))
#
# This is necessary, in case the user doesn't enter any values
# if (count != 0):
#     average = sum / count

# print ("The sum of these numbers is", sum)
# print ("The average of these numbers is", average)

