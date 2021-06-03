from tkinter import *
from time import *


# frame01 = Frame()
# frame01.mainloop()

class MyFrame(Frame):
    def __init__(self, coord=None, decrement=0):
        Frame.__init__(self)

        self.myCanvas = Canvas(width=1300, height=1300, bg="light blue")
        self.myCanvas.grid()

        # cleaner version of animation using variable

        my_rect_id = self.myCanvas.create_rectangle(250, 250, 250, 250, )
        my_oval = self.myCanvas.create_oval(10, 10, 200, 100, fill="blue")
        my_circle = self.myCanvas.create_oval(10, 10, 200, 100, fill="red")
        self.myCanvas.update()

        for count in range(15):

            increment = 100 * count
            self.myCanvas.coords(my_oval,
                                 100 + increment, 100 + increment,
                                 250 + increment, 250 + increment)
            self.myCanvas.coords(my_circle,
                                 100 + increment, 110 - decrement,
                                 200 + increment, 260 - decrement)
            self.myCanvas.update()
            sleep(1)

        # example of animation using a for loop

        # for count in range(10):
        #     increment = 10 * count
        #     self.myCanvas.create_rectangle(10 + increment,
        #                                    10 + increment, 50 + increment, 50 + increment)
        #     self.myCanvas.update()
        #     sleep(1)
        #
        #     # Now color over the previous rectangle
        #     self.myCanvas.create_rectangle(10 + increment,
        #                                    10 + increment, 50 + increment, 50 + increment,
        #                                    outline="white")

        # self.myCanvas.create_rectangle(10, 10, 50, 50)
        # self.myCanvas.update()
        #
        # sleep(1)
        #
        # self.myCanvas.create_rectangle(20, 20, 60, 60)


frame02 = MyFrame()
frame02.mainloop()
