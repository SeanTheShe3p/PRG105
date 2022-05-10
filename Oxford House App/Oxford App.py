import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pickle


# Many thanks to https://www.tutorialspoint.com/python/tk_menu.htm
# https://www.pythontutorial.net/tkinter/tkinter-toplevel/
# https://www.tutorialspoint.com/how-to-sort-a-dictionary-in-python
# https://www.w3schools.com/python/python_dictionaries.asp
# https://pythonguides.com/python-tkinter-frame/, https://www.geeksforgeeks.org/changing-the-mouse-cursor-tkinter/
# And other internet sites that taught me what not to do.


# Main GUI Window
class MenuGUI:
    def __init__(self, window):
        self.window = window
        self.window.geometry('500x400')
        self.window.config(cursor='heart')
        # Frames
        self.frame1 = tk.Frame(self.window, relief=RAISED, bd=20)
        self.frame2 = tk.Frame(self.window)
        self.frame3 = tk.Frame(self.window, relief=RAISED, bd=20)
        # Canvas
        self.picture = tk.Canvas(self.frame2, bg='white', width=300, height=220)
        self.circle1 = self.picture.create_oval(50, 10, 250, 210, fill='black')
        self.circle2 = self.picture.create_oval(60, 20, 240, 200, fill='white')
        self.line1 = self.picture.create_polygon(150, 20, 225, 160, 75, 160, fill='black')
        self.line2 = self.picture.create_polygon(150, 40, 205, 150, 95, 150, fill='white')
        self.picture.pack(padx=75, pady=25)
        # Labels
        self.oxford_label = tk.Label(self.frame1, text='OXFORD')
        self.house_label = tk.Label(self.frame3, text='HOUSE')
        # Menu
        self.menu = Menu(self.window)
        #   Clients
        self.clients_menu = Menu(self.menu, tearoff=0)
        self.clients_menu.add_command(label='New Client', command=self.new_client)
        self.clients_menu.add_command(label='Edit Client', command=self.edit_client)
        self.clients_menu.add_command(label='View Client', command=self.view_client)
        self.clients_menu.add_command(label='Delete', command=self.delete_client)
        self.clients_menu.add_separator()
        self.clients_menu.add_command(label='View All Clients', command=self.all_client)
        self.menu.add_cascade(label='Clients', menu=self.clients_menu)
        #   Calendar
        self.calendar_menu = Menu(self.menu, tearoff=0)
        self.calendar_menu.add_command(label='Add Event', command=self.add_calendar)
        self.calendar_menu.add_command(label='Edit Date', command=self.edit_calendar)
        self.calendar_menu.add_command(label='View Event', command=self.view_calendar)
        self.calendar_menu.add_command(label='delete Date', command=self.delete_calendar)
        self.calendar_menu.add_separator()
        self.calendar_menu.add_command(label='View Calendar', command=self.all_calendar)
        self.menu.add_cascade(label='Calendar', menu=self.calendar_menu)
        #   Board
        self.board_menu = Menu(self.menu, tearoff=0)
        self.board_menu.add_command(label='Add', command=self.add_board)
        self.board_menu.add_command(label='Edit', command=self.edit_board)
        self.board_menu.add_command(label='View', command=self.view_board)
        self.board_menu.add_command(label='delete', command=self.delete_board)
        self.board_menu.add_separator()
        self.board_menu.add_command(label='View All', command=self.all_boards)
        self.menu.add_cascade(label='Boards', menu=self.board_menu)
        #   Recovery
        self.recovery_menu = Menu(self.menu, tearoff=0)
        self.recovery_menu.add_command(label='Add a Meeting', command=self.add_meeting)
        self.recovery_menu.add_command(label='Change a Meeting', command=self.edit_meeting)
        self.recovery_menu.add_command(label='Lookup Meeting', command=self.view_meeting)
        self.recovery_menu.add_command(label='Delete a Meeting', command=self.delete_meeting)
        self.recovery_menu.add_separator()
        self.recovery_menu.add_command(label='View All Meetings', command=self.all_meetings)
        self.menu.add_cascade(label='Meetings', menu=self.recovery_menu)
        window.config(menu=self.menu)
        # Pack
        self.oxford_label.pack()
        self.house_label.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

    def new_client(self):
        NewClientPage(self.window)

    def edit_client(self):
        EditClientPage(self.window)

    def view_client(self):
        ViewClientPage(self.window)

    def delete_client(self):
        DeleteClientPage(self.window)

    def all_client(self):
        AllClientPage(self.window)

    def add_calendar(self):
        NewCalendarPage(self.window)

    def edit_calendar(self):
        EditCalendarPage(self.window)

    def view_calendar(self):
        ViewCalendarPage(self.window)

    def delete_calendar(self):
        DeleteCalendarPage(self.window)

    def all_calendar(self):
        AllCalendarPage(self.window)

    def add_board(self):
        NewBoardPage(self.window)

    def edit_board(self):
        EditBoardPage(self.window)

    def view_board(self):
        ViewBoardPage(self.window)

    def delete_board(self):
        DeleteBoardPage(self.window)

    def all_boards(self):
        AllBoardsPage(self.window)

    def add_meeting(self):
        NewMeetingPage(self.window)

    def edit_meeting(self):
        EditMeetingPage(self.window)

    def view_meeting(self):
        ViewMeetingPage(self.window)

    def delete_meeting(self):
        DeleteMeetingPage(self.window)

    def all_meetings(self):
        AllMeetingsPage(self.window)


class NewClientPage:
    def __init__(self, window):
        try:
            import_doc = open('clients.bat', 'rb')
            self.clients_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            tk.messagebox.showerror('ERRor', 'File could not be found')
            self.clients_data = {}
        self.new_client_gui = tk.Toplevel(window, cursor='heart')
        self.new_client_gui.geometry('500x200')
        # Frames
        self.frame1 = tk.Frame(self.new_client_gui)  # Message
        self.frame2 = tk.Frame(self.new_client_gui)  # Name
        self.frame3 = tk.Frame(self.new_client_gui)  # Birthday
        self.frame4 = tk.Frame(self.new_client_gui)  # Chore
        self.frame5 = tk.Frame(self.new_client_gui)  # Service position
        self.frame6 = tk.Frame(self.new_client_gui)  # Confirm
        self.frame7 = tk.Frame(self.new_client_gui)  # Buttons
        # Labels
        self.results = tk.StringVar()
        self.label_message = tk.Label(self.frame1, text='New Client')
        self.label_name = tk.Label(self.frame2, text='Name: ')
        self.label_birthday = tk.Label(self.frame3, text='Birthday: ')
        self.label_chore = tk.Label(self.frame4, text='Chore: ')
        self.label_service_position = tk.Label(self.frame5, text='Service position: ')
        self.label_result = tk.Label(self.frame6, textvariable=self.results)
        # Entries
        self.entry_name = tk.Entry(self.frame2, width=20)
        self.entry_birthday = tk.Entry(self.frame3, width=8)
        self.entry_chore = tk.Entry(self.frame4, width=20)
        self.entry_service_position = tk.Entry(self.frame5, width=20)
        # Buttons
        self.confirm_button = tk.Button(self.frame7, text='Confirm', command=self.confirm)
        self.back_button = tk.Button(self.frame7, text='Back', command=self.new_client_gui.destroy)
        # Pack
        self.confirm_button.pack(side='left')
        self.back_button.pack(side='right')
        self.entry_name.pack(side='right')
        self.entry_birthday.pack(side='right')
        self.entry_chore.pack(side='right')
        self.entry_service_position.pack(side='right')
        self.label_message.pack(side='left')
        self.label_name.pack(side='left')
        self.label_birthday.pack(side='left')
        self.label_chore.pack(side='left')
        self.label_service_position.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.frame7.pack()

    def confirm(self):
        name = self.entry_name.get()
        name = name.lower()
        birthday = self.entry_birthday.get()
        chore = self.entry_chore.get()
        service_position = self.entry_service_position.get()
        self.clients_data[name] = {'name': name, 'birthday': birthday, 'chore': chore, 'service position': service_position}
        output_file = open('clients.bat', 'wb')
        pickle.dump(self.clients_data, output_file)
        output_file.close()
        self.results.set('Added!')


class EditClientPage:
    def __init__(self, window):
        try:
            import_doc = open('clients.bat', 'rb')
            self.clients_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            tk.messagebox.showerror('ERRor', 'File could not be found')
            self.clients_data = {}
        self.edit_client_gui = tk.Toplevel(window, cursor='heart')
        self.edit_client_gui.geometry('500x200')
        # Frames
        self.frame1 = tk.Frame(self.edit_client_gui)  # Message
        self.frame2 = tk.Frame(self.edit_client_gui)  # Search
        self.frame3 = tk.Frame(self.edit_client_gui)  # Name
        self.frame4 = tk.Frame(self.edit_client_gui)  # Birthday
        self.frame5 = tk.Frame(self.edit_client_gui)  # Chore
        self.frame6 = tk.Frame(self.edit_client_gui)  # Service position
        self.frame7 = tk.Frame(self.edit_client_gui)  # Results
        self.frame8 = tk.Frame(self.edit_client_gui)  # Buttons
        # StringVar
        self.results = tk.StringVar()
        self.search_name = tk.StringVar()
        self.search_birthday = tk.StringVar()
        self.search_chore = tk.StringVar()
        self.search_service_position = tk.StringVar()
        # Labels
        self.label_searchbar = tk.Label(self.frame1, text='search')
        self.label_message = tk.Label(self.frame2, text='Edit Client')
        self.label_name = tk.Label(self.frame3, text='Name: ')
        self.label_birthday = tk.Label(self.frame4, text='Birthday: ')
        self.label_chore = tk.Label(self.frame5, text='Chore: ')
        self.label_service_position = tk.Label(self.frame6, text='Service position: ')
        # StringVar return
        self.search_name_label = tk.Label(self.frame3, textvariable=self.search_name)
        self.search_birthday_label = tk.Label(self.frame4, textvariable=self.search_birthday)
        self.search_chore_label = tk.Label(self.frame5, textvariable=self.search_chore)
        self.search_service_position_label = tk.Label(self.frame6, textvariable=self.search_service_position)
        self.label_result = tk.Label(self.frame7, textvariable=self.results)
        # Entries
        self.entry_search = tk.Entry(self.frame1, width=30)
        self.entry_name = tk.Entry(self.frame3, width=20)
        self.entry_birthday = tk.Entry(self.frame4, width=8)
        self.entry_chore = tk.Entry(self.frame5, width=20)
        self.entry_service_position = tk.Entry(self.frame6, width=20)
        # Buttons
        self.search_button = tk.Button(self.frame1, text='search', command=self.search)
        self.confirm_button = tk.Button(self.frame8, text='Confirm', command=self.edit)
        self.back_button = tk.Button(self.frame8, text='Back', command=self.edit_client_gui.destroy)
        # Pack
        self.confirm_button.pack(side='left')
        self.back_button.pack(side='right')
        self.search_button.pack(side='right')
        self.entry_search.pack(side='right')
        self.entry_name.pack(side='right')
        self.entry_birthday.pack(side='right')
        self.entry_chore.pack(side='right')
        self.entry_service_position.pack(side='right')
        self.label_searchbar.pack(side='left')
        self.label_message.pack(side='left')
        self.search_name_label.pack(side='left')
        self.search_birthday_label.pack(side='left')
        self.search_chore_label.pack(side='left')
        self.search_service_position_label.pack(side='left')
        self.label_name.pack(side='left')
        self.label_birthday.pack(side='left')
        self.label_chore.pack(side='left')
        self.label_service_position.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.frame7.pack()
        self.frame8.pack()

    def search(self):
        name = self.entry_search.get()
        name = name.lower()
        if name not in self.clients_data.keys():
            name = 'Not found'
            self.results.set(name)
        else:
            name = self.clients_data[name]['name']
            birthday = self.clients_data[name]['birthday']
            chore = self.clients_data[name]['chore']
            service_position = self.clients_data[name]['service position']
            self.search_name.set(name)
            self.search_birthday.set(birthday)
            self.search_chore.set(chore)
            self.search_service_position.set(service_position)

    def edit(self):
        new_name = self.entry_name.get()
        new_name.lower()
        old_name = self.entry_search.get()
        birthday = self.entry_birthday.get()
        chore = self.entry_chore.get()
        service_position = self.entry_service_position.get()
        try:
            if new_name != self.clients_data[old_name]['name'] and new_name != '':
                name = new_name
            elif new_name == '':
                name = old_name
            else:
                name = self.clients_data[old_name]['name']
            if birthday != self.clients_data[old_name]['birthday'] and birthday != '':
                birthday = birthday
            else:
                birthday = self.clients_data[old_name]['birthday']
            if chore != self.clients_data[old_name]['chore'] and chore != '':
                chore = chore
            else:
                chore = self.clients_data[old_name]['chore']
            if service_position != self.clients_data[old_name]['service position'] and service_position != '':
                service_position = service_position
            else:
                service_position = self.clients_data[old_name]['service position']
            self.clients_data.pop(old_name)
            self.clients_data[name] = {'name': name, 'birthday': birthday, 'chore': chore, 'service position': service_position}
            output_file = open("clients.bat", 'wb')
            pickle.dump(self.clients_data, output_file)
            output_file.close()
            self.results.set('successfully updated')
        except IndexError:
            tk.messagebox.showerror('ERRor', 'You typed bad')


class ViewClientPage:
    def __init__(self, window):
        try:
            import_doc = open('clients.bat', 'rb')
            self.clients_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            tk.messagebox.showerror('ERRor', 'File could not be found')
            self.clients_data = {}
        self.view_clients_gui = tk.Toplevel(window, cursor='heart')
        self.view_clients_gui.geometry('500x200')
        # Frames
        self.frame1 = tk.Frame(self.view_clients_gui)  # Message
        self.frame2 = tk.Frame(self.view_clients_gui)  # Search
        self.frame3 = tk.Frame(self.view_clients_gui)  # Results
        self.frame4 = tk.Frame(self.view_clients_gui)  # Buttons
        # StringVar
        self.results = tk.StringVar()
        # Labels
        self.label_searchbar = tk.Label(self.frame1, text='search')
        self.label_message = tk.Label(self.frame2, text='View Client')
        # StringVar return
        self.label_result = tk.Label(self.frame3, textvariable=self.results)
        # Entries
        self.entry_search = tk.Entry(self.frame2, width=30)
        # Buttons
        self.search_button = tk.Button(self.frame2, text='search', command=self.search)
        self.back_button = tk.Button(self.frame4, text='Back', command=self.view_clients_gui.destroy)
        # Pack
        self.back_button.pack(side='right')
        self.search_button.pack(side='right')
        self.entry_search.pack(side='right')
        self.label_searchbar.pack(side='left')
        self.label_message.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

    def search(self):
        name = self.entry_search.get()
        name = name.lower()
        if name not in self.clients_data.keys():
            result = 'Not found'
            self.results.set(result)
        else:
            # self.results.set(str(self.clients_data[name]))
            # self.results.set('Name: ' + str(self.clients_data[name]['name']))
            self.results.set('Name: ' + str(self.clients_data[name]['name']) + '\nBirthday: ' + str(self.clients_data[name]['birthday']) + '\nChore: ' + str(self.clients_data[name]['chore']) + '\nService Position: ' + str(self.clients_data[name]['service position']))


class DeleteClientPage:
    def __init__(self, window):
        try:
            import_doc = open('clients.bat', 'rb')
            self.clients_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            tk.messagebox.showerror('ARR!or', 'File could not be found')
            self.clients_data = {}
        self.delete_client_gui = tk.Toplevel(window, cursor='pirate')
        self.delete_client_gui.geometry('500x200')
        # Frames
        self.frame1 = tk.Frame(self.delete_client_gui)  # Message
        self.frame2 = tk.Frame(self.delete_client_gui)  # Search
        self.frame3 = tk.Frame(self.delete_client_gui)  # Results
        self.frame4 = tk.Frame(self.delete_client_gui)  # Buttons
        # StringVar
        self.results = tk.StringVar()
        # Labels
        self.label_searchbar = tk.Label(self.frame1, text='search')
        self.label_message = tk.Label(self.frame2, text='Delete Client')
        # StringVar return
        self.label_result = tk.Label(self.frame3, textvariable=self.results)
        # Entries
        self.entry_search = tk.Entry(self.frame1, width=30)
        # Buttons
        self.search_button = tk.Button(self.frame1, text='search', command=self.search)
        self.delete_button = tk.Button(self.frame4, text='Delete', command=self.delete)
        self.back_button = tk.Button(self.frame4, text='Back', command=self.delete_client_gui.destroy)
        # Pack
        self.back_button.pack(side='right')
        self.delete_button.pack(side='right')
        self.search_button.pack(side='right')
        self.entry_search.pack(side='right')
        self.label_searchbar.pack(side='left')
        self.label_message.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

    def search(self):
        name = self.entry_search.get()
        name = name.lower()
        if name not in self.clients_data.keys():
            result = 'Not found'
            self.results.set(result)
        else:
            self.results.set(self.clients_data[name])

    def delete(self):
        name = self.entry_search.get()
        name = name.lower()
        self.clients_data.pop(name)
        outfile = open('clients.bat', 'wb')
        pickle.dump(self.clients_data, outfile)
        outfile.close()
        self.results.set('Deleted')


class AllClientPage:
    def __init__(self, window):
        try:
            import_doc = open('clients.bat', 'rb')
            self.clients_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            # tk.messagebox.showerror('ERRor', 'File could not be found')
            self.clients_data = {}
        self.all_client_gui = tk.Toplevel(window, cursor='heart')
        # Frames
        self.frame1 = tk.Frame(self.all_client_gui)  # Message
        self.frame2 = tk.Frame(self.all_client_gui)  # Results
        self.frame3 = tk.Frame(self.all_client_gui)  # Buttons
        # StringVar and Labels
        self.results = tk.StringVar()
        self.label_message = tk.Label(self.frame1, text='View Clients')
        self.label_result = tk.Label(self.frame2, textvariable=self.results)
        # Buttons
        self.show_button = tk.Button(self.frame3, text='show', command=self.show_results)
        self.hide_button = tk.Button(self.frame3, text='hide', command=self.hide_results)
        self.back_button = tk.Button(self.frame3, text='Back', command=self.all_client_gui.destroy)
        # Pack
        self.back_button.pack(side='right')
        self.hide_button.pack(side='right')
        self.show_button.pack(side='right')
        self.label_message.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

    def show_results(self):
        dict2 = {}
        for key in sorted(self.clients_data):
            dict2[key] = self.clients_data[key]
        self.results.set(str(dict2))

    def hide_results(self):
        self.results.set('')


class NewCalendarPage:
    def __init__(self, window):
        try:
            import_doc = open('calendar.bat', 'rb')
            self.calendar_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            # tk.messagebox.showerror('ERRor', 'File could not be found')
            self.calendar_data = {}
        self.new_calendar_gui = tk.Toplevel(window, cursor='heart')
        self.new_calendar_gui.geometry('500x200')
        # Frames
        self.frame1 = tk.Frame(self.new_calendar_gui)  # Message
        self.frame2 = tk.Frame(self.new_calendar_gui)  # Date
        self.frame3 = tk.Frame(self.new_calendar_gui)  # Name
        self.frame4 = tk.Frame(self.new_calendar_gui)  # Event
        self.frame5 = tk.Frame(self.new_calendar_gui)  # Confirm
        self.frame6 = tk.Frame(self.new_calendar_gui)  # Buttons
        # Labels
        self.results = tk.StringVar()
        self.label_message = tk.Label(self.frame1, text='New Event')
        self.label_date = tk.Label(self.frame2, text='Date: ')
        self.label_name = tk.Label(self.frame3, text='Name: ')
        self.label_event = tk.Label(self.frame4, text='Event: ')
        self.label_result = tk.Label(self.frame5, textvariable=self.results)
        # Entries
        self.entry_date = tk.Entry(self.frame2, width=8)
        self.entry_name = tk.Entry(self.frame3, width=20)
        self.entry_event = tk.Entry(self.frame4, width=20)
        # Buttons
        self.confirm_button = tk.Button(self.frame6, text='Confirm', command=self.confirm)
        self.back_button = tk.Button(self.frame6, text='Back', command=self.new_calendar_gui.destroy)
        # Pack
        self.confirm_button.pack(side='left')
        self.back_button.pack(side='right')
        self.entry_date.pack(side='right')
        self.entry_name.pack(side='right')
        self.entry_event.pack(side='right')
        self.label_message.pack(side='left')
        self.label_date.pack(side='left')
        self.label_name.pack(side='left')
        self.label_event.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()

    def confirm(self):
        name = self.entry_name.get()
        date = self.entry_date.get()
        event = self.entry_event.get()
        self.calendar_data[date] = {'date': date, 'name': name, 'event': event}
        output_file = open('calendar.bat', 'wb')
        pickle.dump(self.calendar_data, output_file)
        output_file.close()
        self.results.set('Added!')


class EditCalendarPage:
    def __init__(self, window):
        try:
            import_doc = open('calendar.bat', 'rb')
            self.calendar_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            tk.messagebox.showerror('ERRor', 'File could not be found')
            self.calendar_data = {}
        self.edit_event_gui = tk.Toplevel(window, cursor='heart')
        self.edit_event_gui.geometry('500x200')
        # Frames
        self.frame1 = tk.Frame(self.edit_event_gui)  # Message
        self.frame2 = tk.Frame(self.edit_event_gui)  # Search
        self.frame3 = tk.Frame(self.edit_event_gui)  # Date
        self.frame4 = tk.Frame(self.edit_event_gui)  # Name
        self.frame5 = tk.Frame(self.edit_event_gui)  # Event
        self.frame6 = tk.Frame(self.edit_event_gui)  # Results
        self.frame7 = tk.Frame(self.edit_event_gui)  # Buttons
        # StringVar
        self.results = tk.StringVar()
        self.search_name = tk.StringVar()
        self.search_date = tk.StringVar()
        self.search_event = tk.StringVar()
        # Labels
        self.label_searchbar = tk.Label(self.frame1, text='search')
        self.label_message = tk.Label(self.frame2, text='Edit Date')
        self.label_date = tk.Label(self.frame3, text='Date: ')
        self.label_name = tk.Label(self.frame4, text='Name: ')
        self.label_event = tk.Label(self.frame5, text='Event: ')
        # StringVar return
        self.search_date_label = tk.Label(self.frame3, textvariable=self.search_date)
        self.search_name_label = tk.Label(self.frame4, textvariable=self.search_name)
        self.search_event_label = tk.Label(self.frame5, textvariable=self.search_event)
        self.label_result = tk.Label(self.frame6, textvariable=self.results)
        # Entries
        self.entry_search = tk.Entry(self.frame1, width=30)
        self.entry_date = tk.Entry(self.frame3, width=8)
        self.entry_name = tk.Entry(self.frame4, width=20)
        self.entry_event = tk.Entry(self.frame5, width=20)
        # Buttons
        self.search_button = tk.Button(self.frame1, text='search', command=self.search)
        self.confirm_button = tk.Button(self.frame7, text='Confirm', command=self.edit)
        self.back_button = tk.Button(self.frame7, text='Back', command=self.edit_event_gui.destroy)
        # Pack
        self.confirm_button.pack(side='left')
        self.back_button.pack(side='right')
        self.search_button.pack(side='right')
        self.entry_search.pack(side='right')
        self.entry_date.pack(side='right')
        self.entry_name.pack(side='right')
        self.entry_event.pack(side='right')
        self.label_message.pack(side='left')
        self.label_searchbar.pack(side='left')
        self.search_date_label.pack(side='left')
        self.search_name_label.pack(side='left')
        self.search_event_label.pack(side='left')
        self.label_date.pack(side='left')
        self.label_name.pack(side='left')
        self.label_event.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.frame7.pack()

    def search(self):
        date = self.entry_search.get()
        if date not in self.calendar_data.keys():
            result = 'Not found'
            self.results.set(result)
        else:
            date = self.calendar_data[date]['date']
            name = self.calendar_data[date]['name']
            event = self.calendar_data[date]['event']
            self.search_date.set(date)
            self.search_name.set(name)
            self.search_event.set(event)

    def edit(self):
        new_date = self.entry_date.get()
        old_date = self.entry_search.get()
        name = self.entry_name.get()
        event = self.entry_event.get()
        try:
            if new_date != self.calendar_data[old_date]['date'] and new_date != '':
                date = new_date
            elif new_date == '':
                date = old_date
            else:
                date = self.calendar_data[old_date]['date']
            if name != self.calendar_data[old_date]['name'] and name != '':
                name = name
            else:
                name = self.calendar_data[old_date]['name']
            if event != self.calendar_data[old_date]['event'] and event != '':
                event = event
            else:
                event = self.calendar_data[old_date]['event']
            out_dict = {'date': date, 'name': name, 'event': event}
            self.calendar_data.pop(old_date)
            self.calendar_data[date] = out_dict
            output_file = open("calendar.bat", 'wb')
            pickle.dump(self.calendar_data, output_file)
            output_file.close()
            self.results.set('successfully updated')
        except IndexError:
            tk.messagebox.showerror('ERRor', 'You should do better.')


class ViewCalendarPage:
    def __init__(self, window):
        try:
            import_doc = open('calendar.bat', 'rb')
            self.calendar_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            tk.messagebox.showerror('ERRor', 'File could not be found')
            self.calendar_data = {}
        self.view_calendar_gui = tk.Toplevel(window, cursor='heart')
        self.view_calendar_gui.geometry('500x200')
        # Frames
        self.frame1 = tk.Frame(self.view_calendar_gui)  # Message
        self.frame2 = tk.Frame(self.view_calendar_gui)  # Search
        self.frame3 = tk.Frame(self.view_calendar_gui)  # Results
        self.frame4 = tk.Frame(self.view_calendar_gui)  # Buttons
        # StringVar
        self.results = tk.StringVar()
        # Labels
        self.label_searchbar = tk.Label(self.frame1, text='search')
        self.label_message = tk.Label(self.frame2, text='View Date: ')
        # StringVar return
        self.label_result = tk.Label(self.frame3, textvariable=self.results)
        # Entries
        self.entry_search = tk.Entry(self.frame2, width=30)
        # Buttons
        self.search_button = tk.Button(self.frame2, text='search', command=self.search)
        self.back_button = tk.Button(self.frame4, text='Back', command=self.view_calendar_gui.destroy)
        # Pack
        self.back_button.pack(side='right')
        self.search_button.pack(side='right')
        self.entry_search.pack(side='right')
        self.label_searchbar.pack(side='left')
        self.label_message.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

    def search(self):
        date = self.entry_search.get()
        if date not in self.calendar_data.keys():
            result = 'Not found'
            self.results.set(result)
        else:
            self.results.set('Date: ' + str(self.calendar_data[date]['date']) + '\nName: ' + str(self.calendar_data[date]['name']) + '\nEvent: ' + str(self.calendar_data[date]['event']))


class DeleteCalendarPage:
    def __init__(self, window):
        try:
            import_doc = open('calendar.bat', 'rb')
            self.calendar_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            tk.messagebox.showerror('ERRor', 'File could not be found')
            self.calendar_data = {}
        self.delete_calendar_page = tk.Toplevel(window, cursor='pirate')
        self.delete_calendar_page.geometry('500x200')
        # Frames
        self.frame1 = tk.Frame(self.delete_calendar_page)  # Message
        self.frame2 = tk.Frame(self.delete_calendar_page)  # Search
        self.frame3 = tk.Frame(self.delete_calendar_page)  # Results
        self.frame4 = tk.Frame(self.delete_calendar_page)  # Buttons
        # StringVar
        self.results = tk.StringVar()
        # Labels
        self.label_searchbar = tk.Label(self.frame1, text='search')
        self.label_message = tk.Label(self.frame2, text='Delete Day')
        # StringVar return
        self.label_result = tk.Label(self.frame3, textvariable=self.results)
        # Entries
        self.entry_search = tk.Entry(self.frame1, width=30)
        # Buttons
        self.search_button = tk.Button(self.frame1, text='search', command=self.search)
        self.delete_button = tk.Button(self.frame4, text='Delete', command=self.delete)
        self.back_button = tk.Button(self.frame4, text='Back', command=self.delete_calendar_page.destroy)
        # Pack
        self.back_button.pack(side='right')
        self.delete_button.pack(side='right')
        self.search_button.pack(side='right')
        self.entry_search.pack(side='right')
        self.label_searchbar.pack(side='left')
        self.label_message.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

    def search(self):
        date = self.entry_search.get()
        if date not in self.calendar_data.keys():
            result = 'Not found'
            self.results.set(result)
        else:
            self.results.set(self.calendar_data[date])

    def delete(self):
        date = self.entry_search.get()
        self.calendar_data.pop(date)
        outfile = open('calendar.bat', 'wb')
        pickle.dump(self.calendar_data, outfile)
        outfile.close()
        self.results.set('Deleted')


class AllCalendarPage:
    def __init__(self, window):
        try:
            import_doc = open('calendar.bat', 'rb')
            self.calendar_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            # tk.messagebox.showerror('ERRor', 'File could not be found')
            self.calendar_data = {}
        self.all_calendar_gui = tk.Toplevel(window, cursor='heart')
        # Frames
        self.frame1 = tk.Frame(self.all_calendar_gui)  # Message
        self.frame2 = tk.Frame(self.all_calendar_gui)  # Results
        self.frame3 = tk.Frame(self.all_calendar_gui)  # Buttons
        # StringVar and Labels
        self.results = tk.StringVar()
        self.label_message = tk.Label(self.frame1, text='Calendar')
        self.label_result = tk.Label(self.frame2, textvariable=self.results)
        # Buttons
        self.show_button = tk.Button(self.frame3, text='show', command=self.show_results)
        self.hide_button = tk.Button(self.frame3, text='hide', command=self.hide_results)
        self.back_button = tk.Button(self.frame3, text='Back', command=self.all_calendar_gui.destroy)
        # Pack
        self.back_button.pack(side='right')
        self.hide_button.pack(side='right')
        self.show_button.pack(side='right')
        self.label_message.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

    def show_results(self):
        dict2 = {}
        for key in sorted(self.calendar_data):
            dict2[key] = self.calendar_data[key]
        self.results.set(str(dict2))

    def hide_results(self):
        self.results.set('')


class NewBoardPage:
    def __init__(self, window):
        try:
            import_doc = open('boards.bat', 'rb')
            self.board_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            # tk.messagebox.showerror('ERRor', 'File could not be found')
            self.board_data = {}
        self.new_board_gui = tk.Toplevel(window, cursor='heart')
        self.new_board_gui.geometry('500x150')
        # Frames
        self.frame1 = tk.Frame(self.new_board_gui)  # Message
        self.frame2 = tk.Frame(self.new_board_gui)  # cc:
        self.frame3 = tk.Frame(self.new_board_gui)  # Note
        self.frame4 = tk.Frame(self.new_board_gui)  # Confirm
        self.frame5 = tk.Frame(self.new_board_gui)  # Buttons
        # Labels
        self.results = tk.StringVar()
        self.label_message = tk.Label(self.frame1, text='New Board')
        self.label_name = tk.Label(self.frame2, text='cc: ')
        self.label_note = tk.Label(self.frame3, text='Note:')
        self.label_result = tk.Label(self.frame4, textvariable=self.results)
        # Entries
        self.entry_name = tk.Entry(self.frame2, width=20)
        self.entry_note = tk.Entry(self.frame3, width=20)
        # Buttons
        self.confirm_button = tk.Button(self.frame5, text='Confirm', command=self.confirm)
        self.back_button = tk.Button(self.frame5, text='Back', command=self.new_board_gui.destroy)
        # Pack
        self.confirm_button.pack(side='left')
        self.back_button.pack(side='right')
        self.entry_name.pack(side='right')
        self.entry_note.pack(side='right')
        self.label_message.pack(side='left')
        self.label_name.pack(side='left')
        self.label_note.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

    def confirm(self):
        name = self.entry_name.get()
        name = name.lower()
        note = self.entry_note.get()
        self.board_data[name] = {'name': name, 'note': note}
        output_file = open('boards.bat', 'wb')
        pickle.dump(self.board_data, output_file)
        output_file.close()
        self.results.set('Added!')


class EditBoardPage:
    def __init__(self, window):
        try:
            import_doc = open('boards.bat', 'rb')
            self.board_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            tk.messagebox.showerror('ERRor', 'File could not be found')
            self.board_data = {}
        self.edit_board_gui = tk.Toplevel(window, cursor='heart')
        self.edit_board_gui.geometry('500x150')
        # Frames
        self.frame1 = tk.Frame(self.edit_board_gui)  # Message
        self.frame2 = tk.Frame(self.edit_board_gui)  # Search
        self.frame3 = tk.Frame(self.edit_board_gui)  # cc
        self.frame4 = tk.Frame(self.edit_board_gui)  # note
        self.frame5 = tk.Frame(self.edit_board_gui)  # Results
        self.frame6 = tk.Frame(self.edit_board_gui)  # Buttons
        # StringVar
        self.results = tk.StringVar()
        self.search_name = tk.StringVar()
        self.search_note = tk.StringVar()
        # Labels
        self.label_searchbar = tk.Label(self.frame1, text='search')
        self.label_message = tk.Label(self.frame2, text='Edit Boards')
        self.label_name = tk.Label(self.frame3, text='Name: ')
        self.label_note = tk.Label(self.frame4, text='Note: ')
        # StringVar return
        self.search_name_label = tk.Label(self.frame3, textvariable=self.search_name)
        self.search_note_label = tk.Label(self.frame4, textvariable=self.search_note)
        self.label_result = tk.Label(self.frame5, textvariable=self.results)
        # Entries
        self.entry_search = tk.Entry(self.frame1, width=30)
        self.entry_name = tk.Entry(self.frame3, width=20)
        self.entry_note = tk.Entry(self.frame4, width=20)

        # Buttons
        self.search_button = tk.Button(self.frame1, text='search', command=self.search)
        self.confirm_button = tk.Button(self.frame6, text='Confirm', command=self.edit)
        self.back_button = tk.Button(self.frame6, text='Back', command=self.edit_board_gui.destroy)
        # Pack
        self.confirm_button.pack(side='left')
        self.back_button.pack(side='right')
        self.search_button.pack(side='right')
        self.entry_search.pack(side='right')
        self.entry_name.pack(side='right')
        self.entry_note.pack(side='right')
        self.label_message.pack(side='left')
        self.label_searchbar.pack(side='left')
        self.search_name_label.pack(side='left')
        self.search_note_label.pack(side='left')
        self.label_name.pack(side='left')
        self.label_note.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()

    def search(self):
        name = self.entry_search.get()
        name = name.lower()
        if name not in self.board_data.keys():
            result = 'Not found'
            self.results.set(result)
        else:
            note = self.board_data[name]['note']
            self.search_name.set(name)
            self.search_note.set(note)

    def edit(self):
        new_name = self.entry_name.get()
        new_name = new_name.lower()
        old_name = self.entry_search.get()
        old_name = old_name.lower()
        note = self.entry_note.get()
        try:
            if new_name != self.board_data[old_name]['name'] and new_name != '':
                name = new_name
            elif new_name == '':
                name = old_name
            else:
                name = self.board_data[old_name]['name']
            if note != self.board_data[old_name]['note'] and note != '':
                note = note
            else:
                note = self.board_data[old_name]['note']
            self.board_data.pop(old_name)
            self.board_data[name] = {'name': name, 'note': note}
            output_file = open("boards.bat", 'wb')
            pickle.dump(self.board_data, output_file)
            output_file.close()
            self.results.set('successfully updated')
        except IndexError:
            tk.messagebox.showerror('ERRor', 'You messed up')


class ViewBoardPage:
    def __init__(self, window):
        try:
            import_doc = open('boards.bat', 'rb')
            self.board_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            tk.messagebox.showerror('ERRor', 'File could not be found')
            self.board_data = {}
        self.view_boards_gui = tk.Toplevel(window, cursor='heart')
        self.view_boards_gui.geometry('500x150')
        # Frames
        self.frame1 = tk.Frame(self.view_boards_gui)  # Message
        self.frame2 = tk.Frame(self.view_boards_gui)  # Search
        self.frame3 = tk.Frame(self.view_boards_gui)  # Results
        self.frame4 = tk.Frame(self.view_boards_gui)  # Buttons
        # StringVar
        self.results = tk.StringVar()
        # Labels
        self.label_searchbar = tk.Label(self.frame1, text='search')
        self.label_message = tk.Label(self.frame2, text='Search Boards: ')
        # StringVar return
        self.label_result = tk.Label(self.frame3, textvariable=self.results)
        # Entries
        self.entry_search = tk.Entry(self.frame2, width=30)
        # Buttons
        self.search_button = tk.Button(self.frame2, text='search', command=self.search)
        self.back_button = tk.Button(self.frame4, text='Back', command=self.view_boards_gui.destroy)
        # Pack
        self.back_button.pack(side='right')
        self.search_button.pack(side='right')
        self.entry_search.pack(side='right')
        self.label_searchbar.pack(side='left')
        self.label_message.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

    def search(self):
        name = self.entry_search.get()
        name = name.lower()
        if name not in self.board_data.keys():
            result = 'Not found'
            self.results.set(result)
        else:
            string = 'cc: ' + str(self.board_data[name]['name']) + '\nNote: ' + str(self.board_data[name]['note'])
            self.results.set(string)


class DeleteBoardPage:
    def __init__(self, window):
        try:
            import_doc = open('boards.bat', 'rb')
            self.board_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            tk.messagebox.showerror('ERRor', 'File could not be found')
            self.board_data = {}
        self.delete_board_gui = tk.Toplevel(window, cursor='pirate')
        self.delete_board_gui.geometry('500x150')
        # Frames
        self.frame1 = tk.Frame(self.delete_board_gui)  # Message
        self.frame2 = tk.Frame(self.delete_board_gui)  # Search
        self.frame3 = tk.Frame(self.delete_board_gui)  # Results
        self.frame4 = tk.Frame(self.delete_board_gui)  # Buttons
        # StringVar
        self.results = tk.StringVar()
        # Labels
        self.label_searchbar = tk.Label(self.frame1, text='search')
        self.label_message = tk.Label(self.frame2, text='Delete Board')
        # StringVar return
        self.label_result = tk.Label(self.frame3, textvariable=self.results)
        # Entries
        self.entry_search = tk.Entry(self.frame1, width=30)
        # Buttons
        self.search_button = tk.Button(self.frame1, text='search', command=self.search)
        self.delete_button = tk.Button(self.frame4, text='Delete', command=self.delete)
        self.back_button = tk.Button(self.frame4, text='Back', command=self.delete_board_gui.destroy)
        # Pack
        self.back_button.pack(side='right')
        self.delete_button.pack(side='right')
        self.search_button.pack(side='right')
        self.entry_search.pack(side='right')
        self.label_searchbar.pack(side='left')
        self.label_message.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

    def search(self):
        name = self.entry_search.get()
        name = name.lower()
        if name not in self.board_data.keys():
            result = 'Not found'
            self.results.set(result)
        else:
            self.results.set(self.board_data[name])

    def delete(self):
        name = self.entry_search.get()
        name = name.lower()
        self.board_data.pop(name)
        outfile = open('boards.bat', 'wb')
        pickle.dump(self.board_data, outfile)
        outfile.close()
        self.results.set('Deleted')


class AllBoardsPage:
    def __init__(self, window):
        try:
            import_doc = open('boards.bat', 'rb')
            self.board_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            # tk.messagebox.showerror('ERRor', 'File could not be found')
            self.board_data = {}
        self.all_boards_gui = tk.Toplevel(window, cursor='heart')
        # Frames
        self.frame1 = tk.Frame(self.all_boards_gui)  # Message
        self.frame2 = tk.Frame(self.all_boards_gui)  # Results
        self.frame3 = tk.Frame(self.all_boards_gui)  # Buttons
        # StringVar and Labels
        self.results = tk.StringVar()
        self.label_message = tk.Label(self.frame1, text='Board')
        self.label_result = tk.Label(self.frame2, textvariable=self.results)
        # Buttons
        self.show_button = tk.Button(self.frame3, text='show', command=self.show_results)
        self.hide_button = tk.Button(self.frame3, text='hide', command=self.hide_results)
        self.back_button = tk.Button(self.frame3, text='Back', command=self.all_boards_gui.destroy)
        # Pack
        self.back_button.pack(side='right')
        self.hide_button.pack(side='right')
        self.show_button.pack(side='right')
        self.label_message.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

    def show_results(self):
        dict2 = {}
        for key in sorted(self.board_data):
            dict2[key] = self.board_data[key]
        self.results.set(str(dict2))

    def hide_results(self):
        self.results.set('')


class NewMeetingPage:
    def __init__(self, window):
        try:
            import_doc = open('meetings.bat', 'rb')
            self.meeting_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            tk.messagebox.showerror('ERROR', 'File could not be found')
            self.meeting_data = {}
        self.new_meeting_gui = tk.Toplevel(window, cursor='heart')
        self.new_meeting_gui.geometry('500x200')
        # Frames
        self.frame1 = tk.Frame(self.new_meeting_gui)  # Message
        self.frame2 = tk.Frame(self.new_meeting_gui)  # Day
        self.frame3 = tk.Frame(self.new_meeting_gui)  # Meeting Name
        self.frame4 = tk.Frame(self.new_meeting_gui)  # Info
        self.frame5 = tk.Frame(self.new_meeting_gui)  # Confirm
        self.frame6 = tk.Frame(self.new_meeting_gui)  # Buttons
        # Labels
        self.results = tk.StringVar()
        self.label_message = tk.Label(self.frame1, text='New Meeting')
        self.label_day = tk.Label(self.frame2, text='Day: ')
        self.label_meeting = tk.Label(self.frame3, text='Meeting: ')
        self.label_info = tk.Label(self.frame4, text='Info:')
        self.label_result = tk.Label(self.frame5, textvariable=self.results)
        # Entries
        self.entry_day = tk.Entry(self.frame2, width=20)
        self.entry_meeting = tk.Entry(self.frame3, width=20)
        self.entry_info = tk.Entry(self.frame4, width=20)
        # Buttons
        self.confirm_button = tk.Button(self.frame6, text='Confirm', command=self.confirm)
        self.back_button = tk.Button(self.frame6, text='Back', command=self.new_meeting_gui.destroy)
        # Pack
        self.confirm_button.pack(side='left')
        self.back_button.pack(side='right')
        self.entry_day.pack(side='right')
        self.entry_meeting.pack(side='right')
        self.entry_info.pack(side='right')
        self.label_message.pack(side='left')
        self.label_day.pack(side='left')
        self.label_meeting.pack(side='left')
        self.label_info.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()

    def confirm(self):
        day = self.entry_day.get()
        day = day.lower()
        meeting = self.entry_meeting.get()
        info = self.entry_info.get()
        self.meeting_data[day] = {'day': day, 'meeting': meeting, 'info': info}
        output_file = open('meetings.bat', 'wb')
        pickle.dump(self.meeting_data, output_file)
        output_file.close()
        self.results.set('Added!')


class EditMeetingPage:
    def __init__(self, window):
        try:
            import_doc = open('meetings.bat', 'rb')
            self.meeting_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            tk.messagebox.showerror('ERROR', 'File could not be found')
            self.meeting_data = {}
        self.edit_meeting_gui = tk.Toplevel(window, cursor='heart')
        self.edit_meeting_gui.geometry('500x200')
        # Frames
        self.frame1 = tk.Frame(self.edit_meeting_gui)  # Message
        self.frame2 = tk.Frame(self.edit_meeting_gui)  # Search
        self.frame3 = tk.Frame(self.edit_meeting_gui)  # Day
        self.frame4 = tk.Frame(self.edit_meeting_gui)  # Meeting
        self.frame5 = tk.Frame(self.edit_meeting_gui)  # Info
        self.frame6 = tk.Frame(self.edit_meeting_gui)  # Results
        self.frame7 = tk.Frame(self.edit_meeting_gui)  # Buttons
        # StringVar
        self.results = tk.StringVar()
        self.search_day = tk.StringVar()
        self.search_meeting = tk.StringVar()
        self.search_info = tk.StringVar()
        # Labels
        self.label_searchbar = tk.Label(self.frame1, text='search')
        self.label_message = tk.Label(self.frame2, text='Edit Meeting')
        self.label_day = tk.Label(self.frame3, text='Day:')
        self.label_meeting = tk.Label(self.frame4, text='Meeting: ')
        self.label_info = tk.Label(self.frame5, text='Info: ')
        # StringVar return
        self.search_day_label = tk.Label(self.frame3, textvariable=self.search_day)
        self.search_meeting_label = tk.Label(self.frame4, textvariable=self.search_meeting)
        self.search_info_label = tk.Label(self.frame5, textvariable=self.search_info)
        self.label_result = tk.Label(self.frame6, textvariable=self.results)
        # Entries
        self.entry_search = tk.Entry(self.frame1, width=30)
        self.entry_day = tk.Entry(self.frame3, width=20)
        self.entry_meeting = tk.Entry(self.frame4, width=20)
        self.entry_info = tk.Entry(self.frame5, width=20)

        # Buttons
        self.search_button = tk.Button(self.frame1, text='search', command=self.search)
        self.confirm_button = tk.Button(self.frame7, text='Confirm', command=self.edit)
        self.back_button = tk.Button(self.frame7, text='Back', command=self.edit_meeting_gui.destroy)
        # Pack
        self.confirm_button.pack(side='left')
        self.back_button.pack(side='right')
        self.search_button.pack(side='right')
        self.entry_search.pack(side='right')
        self.entry_day.pack(side='right')
        self.entry_meeting.pack(side='right')
        self.entry_info.pack(side='right')
        self.label_message.pack(side='left')
        self.label_searchbar.pack(side='left')
        self.search_day_label.pack(side='left')
        self.search_meeting_label.pack(side='left')
        self.search_info_label.pack(side='left')
        self.label_day.pack(side='left')
        self.label_meeting.pack(side='left')
        self.label_info.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.frame7.pack()

    def search(self):
        day = self.entry_search.get()
        day = day.lower()
        if day not in self.meeting_data.keys():
            result = 'Not found'
            self.results.set(result)
        else:
            meeting = self.meeting_data[day]['meeting']
            info = self.meeting_data[day]['info']
            self.search_day.set(day)
            self.search_meeting.set(meeting)
            self.search_info.set(info)

    def edit(self):
        new_day = self.entry_day.get()
        new_day = new_day.lower()
        old_day = self.entry_search.get()
        old_day = old_day.lower()
        meeting = self.entry_meeting.get()
        info = self.entry_info.get()
        try:
            if new_day != self.meeting_data[old_day]['day'] and new_day != '':
                day = new_day
            elif new_day == '':
                day = old_day
            else:
                day = self.meeting_data[old_day]['day']
            if meeting != self.meeting_data[old_day]['meeting'] and meeting != '':
                meeting = meeting
            else:
                meeting = self.meeting_data[old_day]['meeting']
            if info != self.meeting_data[old_day]['info'] and info != '':
                info = info
            else:
                info = self.meeting_data[old_day]['info']
            self.meeting_data.pop(old_day)
            self.meeting_data[day] = {'day': day, 'meeting': meeting, 'info': info}
            output_file = open("meetings.bat", 'wb')
            pickle.dump(self.meeting_data, output_file)
            output_file.close()
            self.results.set('successfully updated')
        except IndexError:
            tk.messagebox.showerror('ERROR', 'Go to a meeting')


class ViewMeetingPage:
    def __init__(self, window):
        try:
            import_doc = open('meetings.bat', 'rb')
            self.meeting_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            tk.messagebox.showerror('ERROR', 'File could not be found')
            self.meeting_data = {}
        self.view_meeting_gui = tk.Toplevel(window, cursor='heart')
        self.view_meeting_gui.geometry('500x200')
        # Frames
        self.frame1 = tk.Frame(self.view_meeting_gui)  # Message
        self.frame2 = tk.Frame(self.view_meeting_gui)  # Search
        self.frame3 = tk.Frame(self.view_meeting_gui)  # Results
        self.frame4 = tk.Frame(self.view_meeting_gui)  # Buttons
        # StringVar
        self.results = tk.StringVar()
        # Labels
        self.label_searchbar = tk.Label(self.frame1, text='search')
        self.label_message = tk.Label(self.frame2, text='Search Meetings: ')
        # StringVar return
        self.label_result = tk.Label(self.frame3, textvariable=self.results)
        # Entries
        self.entry_search = tk.Entry(self.frame2, width=30)
        # Buttons
        self.search_button = tk.Button(self.frame2, text='search', command=self.search)
        self.back_button = tk.Button(self.frame4, text='Back', command=self.view_meeting_gui.destroy)
        # Pack
        self.back_button.pack(side='right')
        self.search_button.pack(side='right')
        self.entry_search.pack(side='right')
        self.label_searchbar.pack(side='left')
        self.label_message.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

    def search(self):
        day = self.entry_search.get()
        day = day.lower()
        if day not in self.meeting_data.keys():
            result = 'Not found'
            self.results.set(result)
        else:
            string = 'Day: ' + str(self.meeting_data[day]['day']) + '\nMeeting: ' + str(self.meeting_data[day]['meeting']) + '\nInfo: ' + str(self.meeting_data[day]['info'])
            self.results.set(string)


class DeleteMeetingPage:
    def __init__(self, window):
        try:
            import_doc = open('meetings.bat', 'rb')
            self.meeting_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            tk.messagebox.showerror('ERROR', 'File could not be found')
            self.meeting_data = {}
        self.delete_meeting_gui = tk.Toplevel(window, cursor='pirate')
        self.delete_meeting_gui.geometry('500x200')
        # Frames
        self.frame1 = tk.Frame(self.delete_meeting_gui)  # Message
        self.frame2 = tk.Frame(self.delete_meeting_gui)  # Search
        self.frame3 = tk.Frame(self.delete_meeting_gui)  # Results
        self.frame4 = tk.Frame(self.delete_meeting_gui)  # Buttons
        # StringVar
        self.results = tk.StringVar()
        # Labels
        self.label_searchbar = tk.Label(self.frame1, text='search')
        self.label_message = tk.Label(self.frame2, text='Delete Meeting')
        # StringVar return
        self.label_result = tk.Label(self.frame3, textvariable=self.results)
        # Entries
        self.entry_search = tk.Entry(self.frame1, width=30)
        # Buttons
        self.search_button = tk.Button(self.frame1, text='search', command=self.search)
        self.delete_button = tk.Button(self.frame4, text='Delete', command=self.delete)
        self.back_button = tk.Button(self.frame4, text='Back', command=self.delete_meeting_gui.destroy)
        # Pack
        self.back_button.pack(side='right')
        self.delete_button.pack(side='right')
        self.search_button.pack(side='right')
        self.entry_search.pack(side='right')
        self.label_searchbar.pack(side='left')
        self.label_message.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

    def search(self):
        day = self.entry_search.get()
        day = day.lower()
        if day not in self.meeting_data.keys():
            result = 'Not found'
            self.results.set(result)
        else:
            self.results.set(self.meeting_data[day])

    def delete(self):
        day = self.entry_search.get()
        day = day.lower()
        self.meeting_data.pop(day)
        outfile = open('meetings.bat', 'wb')
        pickle.dump(self.meeting_data, outfile)
        outfile.close()
        self.results.set('Deleted')


class AllMeetingsPage:
    def __init__(self, window):
        try:
            import_doc = open('meetings.bat', 'rb')
            self.meeting_data = pickle.load(import_doc)
            import_doc.close()
        except FileNotFoundError:
            # tk.messagebox.showerror('ERRor', 'File could not be found')
            self.meeting_data = {}
        self.all_meeting_gui = tk.Toplevel(window, cursor='heart')
        # Frames
        self.frame1 = tk.Frame(self.all_meeting_gui)  # Message
        self.frame2 = tk.Frame(self.all_meeting_gui)  # Results
        self.frame3 = tk.Frame(self.all_meeting_gui)  # Buttons
        # StringVar and Labels
        self.results = tk.StringVar()
        self.label_message = tk.Label(self.frame1, text='Meetings')
        self.label_result = tk.Label(self.frame2, textvariable=self.results)
        # Buttons
        self.show_button = tk.Button(self.frame3, text='show', command=self.show_results)
        self.back_button = tk.Button(self.frame3, text='Back', command=self.all_meeting_gui.destroy)
        # Pack
        self.back_button.pack(side='right')
        self.show_button.pack(side='right')
        self.label_message.pack(side='left')
        self.label_result.pack(side='left')
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

    def show_results(self):
        dict2 = {}
        for key in sorted(self.meeting_data):
            dict2[key] = self.meeting_data[key]
        self.results.set(str(dict2))


def main():
    root = tk.Tk()
    MenuGUI(root)
    root.mainloop()


main()
