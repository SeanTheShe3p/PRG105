import tkinter
import tkinter.messagebox
# 13.2
# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2


class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label1 = tkinter.Label(self.main_window, text='Sean Widdowson')
        self.label1.pack()
        tkinter.mainloop()


class MyGUI3:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.label1 = tkinter.Label(self.frame1, text='Sean Widdowson, Associates in Art')
        self.label2 = tkinter.Label(self.frame2, text='PRG-105, ENG-151')
        self.label1.pack()
        self.label2.pack()
        self.frame1.pack()
        self.frame2.pack()
        tkinter.mainloop()


class MyGUI4:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame1 = tkinter.Frame(self.main_window)
        self.label1 = tkinter.Label(self.frame1, text='Why did the chicken cross the road?')
        self.button1 = tkinter.Button(self.main_window, text='answer', command=self.do_something)
        self.label1.pack()
        self.frame1.pack()
        self.button1.pack()
        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('response', 'To get to the other side!')


class InToCm:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.label1 = tkinter.Label(self.frame1, text='Enter in to convert to cm')
        self.inches = tkinter.Entry(self.frame2, width=10)
        self.calc_button = tkinter.Button(self.frame2, text='convert', command=self.calculate)
        self.quit_button = tkinter.Button(self.frame2, text='quit', command=self.main_window.destroy)
        self.calc_button.pack()
        self.quit_button.pack()
        self.label1.pack()
        self.inches.pack()
        self.frame1.pack()
        self.frame2.pack()
        tkinter.mainloop()

    def calculate(self):
        inches = float(self.inches.get())
        centimeters = inches * 2.54
        tkinter.messagebox.showinfo('conversion', str(inches) + 'in. is equal to ' + str(centimeters) + 'cm.')


MyGUI2()
MyGUI3()
MyGUI4()
InToCm()

# 13.3
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2
# 13.4
# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Creates an instance of MyGUI3
# 13.5
# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI
# 13.6-13.7
# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters
