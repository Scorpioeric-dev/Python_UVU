
# year = eval(input("Enter year: "))
# if year == 1:
#    print ("Freshman")
# if year == 2:
#    print ("Sophomore")
# if year == 3:
#    print ("Junior")
# if year == 4:
#    print ("Senior")

   # //nested if statements you can use the elif syntax to create nested if statements indention convention is critical for python

# year = eval(input("Enter year: "))
# if year == 1:
#    print ("Freshman")
# elif year == 2:
#    print ("Sophomore")
# elif year == 3:
#    print ("Junior")
# elif year == 4:
#    print ("Senior")
# else:
#    print ("Not a valid year")


#indentation is key

# age = eval(input("How old are you? "))
# registered = input("Are you registered? (y/n) ")
#
# if age >= 18:
#     if registered == "y":
#          print ("You are ready to vote!")
#     else:
#          print ("You are not ready to vote.")


#Compound condition operators and or included in if statements clean up the code

# age = eval(input("How old are you? "))
# registered = input("Are you registered? (y/n) ")
#
# if age >= 18 and registered == "y":
#     print("You are ready to vote!")
# else:
#     print("You are not ready to vote.")

# rate = eval(input("what is your hourly rate?"))
# hours = eval(input("How many hours have you worked?"))
#
# if hours < 40:
#     pay = hours * rate
# else:
#     pay = hours * rate
#     overtimeHours = hours - 40
#     overtimePay = overtimeHours * (rate * 0.5)
#     pay = pay + overtimePay
#
# print("Your weekly pay is :", pay)


# expenses = eval(input('What are your expenses total?'))
# assets = eval(input('What are your assets total?'))
#
# if expenses < assets:
#     Difference = assets - expenses
#
# print(f"You will have : {Difference} left over")

# Prompt a user for wind speed

speed = eval(input("What is the wind speed presently?"))
if speed >= 156:
    print('this is a Hurricane Category 5 take Shelter immediately')
elif 131 <= speed <= 155:
    print('This is a category 4 Hurricane take shelter')
elif 111 <= speed <= 130:
    print('This is a category 3 Hurricane take cover')
elif 96 <= speed <= 110:
    print('This is a category 2 Hurricane take shelter')
else:
    print('Category 1 Windy conditions this is not a hurricane')

