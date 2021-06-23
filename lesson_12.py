from tkinter import *


class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("500x200")
        self.master.title("F12")
        self.grid()

        #     self.prompt = Label(self, text="What's your name?")
        #     self.prompt.grid(row=0, column=0, padx=2)
        #     self.input = Entry(self)
        #     self.input.grid(row=0, column=1, padx=2)
        #
        #     self.button_click_here = Button(self, text="Submit",
        #                                     command=self.press_here)
        #     self.button_click_here.grid(columnspan=2, pady=10)
        #
        #     self.my_text = StringVar()
        #     self.message = Label(self, textvariable=self.my_text)
        #     self.message.grid(columnspan=2, pady=2)
        #
        # def press_here(self):
        #     output_message = 'Hi there ' + self.input.get()
        #     self.my_text.set(output_message)

        self.sample_label = Label(self, text="Some Sample Text", font="Courier 10")
        self.sample_label.grid(row=0, column=0, columnspan=2)
        #  Bold checkbox
        self.bold_on = IntVar()
        self.check_bold = Checkbutton(self, text="Bold",
                                      variable=self.bold_on, command=self.set_font)
        self.check_bold.grid(row=1, column=0)
        # Underline checkbox
        self.underline_on = IntVar()
        self.check_underline = Checkbutton(self, text="Underline",
                                           variable=self.underline_on, command=self.set_font)
        self.check_underline.grid(row=1, column=1)

        # Radio Button --
        self.point_size = StringVar()
        self.point_size.set("10")

        self.ten_point = Radiobutton(self, text="10 point",
                                     variable=self.point_size, value="10",
                                     command=self.set_font)
        self.ten_point.grid(row=2, column=0)

        self.point_size = StringVar()
        self.point_size.set("12")

        self.twelve_point = Radiobutton(self, text="12 point",
                                        variable=self.point_size, value="12",
                                        command=self.set_font)
        self.twelve_point.grid(row=2, column=1)

    def set_font(self):
        new_font = "Courier"

        if self.point_size.get() == '10':
            new_font = new_font + ' 10'
        else:
            new_font = new_font + ' 12'

        if self.bold_on.get() == 1:
            new_font = new_font + " bold"

        if self.underline_on.get() == 1:
            new_font = new_font + " underline"

        self.sample_label.config(font=new_font)


frame01 = MyFrame()
frame01.mainloop()
