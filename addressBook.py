"""
Synopsis:
Project Name:-
    Address Book App (Version 1.0)
Software Details:-
    Operating System: Windows 10
    Python Version: 3.9.1
Project Details:-
    The following is an address-book app.
    It contains the Name, Contact Number, Address and Email id of the user.
    It can be used to add, update, delete and search for a particular data set.
    Data is stored in a csv file.
"""
from tkinter import *
from tkinter.scrolledtext import ScrolledText
length=0
details=[]
main_win=Tk()
main_win.title("Address Book App")
window_width = 600
window_height = 400
# get the screen dimension
screen_width = main_win.winfo_screenwidth() #RETURNS LAPTOP SCREENWIDTH
screen_height = main_win.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - window_width / 2) #STARTING X POINT OF THE WINDOW
center_y = int(screen_height/2 - window_height / 2)
main_win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
main_win.resizable(False, False)
def addEntry():
    """
    The function is called when the 'Add Entry' button in the main window is clicked. It opens a new window where the
    respective entry fields are to be filled. A error window is displayed for the following cases: Repeated names, names containing numbers or special characters,
    contact number of other than 10 digits, email id not containing '@' and '.' and if the default given value of the
    entry field is not cleared.If all the constraints are satisifed, upon clicking 'Add' the function adds the new
    entry to the csv file
    """
    f1 = open('address_book.csv', 'r')
    rows,det=[],[]
    for detail in f1:
        rows+=[detail.strip()]
    for i in rows:
        det+=[i.split(',')]
    f1.close()
    #print(rows)
    #print(det)
    #length = len(det)
    #print(length, det)
    add_win=Toplevel(main_win)
    add_win.title("Add New Entry")
    window_width = 600
    window_height = 300
    # get the screen dimension
    screen_width = add_win.winfo_screenwidth()
    screen_height = add_win.winfo_screenheight()
    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    add_win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    add_win.resizable(False, False)
    def add_value():
        n=name.get()
        c=contact.get()
        a=address.get('1.0',"end-1c")
        ad=a.replace(',',' ')
        e=email.get()
        f = open('address_book.csv', 'a')
        x=False
        y=False
        special_characters = r'!@#$%^&*()-+?_=,<>/'
        if c=='enter your contact number' or n=='enter your name' or a=='enter your address' or e=='enter your email id':
            x=False
            y=False

        if (c != 'enter your contact number' and True) and (n != 'enter your name' and True) and (a != 'enter your address' and True) and (e != 'enter your email id' and True):
            if not(any(ch.isdigit() for ch in n)):
                if not(any(charac in special_characters for charac in n)):
                    if len(c)==10 and ('@' and '.' in e) and (c.isdigit()==True):
                        x=True
                        y=True
        for j in det:
            if n.upper() == j[0].upper():
                #print("exists")
                y=False
                #print("y should have become false", y)
                break
        #print(y)
        if x==True and y==True:
            f.write(n + "," + c + "," + ad + "," + e)
            f.write("\n")
            f.close()
            add_win.destroy()

        if x==False or y==False:
            #print("x is false and error is displayed")
            error_win = Toplevel(add_win)
            # error_win = Tk()
            error_win.title("ERROR")
            window_width = 200
            window_height = 200
            # get the screen dimension
            screen_width = error_win.winfo_screenwidth()
            screen_height = error_win.winfo_screenheight()
            # find the center point
            center_x = int(screen_width / 2 - window_width / 2)
            center_y = int(screen_height / 2 - window_height / 2)
            error_win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
            error_win.resizable(False, False)
            if x==False:
                #print("x is ",x)
                #print("y is ",y)
                error = Label(error_win, text="INVALID ENTRY!!")
                error.place(x=60, y=70)
                close = Button(error_win, text="Close", command=error_win.destroy)
                close.place(x=80, y=100)
            elif y==False:
                #print("x is ", x)
                #print("y is ", y)
                error = Label(error_win, text="ENTRY ALREADY EXISTS!!")
                error.place(x=35, y=70)
                close = Button(error_win, text="Close", command=error_win.destroy)
                close.place(x=80, y=100)
                #elif x==False and y==False:
                #error = Label(error_win, text="INVALID ENTRY!!")
                #error.place(x=60, y=70)
                #close = Button(error_win, text="Close", command=error_win.destroy)
                #close.place(x=80, y=100)
            error_win.mainloop()

    Name = Label(add_win, text="Name :")
    Name.place(x=5, y=10, height=30)
    name = Entry(add_win, width=50)
    name.place(x=110, y=10, width=450, height=30)
    name.insert(0, 'enter your name')
    Contact = Label(add_win, text="Contact Number :")
    Contact.place(x=5, y=50, height=30)
    contact = Entry(add_win, width=50)
    contact.place(x=110, y=50, width=450, height=30)
    contact.insert(0, 'enter your contact number')
    Address = Label(add_win, text="Address :")
    Address.place(x=5, y=90, height=30)
    address = Text(add_win, height=4,font=('calibri',10))
    address.place(x=110, y=90, width=450, height=90)
    address.insert('1.0','enter your address')
    Email = Label(add_win, text="Email Id :")
    Email.place(x=5, y=190, height=30)
    email = Entry(add_win, width=50)
    email.place(x=110, y=190, width=450, height=30)
    email.insert(0, 'enter your email id')
    submit = Button(add_win, text="Add", command=add_value)
    submit.place(x=220, y=225)
    Quit_add = Button(add_win, text="Quit", command=add_win.destroy)
    Quit_add.place(x=320, y=225)
    add_win.mainloop()

def selectEntry():
    """
    The function is called when 'Update Entry' button in the main window is clicked. The required entry is fetched by
    the name user has entered in the search box. Upon entering an unacceptable value for a particular detail, an error is shown.
    Upon clicking update, the new details are overwritten in the csv file over the old ones.
    """
    select_entry_win= Toplevel(main_win)
    select_entry_win.title("Update Existing Entry")
    window_width = 500
    window_height = 150
    # get the screen dimension
    screen_width = select_entry_win.winfo_screenwidth()
    screen_height = select_entry_win.winfo_screenheight()
    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    select_entry_win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    select_entry_win.resizable(False, False)

    def updateEntry():
        update_win = Toplevel(select_entry_win)
        update_win.title("Update Existing Entry")
        window_width = 600
        window_height = 200
        # get the screen dimension
        screen_width = update_win.winfo_screenwidth()
        screen_height = update_win.winfo_screenheight()
        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        update_win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        update_win.resizable(False, False)
        n = update_entry.get()
        Name = Label(update_win, text="Name :")
        Name.place(x=5, y=10, height=30)
        name = Entry(update_win, width=50)
        name.place(x=110, y=10, width=400, height=30)
        Contact = Label(update_win, text="Contact Number :")
        Contact.place(x=5, y=50, height=30)
        contact = Entry(update_win, width=50)
        contact.place(x=110, y=50, width=400, height=30)
        Address = Label(update_win, text="Address :")
        Address.place(x=5, y=90, height=30)
        address = Entry(update_win, width=50)
        address.place(x=110, y=90, width=400, height=30)
        Email = Label(update_win, text="Email Id :")
        Email.place(x=5, y=130, height=30)
        email = Entry(update_win, width=50)
        email.place(x=110, y=130, width=400, height=30)
        notfound=False
        f1 = open('address_book.csv', 'r')
        rows, det = [], []
        for detail in f1:
            rows += [detail.strip()]
        for i in rows:
            det += [i.split(',')]
        f1.close()
        #length = len(det)
        #print(det)
        for j in det:
            if n.upper() == j[0].upper():
                name.insert(0, j[0]) #TO DISPLAY THE ALREADY EXISTING VALUES
                contact.insert(0, j[1])
                address.insert(0, j[2])
                email.insert(0, j[3])
                notfound=False
                break
            else:
                notfound=True

        def update_value():
            """
            this function is called when 'update' button is pressed after updating values
            """
            f1 = open('address_book.csv', 'r')
            rows, det = [], []
            for detail in f1:
                rows += [detail.strip()]
            for i in rows:
                det += [i.split(',')]
            #length = len(det)
            #print(length, det)
            x=False
            for j in det:
                n = name.get()
                if n.upper() == j[0].upper():
                    c = contact.get()
                    a = address.get()
                    ad = a.replace(',', ' ')
                    e = email.get()

                    special_characters = r'!@#$%^&*()-+?_=,<>/'
                    if (c != 'enter your contact number' and True) and (n != 'enter your name' and True) and (
                            a != 'enter your address' and True) and (e != 'enter your email id' and True):
                        if not (any(ch.isdigit() for ch in n)):
                            if not (any(charac in special_characters for charac in n)):
                                if len(c) == 10 and ('@' and '.' in e):
                                    for k in c:
                                        if ord(k) in range(48, 58):
                                            x = True
            if x==True:
                f = open('address_book.csv', 'w')
                #print("x is ",x)
                for k in det:
                    if n.upper() == k[0].upper():
                        det.remove(k)
                        break
                for i in det:
                    for k in i:
                        if k == i[-1]:
                            f.write(k)
                        else:
                            f.write(k + ',')
                    f.write("\n")
                f.write(n + "," + c + "," + ad + "," + e)
                f.write("\n")
                f.close()
                update_win.destroy()

            else:
                #print("x is ", x)
                error_win = Toplevel(update_win)
                # error_win = Tk()
                error_win.title("ERROR")
                window_width = 200
                window_height = 200
                # get the screen dimension
                screen_width = error_win.winfo_screenwidth()
                screen_height = error_win.winfo_screenheight()
                # find the center point
                center_x = int(screen_width / 2 - window_width / 2)
                center_y = int(screen_height / 2 - window_height / 2)
                error_win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
                error_win.resizable(False, False)
                error = Label(error_win, text="INVALID ENTRY!!")
                error.place(x=60, y=70)
                close = Button(error_win, text="Close", command=error_win.destroy)
                close.place(x=80, y=100)
                error_win.mainloop()
            f1 = open('address_book.csv', 'r')
            rows, det = [], []
            for detail in f1:
                rows += [detail.strip()]
            for i in rows:
                det += [i.split(',')]
            f1.close()
            #length = len(det)
            #print(length, det)
        submit = Button(update_win, text="Update",command=update_value)
        submit.place(x=200, y=165)
        Quit_update = Button(update_win, text="Quit", command=update_win.destroy)
        Quit_update.place(x=300, y=165)
        if notfound==True:
            not_found = Label(select_entry_win, text="ENTRY NOT FOUND!!")
            not_found.place(x=190, y=60, height=30)
            update_win.destroy()
        update_win.mainloop()

    Name = Label(select_entry_win, text=" Enter Name :")
    Name.place(x=5, y=10, height=30)
    update_entry = Entry(select_entry_win, width=50)
    update_entry.place(x=110, y=10, width=350, height=30)
    select = Button(select_entry_win, text="Select",command=updateEntry)
    select.place(x=180, y=window_height-50)
    Quit_select = Button(select_entry_win, text="Quit", command=select_entry_win.destroy)
    Quit_select.place(x=300, y=window_height-50)
    select_entry_win.mainloop()

def deleteEntry():
    """
    The function provides a search window, where the name of the to-be deleted entry is entered. The function searches
    and deletes the respective entry and upon completion the particular entry is removed from the csv file. If a
    non-existing name is entered, a "entry not found" error is displayed through a label.
    """

    f1 = open('address_book.csv', 'r')
    rows, det = [], []
    for detail in f1:
        rows += [detail.strip()]
    for i in rows:
        det += [i.split(',')]
    f1.close()
    #length = len(det)
    #print(length, det)
    delete_win = Toplevel(main_win)
    delete_win.title("Delete Existing Entry")
    window_width = 500
    window_height = 150
    # get the screen dimension
    screen_width = delete_win.winfo_screenwidth()
    screen_height = delete_win.winfo_screenheight()
    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    delete_win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    delete_win.resizable(False, False)

    def delete_Entry():
        n = delete_entry.get()
        notfound = False
        f = open('address_book.csv', 'w')

        for j in det:
            if n.upper() == j[0].upper():
                det.remove(j)
                #print(det)
                delete_win.destroy()
                notfound=False
                break
            else:
                notfound=True

        for i in det:
            for k in i:
                if k==i[-1]:
                    f.write(k)
                else:
                    f.write(k + ',')
            f.write("\n")

        f.close()
        if notfound==True:
            not_found = Label(delete_win, text="ENTRY NOT FOUND!!")
            not_found.place(x=190, y=60, height=30)

    Name = Label(delete_win, text=" Enter Name :")
    Name.place(x=5, y=10, height=30)
    delete_entry = Entry(delete_win, width=50)
    delete_entry.place(x=110, y=10, width=350, height=30)
    select = Button(delete_win, text="Delete", command=delete_Entry)
    select.place(x=180, y=window_height - 50)
    Quit_select = Button(delete_win, text="Quit", command=delete_win.destroy)
    Quit_select.place(x=300, y=window_height - 50)
    delete_win.mainloop()

def searchEntry():
    """
    Upon clicking the search entry button the function displays the Search entry window with buttoned options to
    search using any detail pertaining to the entry. The complete details of the respective entry is displayed upon clicking Search.
    If no entry is found it displays an 'entry not found error'. An entry can be searched using name, contact, address or email id.
    """
    f1 = open('address_book.csv', 'r')
    rows, det = [], []
    for detail in f1:
        rows += [detail.strip()]
    for i in rows:
        det += [i.split(',')]
    f1.close()
    #length = len(det)
    #print(length, det)
    search_win = Toplevel(main_win)
    search_win.title("Search Existing Entry")
    window_width = 500
    window_height = 350
    # get the screen dimension
    screen_width = search_win.winfo_screenwidth()
    screen_height = search_win.winfo_screenheight()
    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    search_win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    search_win.resizable(False, False)

    f1 = open('address_book.csv', 'r')
    rows, det = [], []
    for detail in f1:
        rows += [detail.strip()]
    for i in rows:
        det += [i.split(',')]
    headings=['Name: ','Contact Number: ','Address: ','Email Id: ']

    def search_name():
        """The function is called when search by name is clicked"""
        search_name_win = Toplevel(search_win)
        search_name_win.title("Search Existing Entry")
        window_width = 600
        window_height = 300
        # get the screen dimension
        screen_width = search_name_win.winfo_screenwidth()
        screen_height = search_name_win.winfo_screenheight()
        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        search_name_win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        search_name_win.resizable(False, False)
        entry = ScrolledText(search_name_win, wrap=WORD, width=40, height=10)
        entry.place(x=110,y=50,width= 415)
        def get_name():
            n=name.get()
            n=n.upper()
            c=0
            for j in det:
                if n in j[0].upper():
                    for k in j:
                        c+=1
                        entry.insert(INSERT, headings[j.index(k)]+k+"\n")
                    entry.insert(INSERT,"\n")
            if c==0:
                entry.insert(INSERT, "ENTRY NOT FOUND!!!/n")
                entry.configure(state ='disabled')

        Name = Label(search_name_win, text=" Enter Name :")
        Name.place(x=5, y=10, height=30)
        name = Entry(search_name_win, width=50)
        name.place(x=110, y=10, width=400, height=30)

        submit = Button(search_name_win, text="Get Entry", command=get_name)
        submit.place(x=200, y=250)
        Quit_search_name = Button(search_name_win, text="Quit", command=search_name_win.destroy)
        Quit_search_name.place(x=300, y=250)
        search_name_win.mainloop()

    def search_contact():
        """This function is called when search by contact is clicked"""
        search_contact_win = Toplevel(search_win)
        search_contact_win.title("Search Existing Entry")
        window_width = 600
        window_height = 300
        # get the screen dimension
        screen_width = search_contact_win.winfo_screenwidth()
        screen_height = search_contact_win.winfo_screenheight()
        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        search_contact_win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        search_contact_win.resizable(False, False)
        entry = ScrolledText(search_contact_win, wrap=WORD, width=40, height=10)
        entry.place(x=110, y=50, width=415)
        def get_contact():
            c=contact.get()
            count=0
            for j in det:
                if j[1]==c:
                    for k in j:
                        entry.insert(INSERT, headings[j.index(k)] + str(k) + "\n")
                        count+=1
                    entry.insert(INSERT,"\n")

            if count==0:
                entry.insert(INSERT, "ENTRY NOT FOUND!!!")
                entry.configure(state='disabled')

        Contact = Label(search_contact_win, text=" Enter Contact :")
        Contact.place(x=5, y=10, height=30)
        contact = Entry(search_contact_win, width=50)
        contact.place(x=110, y=10, width=400, height=30)

        submit = Button(search_contact_win, text="Get Entry", command=get_contact)
        submit.place(x=200, y=250)
        Quit_search_contact = Button(search_contact_win, text="Quit", command=search_contact_win.destroy)
        Quit_search_contact.place(x=300, y=250)
        search_contact_win.mainloop()

    def search_address():
        """This function is called when search by address is clicked"""
        search_address_win = Toplevel(search_win)
        search_address_win.title("Search Existing Entry")
        window_width = 600
        window_height = 300
        # get the screen dimension
        screen_width = search_address_win.winfo_screenwidth()
        screen_height = search_address_win.winfo_screenheight()
        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        search_address_win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        search_address_win.resizable(False, False)
        entry = ScrolledText(search_address_win, wrap=WORD, width=40, height=10)
        entry.place(x=110, y=70, width=415)
        def get_address():
            a = address.get('1.0',"end-1c")
            a = a.upper()
            ad = a.replace(',', ' ')
            c=0
            for j in det:
                if ad in j[2].upper():
                    for k in j:
                        entry.insert(INSERT, headings[j.index(k)] + str(k) + "\n")
                        c+=1
                    entry.insert(INSERT,"\n")

            if c == 0:
                entry.insert(INSERT, "ENTRY NOT FOUND!!!")
                entry.configure(state='disabled')

        Address = Label(search_address_win, text=" Enter Address :")
        Address.place(x=5, y=10, height=30)
        address = Text(search_address_win, height=4, font=('calibri', 10))
        address.place(x=110, y=10, width=400, height=50)

        submit = Button(search_address_win, text="Get Entry", command=get_address)
        submit.place(x=200, y=250)
        Quit_search_address = Button(search_address_win, text="Quit", command=search_address_win.destroy)
        Quit_search_address.place(x=300, y=250)
        search_address_win.mainloop()

    def search_email():
        """ This function is called when search by email is clicked"""
        search_email_win = Toplevel(search_win)
        search_email_win.title("Search Existing Entry")
        window_width = 600
        window_height = 300
        # get the screen dimension
        screen_width = search_email_win.winfo_screenwidth()
        screen_height = search_email_win.winfo_screenheight()
        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        search_email_win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        search_email_win.resizable(False, False)
        entry = ScrolledText(search_email_win, wrap=WORD, width=40, height=10)
        entry.place(x=110, y=50, width=415)
        def get_email():
            e=email.get()
            c=0
            for j in det:
                if j[3] == e:

                    for k in j:
                        entry.insert(INSERT, headings[j.index(k)] + str(k) + "\n")
                        c+=1
                    entry.insert(INSERT,"\n")

            if c == 0:
                entry.insert(INSERT, "ENTRY NOT FOUND!!!")
                entry.configure(state='disabled')

        Email = Label(search_email_win, text=" Enter Email Id :")
        Email.place(x=5, y=10, height=30)
        email = Entry(search_email_win, width=50)
        email.place(x=110, y=10, width=400, height=30)

        submit = Button(search_email_win, text="Get Entry", command=get_email)
        submit.place(x=200, y=250)
        Quit_search_win = Button(search_email_win, text="Quit", command=search_email_win.destroy)
        Quit_search_win.place(x=300, y=250)
        search_email_win.mainloop()
    f1.close()
    l1 = Label(search_win, text="")
    l1.pack()
    l = Label(search_win, text="Search By:")
    l.pack()
    l1 = Label(search_win, text="")
    l1.pack()
    add = Button(search_win, text="Name", command=search_name, padx=5, pady=5)
    add.pack()
    l1 = Label(search_win, text="")
    l1.pack()
    contact = Button(search_win, text="Contact Number", command=search_contact, padx=5, pady=5)
    contact.pack()
    l1 = Label(search_win, text="")
    l1.pack()
    delete = Button(search_win, text="Address", command=search_address, padx=5, pady=5)
    delete.pack()
    l1 = Label(search_win, text="")
    l1.pack()
    search = Button(search_win, text="Email Id", command=search_email, padx=5, pady=5)
    search.pack()
    l1 = Label(search_win, text="")
    l1.pack()
    Quit_search = Button(search_win, text="Quit", command=search_win.destroy)
    Quit_search.pack()
    search_win.mainloop()

def displayEntry():
    """
    The function is called upon clicking the 'display all entries' button in the main address book window.
    It displays all the entries saved in the address book app. If no entries exit it displays a blank screen.
    """
    f1 = open('address_book.csv', 'r')
    rows, det = [], []
    for detail in f1:
        rows += [detail.strip()]
    for i in rows:
        det += [i.split(',')]
    f1.close()
    display_win = Toplevel(main_win)
    display_win.title("Display All Entries")
    window_width = 600
    window_height = 400
    # get the screen dimension
    screen_width = display_win.winfo_screenwidth()
    screen_height = display_win.winfo_screenheight()
    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    display_win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    display_win.resizable(False, False)
    l = Label(display_win, text="All Entries")
    l.place(x=270,y=10)
    entry = ScrolledText(display_win, wrap=WORD, width=60, height=20)
    entry.place(x=50,y=30)
    headings = ['Name: ', 'Contact Number: ', 'Address: ', 'Email Id: ']
    for j in det:
        for k in j:
            entry.insert(INSERT, headings[j.index(k)] + str(k) + "\n")
        entry.insert(INSERT,"\n")
    entry.configure(state='disabled')
    Quit_display = Button(display_win, text="Quit", command=display_win.destroy)
    Quit_display.place(x=285, y=360)

l1 = Label(main_win, text="")
l1.pack()
l = Label(main_win, text="Address Book")
l.pack()
l1 = Label(main_win, text="")
l1.pack()
add=Button(main_win,text="Add Entry",command=addEntry,padx =5,pady =5)
add.pack()
l1 = Label(main_win, text="")
l1.pack()
update=Button(main_win,text="Update Entry",command=selectEntry,padx =5,pady =5)
update.pack()
l1 = Label(main_win, text="")
l1.pack()
search=Button(main_win,text="Search Entry",command=searchEntry,padx =5,pady =5)
search.pack()
l1 = Label(main_win, text="")
l1.pack()
delete=Button(main_win,text="Delete Entry",command=deleteEntry,padx =5,pady =5)
delete.pack()
l1 = Label(main_win, text="")
l1.pack()
display=Button(main_win,text="Display All Entries",command=displayEntry,padx =5,pady =5)
display.pack()
l1 = Label(main_win, text="")
l1.pack()
Quit_main=Button(main_win,text="Quit",command=main_win.destroy)
Quit_main.pack()
main_win.mainloop()

#------------------------------ MAIN WINDOW ENDS -----------------------------------