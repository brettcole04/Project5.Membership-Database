from peewee import *
from tkinter import*
from tkinter import ttk
import tkinter.messagebox

db = SqliteDatabase('testmembership.db')

class Member(Model):
    ''' creates each collumn name for datebase, and sets values
        types for each entry'''
    last_name = CharField(null = True)
    first_name = CharField(null = True)
    birth_date = DateField(null = True)
    license_num = CharField(null = True)
    street = CharField(null = True)
    city = CharField(null = True)
    state = CharField(null = True)
    zip_ = IntegerField(null = True)    
    cell_phone_num = IntegerField(null = True)
    employer = CharField(null = True)
    email = CharField(null = True)
    
    
    class Meta:
        '''creates the main table that uses variables from class Member'''
        database = db
        db_table = 'members'
        

def save():
    '''Pulls user input from entry fields and inserts into
        appropriate fields in database'''   
    try:
        en_mem = Member.create(last_name = e1.get().title(),
                               first_name = e2.get().title(),
                               birth_date = e3.get().title(),
                               license_num = e4.get().title(),
                               street = e5.get().title(),
                               city = e6.get().title(),
                               state = e7.get().upper(),
                               zip_ = e8.get().title(),
                               cell_phone_num = e9.get().title(),
                               employer = e10.get().title(),
                               email = e11.get().title())
        save_complete()
    except ValueError:
        error_message()#informs user that entry f
        clear_boxes()#resets to empty
    
    
def save_complete():
    '''displays a save dialog'''
    tkinter.messagebox.showinfo("Member Info Save", "Your Save Was Successful")

    
def error_message():
    '''displays error message when fields are not correct'''
    tkinter.messagebox.showerror("Error", "Make Sure all Fields are Correct")


def member_list_display():
    '''Pulls data from database table, and inserts it into an uneditable user display'''
    
    root = Tk(className = " Member Information")
    #places and up/down scroll bar on the right, for when database gets larger
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)    
    tree = ttk.Treeview(root, yscrollcommand=scrollbar.set)
    #creates the columns for which you insert data
    tree["columns"] = ("one","two","three", "four","five","six", "seven",
                       "eight", "nine", "ten", "eleven")
    #Setting up the treeview dimensions
    tree.column("one", width=50, anchor='center')
    tree.column("two", width=100, anchor='center')
    tree.column("three", width=100, anchor='center')
    tree.column("four", width=120, anchor='center')
    tree.column("five", width=140, anchor='center')
    tree.column("six", width=100, anchor='center')
    tree.column("seven", width=50, anchor='center')
    tree.column("eight", width=50, anchor='center')
    tree.column("nine", width=100, anchor='center')
    tree.column("ten", width=100, anchor='center')
    tree.column("eleven", width=180, anchor='center')
    #setting the names of each column 
    tree.heading("one", text="Last Name")
    tree.heading("two", text="First Name")
    tree.heading("three", text="BirthDate")
    tree.heading("four", text="License Number")
    tree.heading("five", text="Street")
    tree.heading("six", text="City")
    tree.heading("seven", text="State")
    tree.heading("eight", text="Zip Code")
    tree.heading("nine", text="Cell Phone")
    tree.heading("ten", text="Employer")
    tree.heading("eleven", text="Email")
    tree.pack(side=LEFT, fill=BOTH)   
    scrollbar.config(command=tree.yview)

    #pulls data from our database table and inserts into treeview for user-end display
    text_ent = 0
    for member in Member.select():
        text_ent += 1
        tree.insert("" , 0, text= text_ent, values=(member.last_name, member.first_name,
                                                       member.birth_date, member.license_num,
                                                       member.street, member.city,member.state,
                                                       member.zip_, member.cell_phone_num,
                                                       member.employer, member.email))
    
    root.geometry('1200x250+150+150')
    root.config(bg='grey87')
    mainloop()
    


def clear_boxes():
    '''resets all entry fields'''
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    e11.delete(0,END)



if __name__ == '__main__':
    '''connect to database, and creates the Member table that is outlined in class Member(Model)'''
    db.connect()
    db.create_tables([Member], safe = True)
    
    
master = Tk(className = "The Memberlist")##main window
#labels on main window
last = Label(master,  text= "Last Name:",font = ('times', 16), bg = 'grey87').grid(row = 0, column = 0)#e1
first = Label(master, text= "First Name:", font = ('times', 16), bg = 'grey87').grid(row = 0, column = 2)#e2
license_num = Label(master, text = "License Number:", font = ('times', 16), bg='grey87').grid(row = 1, column = 2)#e3
street = Label(master, text = "Street Address:", font = ('times', 16), bg = 'grey87').grid(row = 2, column = 0)#e4
city = Label(master, text = "City:", font = ('times', 16),bg ='grey87').grid(row = 2, column = 2)#e5
state = Label(master, text = "State:", font = ('times', 16),bg ='grey87').grid(row = 3, column = 0)#e6
zip_code = Label(master, text = "Zip Code:", font=('times', 16), bg ='grey87').grid(row = 3, column = 2)#e7
birth_date = Label(master, text = 'Birth Date(YY-MM-DD):', font = ('times', 16), bg = 'grey87').grid(row = 1, column = 0)#e8
cell_phone = Label(master, text = "Cell Phone(9101234567):", font = ('times', 16), bg = 'grey87').grid(row = 4, column = 0)#e9
employer = Label(master, text = "Employer Name:", font = ('times', 16), bg = 'grey87').grid(row = 4,column = 2)#e10
email = Label(master, text = "Email Address:", font=('times', 16), bg ='grey87').grid(row = 5, column = 0)#11

master.resizable(False,False)
master.geometry('900x250+150+150')
master.config(bg='grey87')

e1 = Entry(master, highlightbackground='grey87')#.grid(row=0, column=1)#last
e2 = Entry(master, highlightbackground='grey87')#.grid(row=0, column=3)#first
e3 = Entry(master, highlightbackground='grey87')#.grid(row=1, column=1)#birthday
e4 = Entry(master, highlightbackground='grey87')#.grid(row=1, column=3)#license
e5 = Entry(master, highlightbackground='grey87')#.grid(row=2, column=1)#street
e6 = Entry(master, highlightbackground='grey87')#.grid(row=2, column=3)#city
e7 = Entry(master, highlightbackground='grey87')#.grid(row=3, column=1)#state
e8 = Entry(master, highlightbackground='grey87')#.grid(row=3, column=3)#zip
e9 = Entry(master, highlightbackground='grey87')#.grid(row=4, column=1)#cell
e10 = Entry(master, highlightbackground='grey87')#.grid(row=4, column=3)#employer
e11 = Entry(master, highlightbackground='grey87')#.grid(row=5, column=1)#email

e1.grid(row = 0, column = 1)#last
e2.grid(row = 0, column = 3)#first
e3.grid(row = 1, column = 1)#birthday
e4.grid(row = 1, column = 3)#license
e5.grid(row = 2, column = 1)#street
e6.grid(row = 2, column = 3)#city
e7.grid(row = 3, column = 1)#state
e8.grid(row = 3, column = 3)#zip
e9.grid(row = 4, column = 1)#cell
e10.grid(row = 4, column = 3)#employer
e11.grid(row = 5, column = 1)#email

b2 = Button(master, text="SAVE", highlightbackground = 'grey87', command = save).grid(row = 5, column = 3)
b3 = Button(master, text="Member List", highlightbackground = 'grey87', command = member_list_display)
b4 = Button(master, text="Clear All Text", highlightbackground = 'grey87', command = clear_boxes)

#b2.grid(row = 5, column = 3)
b3.grid(row = 15, column = 0)
b4.grid(row = 15, column = 4)
l1 = Label(master, text= '"\u00AE" Brett Cole and Bryan Marzoff Class Project. Spring 2017', font = ('times', 9),
           bg = 'grey87').grid(row = 17, column = 2)

master.mainloop()


    
        
