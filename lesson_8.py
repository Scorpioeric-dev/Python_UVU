from tkinter import Frame, Canvas


class MyFrame(Frame):
    def __init__(self, coord=None, decrement=0):
        Frame.__init__(self)

        self.myCanvas = Canvas(width=150, height=150, bg="white")
        self.myCanvas.grid()

        self.myCanvas.create_rectangle(10, 10, 20, 20, fill="red")
        self.myCanvas.create_rectangle(10, 30, 20, 40, fill="yellow")
        self.myCanvas.create_rectangle(10, 50, 20, 60, fill="blue")

        print("Finds all shapes")
        print(self.myCanvas.find_enclosed(0, 0, 30, 70))

        print("Finds middle shape")
        print(self.myCanvas.find_enclosed(0, 25, 30, 45))

        print("Finds no shapes")
        print(self.myCanvas.find_enclosed(0, 0, 1, 1))


# frame02 = MyFrame()
# frame02.mainloop()

# my_list = [10, 'ten']
#
# my_list.extend([20, 'twenty'])
#
#
# my_list.insert(3, 'hi there!')
#
#
# my_list.remove('hi there!')
#
# # my_list.sort()
# my_list.reverse()
#
#
# days_of_week = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
# print(days_of_week)

num = []
sum = 0.0

user_number = eval(input("Please enter a number (-999 stop): "))
# loop until user is ready to quit
while user_number != -999:
    num.append(user_number)
    sum = sum + user_number
    user_number = eval(input("Please enter a number (-999 stop): "))

# Make sure the user entered something
if len(num) != 0:
    # Compute average
    average = sum / len(num)

    # Do output
    print("Using the numbers:")

    for i in range(len(num)):
        # Note the end = " " at the end will keep the output on
        #   the same line
        print(num[i], end=" ")

    print("\nThe average is:", average)
else:
    print("No values were entered")
