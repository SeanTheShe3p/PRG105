import tkinter as tk


class MyWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.frame1 = tk.Frame(self.window)
        self.frame2 = tk.Frame(self.window)
        self.frame3 = tk.Frame(self.window)
        self.frame4 = tk.Frame(self.window)
        self.frame5 = tk.Frame(self.window)
        self.frame6 = tk.Frame(self.window)
        self.label1 = tk.Label(self.frame1, text="How many gallons does your tank hold?")
        self.label2 = tk.Entry(self.frame2, width=8)
        self.label3 = tk.Label(self.frame3, text="How many miles have you driven")
        self.label4 = tk.Entry(self.frame4, width=20)
        self.value = tk.StringVar()
        self.label5 = tk.Label(self.frame5, textvariable=self.value)
        self.button1 = tk.Button(self.frame6, text="Convert", command=self.convert)
        self.button2 = tk.Button(self.frame6, text="Quit", command=self.window.destroy)
        # Packing
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()
        self.label5.pack()
        self.button1.pack()
        self.button2.pack()
        tk.mainloop()

    def convert(self):
        gallons = int(self.label2.get())
        miles = int(self.label4.get())
        mpg_return = miles / gallons
        mpg_return = str(mpg_return)
        self.value.set(mpg_return)


my_gui = MyWindow
my_gui()
