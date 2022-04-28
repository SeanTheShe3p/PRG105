from tkinter import messagebox
import tkinter as tk
import pickle
    # I'm having trouble with the pickle I've been getting the same error for about 4 hours and dont know the solution,
    # the assignment is already late, I will send you an email also asking if maybe you can see what I am doing wrong. Thanks!
    # EOFError: Ran out of input 

class MenuGUI:
    def __init__(self, master):
        self.master = master
        # frames
        self.frame1 = tk.Frame(self.master)
        self.frame2 = tk.Frame(self.master)
        self.frame3 = tk.Frame(self.master)
        self.frame4 = tk.Frame(self.master)
        self.frame5 = tk.Frame(self.master)
        # Variable for Radios
        self.radio_var = tk.IntVar()
        self.radio_var.set(1)
        # radios
        self.radio1 = tk.Radiobutton(self.frame1, text='Search', variable=self.radio_var, value=1)
        self.radio2 = tk.Radiobutton(self.frame2, text='Add', variable=self.radio_var, value=2)
        self.radio3 = tk.Radiobutton(self.frame3, text='Change', variable=self.radio_var, value=3)
        self.radio4 = tk.Radiobutton(self.frame4, text='Delete', variable=self.radio_var, value=4)
        # pack radio buttons
        self.radio1.pack()
        self.radio2.pack()
        self.radio3.pack()
        self.radio4.pack()
        # Buttons
        self.select_button = tk.Button(self.frame5, text='select', command=self.open_window)
        self.quit_button = tk.Button(self.frame5, text='quit', command=self.master.destroy)
        # pack
        self.select_button.pack()
        self.quit_button.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

    def open_window(self):
        if self.radio_var.get() == 1:
            LookupGUI(self.master)
        elif self.radio_var.get() == 2:
            AddGUI(self.master)
        elif self.radio_var.get() == 3:
            ChangeGUI(self.master)
        elif self.radio_var.get() == 4:
            DeleteGUI(self.master)
        else:
            tk.messagebox.showinfo('ERROR', 'The selection was somehow invalid')


class LookupGUI:
    def __init__(self, master):
        try:
            input_file = open("personal_data.bat", 'rb')
            self.personal_data = pickle.load(input_file)
            input_file.close()
        except FileNotFoundError:
            tk.messagebox.showerror('Error', 'File not found')
            self.personal_data = {}
        # Lookup GUI
        self.lookup = tk.Toplevel(master)
        # Frames
        self.frame1 = tk.Frame(self.lookup)
        self.frame2 = tk.Frame(self.lookup)
        self.frame3 = tk.Frame(self.lookup)
        self.frame4 = tk.Frame(self.lookup)

        # search variables
        self.return_value = tk.StringVar()
        self.text = tk.Label(self.frame1, text='Search:')
        self.search_box = tk.Entry(self.frame2, width=20)
        self.label = tk.Label(self.frame3, textvariable=self.return_value)
        # Pack
        self.text.pack()
        self.search_box.pack()
        self.label.pack()
        # Buttons
        self.search_button = tk.Button(self.frame4, text='search', command=self.search)
        self.back_button = tk.Button(self.frame4, text='back', command=self.back)
        # Pack
        self.search_button.pack()
        self.back_button.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

    def search(self):
        name = self.search_box.get()
        input_file = open("personal_data.bat", 'rb')
        self.personal_data = pickle.load(input_file)
        result = self.personal_data.get(name)
        self.return_value.set(result)

    def back(self):
        self.lookup.destroy()


class AddGUI:
    def __init__(self, master):
        try:
            input_file = open("personal_data.bat", 'rb')
            self.personal_data = pickle.load(input_file)
            input_file.close()
        except FileNotFoundError:
            tk.messagebox.showerror('Error', 'File not found')
            self.personal_data = {}
        # Lookup GUI
        self.add = tk.Toplevel(master)
        # Frames
        self.frame1 = tk.Frame(self.add)
        self.frame2 = tk.Frame(self.add)
        self.frame3 = tk.Frame(self.add)
        self.frame4 = tk.Frame(self.add)
        # search variables
        self.confirm_var = tk.StringVar()
        self.name = tk.Entry(self.frame1, width=20)
        self.label1 = tk.Label(self.frame1, text='Name:')
        self.phone = tk.Entry(self.frame2, width=20)
        self.label2 = tk.Label(self.frame2, text='Number:')
        # Confirm
        self.confirm_var_label = tk.Label(self.frame3, textvariable=self.confirm_var)
        # Buttons
        self.add_button = tk.Button(self.frame4, text='add', command=self.add_person)
        self.back_button = tk.Button(self.frame4, text='back', command=self.back)
        # Pack
        self.add_button.pack()
        self.back_button.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.confirm_var_label = tk.Label(self.frame3, textvariable=self.confirm_var)
        self.confirm_var = tk.StringVar()
        self.name.pack(side='right')
        self.label1.pack(side='left')
        self.phone.pack(side='right')
        self.label2.pack(side='left')

    def add_person(self):
        name = self.name.get()
        phone = self.phone.get()
        # input_file = open("personal_data.bat", 'rb')
        # self.personal_data = pickle.load(input_file)
        # input_file.close()
        self.personal_data[name] = phone
        output_file = open("personal_data.bat", 'wb')
        pickle.dump(self.personal_data, output_file)
        self.confirm_var.set('successfully added')

    def back(self):
        self.add.destroy()


class ChangeGUI:
    def __init__(self, master):
        try:
            input_file = open("personal_data.bat", 'rb')
            self.personal_data = pickle.load(input_file)
            input_file.close()
        except FileNotFoundError:
            tk.messagebox.showerror('Error', 'File not found')
            self.personal_data = {}
        self.change = tk.Toplevel(master)
        # Frames
        self.frame1 = tk.Frame(self.change)
        self.frame2 = tk.Frame(self.change)
        self.frame3 = tk.Frame(self.change)
        self.frame4 = tk.Frame(self.change)
        self.frame5 = tk.Frame(self.change)
        self.frame6 = tk.Frame(self.change)
        # Search
        self.results = tk.StringVar()
        self.label = tk.Label(self.frame1, text='search the user to change:')
        self.search = tk.Entry(self.frame1, width=20)
        self.search_button = tk.Button(self.frame1, text='search', command=self.search_person)
        # pack
        self.label.pack(side='left')
        self.search.pack(side='left')
        self.search_button.pack(side='right')
        self.frame1.pack()
        # Edit
        self.confirm = tk.StringVar()
        self.label_result = tk.Label(self.frame2, textvariable=self.results)
        self.label_name = tk.Label(self.frame3, text='New name:')
        self.entry_name = tk.Entry(self.frame3, width=20)
        self.label_phone = tk.Label(self.frame4, text='New phone:')
        self.entry_phone = tk.Entry(self.frame4, width=20)
        # Edit back buttons
        self.button_edit = tk.Button(self.frame6, text='edit', command=self.edit_person)
        self.button_back = tk.Button(self.frame6, text='back', command=self.back)
        self.label_confirm = tk.Label(self.frame5, textvariable=self.confirm)
        # Pack
        self.button_edit.pack()
        self.button_back.pack()
        self.label_confirm.pack()
        self.label_result.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.label_name.pack(side='left')
        self.entry_name.pack(side='right')
        self.label_phone.pack(side='left')
        self.entry_phone.pack(side='right')

    def search_person(self):
        name = self.search.get()
        # input_file = open("personal_data.bat", 'rb')
        # self.personal_data = pickle.load(input_file)
        results = self.personal_data.get(name, 'cannot find')
        self.results.set(results)

    def edit_person(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        # input_file = open("personal_data.bat", 'rb')
        # self.personal_data = pickle.load(input_file)
        # input_file.close()
        self.personal_data.pop(self.search)
        self.personal_data[name] = phone
        output_file = open("personal_data.bat", 'wb')
        pickle.dump(self.personal_data, output_file)
        self.confirm_var.set('successfully updated')

    def back(self):
        self.change.destroy()


class DeleteGUI:
    def __init__(self, master):
        try:
            input_file = open("personal_data.bat", 'rb')
            self.personal_data = pickle.load(input_file)
            input_file.close()
        except FileNotFoundError:
            tk.messagebox.showerror('Error', 'File not found')
            self.personal_data = {}
        self.delete = tk.Toplevel(master)
        # Frames
        self.frame1 = tk.Frame(self.delete)
        self.frame2 = tk.Frame(self.delete)
        self.frame3 = tk.Frame(self.delete)
        self.frame4 = tk.Frame(self.delete)
        # Search
        self.results = tk.StringVar()
        self.label = tk.Label(self.frame1, text='search the user to delete:')
        self.search = tk.Entry(self.frame1, width=20)
        self.search_button = tk.Button(self.frame1, text='search', command=self.search_person)
        # pack
        self.label.pack(side='left')
        self.search.pack(side='left')
        self.search_button.pack(side='right')
        self.frame1.pack()
        # Edit
        self.confirm = tk.StringVar()
        self.label_result = tk.Label(self.frame2, textvariable=self.results)
        # Edit back buttons
        self.label_confirm = tk.Label(self.frame3, textvariable=self.confirm)
        self.button_delete = tk.Button(self.frame4, text='delete', command=self.delete_person)
        self.button_back = tk.Button(self.frame4, text='back', command=self.back)
        # Pack
        self.button_delete.pack()
        self.button_back.pack()
        self.label_confirm.pack()
        self.label_result.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

    def search_person(self):
        name = self.search.get()
        # input_file = open("personal_data.bat", 'rb')
        # self.personal_data = pickle.load(input_file)
        # input_file.close()
        results = self.personal_data.get(name, 'cannot find')
        self.results.set(results)

    def delete_person(self):
        name = self.search.get()
        # input_file = open("personal_data.bat", 'rb')
        # self.personal_data = pickle.load(input_file)
        # input_file.close()
        self.personal_data.pop(name)
        output_file = open('personal_data.bat', 'wb')
        pickle.dump(self.personal_data, output_file)
        self.confirm.set('successfully added')

    def back(self):
        self.delete.destroy()


def main():
    root = tk.Tk()
    MenuGUI(root)
    root.mainloop()


main()
