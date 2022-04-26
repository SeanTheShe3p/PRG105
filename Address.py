import tkinter as tk


class MainGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('300x150')
        self.frame1 = tk.Frame(self.window)
        self.frame2 = tk.Frame(self.window)
        self.frame3 = tk.Frame(self.window)
        self.frame4 = tk.Frame(self.window)
        self.label1 = tk.Label(self.frame1, text='Display address program')
        self.address = tk.StringVar()
        self.label2 = tk.Label(self.frame2, textvariable=self.address)
        self.button_show = tk.Button(self.frame4, text='display', command=self.show_address)
        self.button_quit = tk.Button(self.frame4, text='Quit', command=self.window.destroy)
        # packing
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.label1.pack()
        self.label2.pack()
        self.button_show.pack(side='left')
        self.button_quit.pack(side='right')
        # loop
        tk.mainloop()

    def show_address(self):
        self.address.set('8900 US-14\n Crystal Lake, IL 60012\n')


main_gui = MainGUI()
