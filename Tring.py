import mysql.connector as mcon
from tkinter import *
from mysql.connector import Error
from tkinter import messagebox


con = mcon.connect(host="localhost", user="root", password="cyril")
c = con.cursor()
c.execute("use db1")
#c.execute("create table reminder(email_id varchar(60),reminder char(100),date date,time char(5))")
gname = ""

# Output window
f = ('Times', 14)
root = Tk()
root.title('tring')
root.geometry('940x500')
root.config(bg='#0B5A81')

'''
try:
    cur = connection.cursor()
    insert_stm = "create database db1"
    cur.execute(insert_stm)
    insert_stm = "create table users"
    cur.execute(insert_stm)
    connection.commit()
except Error as e:
        print("Error while connecting to MySQL", e)
'''


# Function for registering
def insert_record():
    # Getting the inputs
    check_counter = 0
    warn = ""
    if register_name.get() == "":
        warn = "Name can't be empty"
    else:
        check_counter += 1

    if register_email.get() == "":
        warn = "Email can't be empty"
    else:
        check_counter += 1
    r = register_pwd.get()
    if r == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
        pass

    if pwd_again.get() == "":
        warn = "Re-enter password can't be empty"
    else:
        check_counter += 1

    if register_pwd.get() != pwd_again.get():
        warn = "Passwords didn't match!"
    else:
        check_counter += 1

    if check_counter == 5:
        # Inserting the record into database
        try:
            cur = con.cursor()
            name = register_name.get()
            email = register_email.get()
            password = register_pwd.get()
            data = (name, email, password)
            insert_stm = "INSERT INTO users VALUES (%s,%s,%s)"
            cur.execute(insert_stm, data)
            con.commit()
            messagebox.showinfo('Confirmation', 'Record Saved')

        except Error as ep:
            messagebox.showerror('', ep)
    else:
        messagebox.showerror('Error', warn)


# Function for login
def login_response():
    # Getting inputs
    global gname
    uname = email_tf.get()
    upwd = pwd_tf.get()
    try:
        # Checking if inputs are valid
        qu = "select* from users"
        c = con.cursor()
        c.execute(qu)
        record = c.fetchall()
        con.commit()
        flag = 0
        for row in record:
            username = row[1]
            pwd = row[2]
            check_counter = 0
            if uname == "":
                warn = "Username can't be empty"
            else:
                check_counter += 1
            if upwd == "":
                warn = "Password can't be empty"
            else:
                check_counter += 1
            if check_counter == 2:
                if uname == username and upwd == pwd:
                    flag = 1
                    break
                else:
                    flag = 2
            else:
                pass
        if flag == 1:
            gname = uname
            messagebox.showinfo('Login Status', 'Logged in Successfully!')
            print("csalling home")
            home()

        elif flag == 2:
            messagebox.showerror('Login Status', 'Invalid username or password')
        else:
            messagebox.showerror('', warn)

    except Exception as ep:
        messagebox.showerror('', ep)


# Widgets
left_frame = Frame(
    root,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
)

Label(
    left_frame,
    text="Enter Email",
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    left_frame,
    text="Enter Password",
    bg='#CCCCCC',
    font=f
).grid(row=1, column=0, pady=10)

email_tf = Entry(
    left_frame,
    font=f
)
pwd_tf = Entry(
    left_frame,
    font=f,
    show='*'
)
login_btn = Button(
    left_frame,
    width=15,
    text='Login',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=login_response
)

right_frame = Frame(
    root,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
)

Label(
    right_frame,
    text="Enter Name",
    bg='#CCCCCC',
    font=f
).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Email",
    bg='#CCCCCC',
    font=f
).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Password",
    bg='#CCCCCC',
    font=f
).grid(row=5, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Re-Enter Password",
    bg='#CCCCCC',
    font=f
).grid(row=6, column=0, sticky=W, pady=10)

register_name = Entry(
    right_frame,
    font=f
)

register_email = Entry(
    right_frame,
    font=f
)

register_pwd = Entry(
    right_frame,
    font=f,
    show='*'
)
pwd_again = Entry(
    right_frame,
    font=f,
    show='*'
)

register_btn = Button(
    right_frame,
    width=15,
    text='Register',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=insert_record
)

# Widgets placement
email_tf.grid(row=0, column=1, pady=10, padx=20)
pwd_tf.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)
left_frame.place(x=50, y=50)

register_name.grid(row=0, column=1, pady=10, padx=20)
register_email.grid(row=1, column=1, pady=10, padx=20)
register_pwd.grid(row=5, column=1, pady=10, padx=20)
pwd_again.grid(row=6, column=1, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.place(x=500, y=50)


def insert():  # to insert a new reminder into a file
    global e1, e2, e3, e4
    email = gname
    rem = e2.get()
    date = e3.get()
    time = e4.get()
    c.execute("insert into reminder values(%s,%s,%s,%s)", (email, rem, date, time))
    c.execute("select * from reminder")
    d = c.fetchall()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    con.commit()
'''
#Function to update the password in database
def update_password():
    try:
        qu = "select* from users"
        c = connection.cursor()
        c.execute(qu)
        flag = 0
        record = c.fetchall()
        for row in record:
            if row[1] == gname and row[2] == oldpassword:
                flag = 1
                break

        if flag == 1:
            data = (newpassword, gname)
            squ = "update users set password=%s where email=%s"
            c = connection.cursor()
            c.execute(squ, data)
            connection.commit()
            messagebox.showinfo("Password update","Updated!")

        else:
            messagebox.showerror("Password update","Incorrect existing password!")

        c.close()
        connection.close()
    except mysql.connector.Error as error:
        messagebox.showerror(error)
    window.mainloop()

#Settings window to change password
def cpass():
    global window
    window.destroy()
    window = Tk()
    window.title('Settings')
    window.geometry('940x500')
    Label(window, text="Enter the existing password", bg='#CCCCCC',
          font=f).pack()
    pasd= Entry(window, width=15)
    pasd.pack()
    Label(window, text="Enter new password:", bg='#CCCCCC',
          font=f).pack()
    passn = Entry(window, width=15)
    passn.pack()
    Button(window, text="OK", command=lambda: chgpass(passn.get(), pasd.get())).pack()
    window.mainloop()


def chgpass(newpass, oldpass):
    global newpassword
    global oldpassword
    newpassword = newpass
    oldpassword=oldpass
    update_password()


#Settings window
def settings():
    global window
    window = Tk()
    window.title('Settings')
    window.geometry('940x500')
    Button(window, text="Change your password", command=cpass, bd=2,
           bg='#CCCCCC',
           relief=SOLID,
           padx=10,
           pady=10).pack()
    window.mainloop()

settings()
'''

def upcoming():  # to see the upcoming four reminders
    global l1
    data=(gname)

    qu="select reminder,date,time from reminder where email_id=%s and date>=curdate() order by date"
    c.execute(qu,data)
    d = c.fetchall()
    count = 0
    l1.grid(row=1, column=1)
    for i in d:
        count += 1
        rem = i[0]
        date1 = i[1]
        time = i[2]
        l6 = Label(l1, text=rem + "\n" + str(date1) + "\t" + time)
        l6.grid(row=count, column=0)


def today():  # to see all the reminders for today
    print("today")

    global gname
    data=(gname)
    qu="select reminder,date,time from reminder where date=curdate() and email_id=%s  order by date"
    c.execute(qu,data)
    d = c.fetchall()
    global l2
    count = 0
    l2.grid(row=1, column=2)
    for i in d:
        rem = i[0]
        date1 = i[1]
        time = i[2]
        count += 1
        l4 = Label(l2, text=rem + "\n" + str(date1) + "\t" + time)
        l4.grid(row=count, column=0)


def month():  # to see all the reminders for the month
    print("Month")

    global gname
    qu="select reminder,date,time from reminder where MONTH(date)=MONTH(curdate()) and email_id=%s and date>=curdate() order by date"
    data=(gname)
    c.execute(qu,data)
    d = c.fetchall()
    print('hi')
    global l3
    l3.grid(row=1, column=2)
    count = 0
    for i in d:
        rem = i[0]
        date1 = i[1]
        time = i[2]
        count += 1
        l5 = Label(l2, text=rem + "\n" + str(date1) + "\t" + time)
        l5.grid(row=count, column=0)


def home():
    print("inside home")
    global mylabel1, left_frame, right_frame
    global mylabel2, button1, settings, botton2, button3
    global mylabel3, e1, e2, e3, e4, l2, l3
    settings = Button(root, text="settings", padx=30)
    e1.grid_forget()
    e2.grid_forget()
    e3.grid_forget()
    e4.grid_forget()
    l2.grid_forget()
    l3.grid_forget()
    left_frame.place_forget()
    right_frame.place_forget()
    button1.grid_forget()
    button2.grid_forget()
    button3.grid_forget()
    settings.grid(row=0, column=1)
    print('hi1')
    upcoming()
    mylabel1 = Button(root, text="Home", padx=30, command=home)
    mylabel2 = Button(root, text="Add reminder", padx=10, command=add)
    mylabel3 = Button(root, text="See all reminders", padx=2, command=see)
    mylabel1["state"] = DISABLED
    mylabel2["state"] = NORMAL
    mylabel3["state"] = NORMAL
    mylabel1.grid(row=0, column=0)
    mylabel2.grid(row=1, column=0)
    mylabel3.grid(row=2, column=0)


def add():
    global mylabel1, settings, botton2, button3
    global mylabel2, button1, l1, l2, l3
    global mylabel3, e1, e2, e3, e4
    e1 = Entry(root, width=50)
    e2 = Entry(root, width=50)
    e3 = Entry(root, width=50)
    e4 = Entry(root, width=50)
    l1.grid_forget()
    l2.grid_forget()
    l3.grid_forget()
    button2.grid_forget()
    button3.grid_forget()
    settings.grid_forget()
    button1 = Button(root, text="enter", padx=30, command=insert)
    e2.insert(0, "enter the reminder")
    e3.insert(0, "enter the date(YYYY-MM-DD)")
    e4.insert(0, "enter the time(hour:minute)")
    print('hi2')
    mylabel1 = Button(root, text="Home", padx=30, command=home)
    mylabel2 = Button(root, text="Add reminder", padx=10, command=add)
    mylabel3 = Button(root, text="See all reminders", padx=2, command=see)
    mylabel2["state"] = DISABLED
    mylabel1["state"] = NORMAL
    mylabel3["state"] = NORMAL
    mylabel1.grid(row=0, column=0)
    mylabel2.grid(row=1, column=0)
    mylabel3.grid(row=2, column=0)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)
    e4.grid(row=4, column=1)
    button1.grid(row=5, column=1)


def see():
    global mylabel1, settings
    global mylabel2, button1, l1, button2, button3
    global mylabel3, e1, e2, e3, e4
    e1.grid_forget()
    e2.grid_forget()
    e3.grid_forget()
    e4.grid_forget()
    l1.grid_forget()
    button1.grid_forget()
    settings.grid_forget()
    print('hi3')
    mylabel1 = Button(root, text="Home", padx=30, command=home)
    mylabel2 = Button(root, text="Add reminder", padx=10, command=add)
    mylabel3 = Button(root, text="See all reminders", padx=2, command=see)
    button2 = Button(root, text="today", padx=30, command=today)
    button3 = Button(root, text="this month", padx=30, command=month)
    mylabel3["state"] = DISABLED
    mylabel2["state"] = NORMAL
    mylabel1["state"] = NORMAL
    mylabel1.grid(row=0, column=0)
    mylabel2.grid(row=1, column=0)
    mylabel3.grid(row=2, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=1, column=1)


mylabel1 = Button(root, text="Home", padx=30, command=home)
mylabel2 = Button(root, text="Add reminder", padx=10, command=add)
mylabel3 = Button(root, text="See all reminders", padx=2, command=see)
settings = Button(root, text="settings", padx=30)
l1 = Frame(root)
l2 = Frame(root)
l3 = Frame(root)
e1 = Entry(root, width=50)
e2 = Entry(root, width=50)
e3 = Entry(root, width=50)
e4 = Entry(root, width=50)
mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=0)
mylabel3.grid(row=2,column=0)
button1 = Button(root, text="enter", padx=30, command=insert)
button2 = Button(root, text="today", padx=30, command=today)
button3 = Button(root, text="this month", padx=30, command=month)
root.mainloop()