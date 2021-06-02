from Time_Class import Time

# First Time object
myTime1 = Time()
myTime1.set_time(1, 2, 3)
myTime1.print_time()

# Second Time object
myTime2 = Time()
myTime2.set_time(12, 0, 0)


myTime3 = Time()
myTime3.set_time(6, 8, 10)

for i in range(10):
    myTime3.print_time()
    myTime3.tick()

print("My 3 time objects are now storing:")
myTime1.print_time()
myTime2.print_time()
myTime3.print_time()



# Gives you the documentation/comments you put in your class code
print (myTime1.__doc__)

# Let's you know the class you are working with
print (myTime1.__class__)