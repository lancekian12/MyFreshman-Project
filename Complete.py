from tkinter import *
from accdict import account
from tkinter import filedialog
import tkinter.messagebox
from tkinter import ttk

root = Tk()
root.title("Tosho Center")
text = StringVar()
root.config(bg="white")
root.state('zoomed')

button_mode = True


def customize(event):
    global button_mode

    if button_mode:
        button3.config(image=off, bg="#121212", activebackground="#121212")
        second_frame.config(bg="#121212")
        my_label1.config(image=my_label, bg="#121212", activebackground="#121212")
        recommendation2.config(image=recommendation, bg="#121212", activebackground="#121212")
        my_emptylabel1.config(bg="#121212")
        my_emptylabel2.config(bg="#121212")
        my_emptylabel3.config(bg="#121212")
        my_emptylabel4.config(bg="#121212")
        emptylabelfourth.config(bg="#121212")
        emptylabelfifth.config(bg="#121212")
        my_canvas.config(bg="#121212")
        button_mode = False
    else:
        button3.config(image=on, bg="white", activebackground="white")
        second_frame.config(bg="white")
        my_label1.config(image=my_label, bg="white", activebackground="white")
        recommendation2.config(image=recommendation, bg="white", activebackground="white")
        my_emptylabel1.config(bg="white")
        my_emptylabel2.config(bg="white")
        my_emptylabel3.config(bg="white")
        my_emptylabel4.config(bg="white")
        emptylabelfourth.config(bg="white")
        emptylabelfifth.config(bg="white")
        my_canvas.config(bg="white")
        button_mode = True


# Create a main frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create a Canvas
my_canvas = Canvas(main_frame, bg="white")
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scrollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# Creates ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas, bg="white")

# Add that New Frame To a window In the Canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

on = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\black2.PNG")
off = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\light2.PNG")

# Create a function to check entry vs listbox
def check(e):
    global typed
    # grab what was typed
    typed = my_entry.get()
    if typed == "":
        my_list.grid_remove()
        data = manga
    else:
        my_list.grid()
        data = []
        for item in manga:
            if typed.lower() in item.lower():
                data.append(item)

    # update our listbox with selected items
    update(data)


# Update the listbox
def update(data):
    # Clear the listbox
    my_list.delete(0, END)

    # Add manga to listbox
    for item in data:
        my_list.insert(END, item)


# Update entry box with listbox clicked
def fillout(e):
    # Delete Whatever is in the entry box
    my_entry.delete(0, END)

    # Add clicked list item to the entry box
    my_entry.insert(0, my_list.get(ACTIVE))

def search():
    search2 = my_entry.get().lower()
    if search2 == "martial Peak".lower():
        martialpeak()
    elif search2 =="one punch man".lower():
        onepunchman()
    elif search2 =="fly me to the moon".lower():
        flymetothemoon()
    elif search2 =="Sousouno Frieren".lower():
        sousounofrieren()
    elif search2 =="Solo Leveling".lower():
        sololeveling()
# Welcome Main
user2 = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Welcome User.png")

# Create a label
# my_label = Label(root,text="Tosho Center",font=("Arial",50,"bold"),bg="white")
# my_label.grid(column=5,row=2)

my_label = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Tittle 1.png")
my_label1 = Label(second_frame, image=my_label, bd=0, bg="white", activebackground="white")
my_label1.grid(column=5, row=2)

# Empty Label
my_emptylabel1 = Label(second_frame, text=" ", bg="white")
my_emptylabel1.grid(column=5, row=3)

# Button for Dark and Light
button3 = Button(second_frame, image=on, bd=0, bg="white")
button3.bind("<Button-1>",customize)
button3.grid(column=10, row=2)
root.bind("<F5>", customize)

# Create an entry box
my_entry = Entry(second_frame, font=("Times", 13, "bold"), width=70, bd=2, bg="white")
my_entry.grid(column=5, row=5)

# Search Button
button = Button(second_frame, text="Search", font=("Times", 10, "bold"), bg="white", fg="black", width=10, bd=1, command=search)
button.place(x=1319, y=337)

# Create a listbox
my_list = Listbox(second_frame,bg="white",width=105, height=0)
my_list.grid(column=5, row=7)

# Create A Label for Recommendation
recommendation = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Recommendation 3.png")
recommendation2 = Label(second_frame, image=recommendation, bd=0, bg="white", activebackground="white")
recommendation2.grid(column=3, row=8)

# Empty Label
my_emptylabel2 = Label(second_frame, text=" ", bg="white")
my_emptylabel2.grid(column=5, row=9)

# Empty Label
my_emptylabel3 = Label(second_frame, text=" ", bg="white")
my_emptylabel3.grid(column=5, row=11)

# Empty Label
my_emptylabel4 = Label(second_frame, text=" ", bg="white")
my_emptylabel4.grid(column=5, row=13)

#Pictures for creation
tittle1 = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Creation Folder\\Tittle.png")
description = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Creation Folder\\Description.png")
mangacreationpage = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Creation Folder\\Manga Creation Page 1.png")
mangacreationpage2 = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Creation Folder\\Manga Creation Page 2.png")
pageresult = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Creation Folder\\Result.png")
usingimage = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Creation Folder\\Imagethatyouuse.png")

# Create a list of pizza manga
manga = ["Martial Peak", "One Punch Man","Solo Leveling","Fly me to the moon", "Sousouno Frieren"]

# Add the manga to our list
update(manga)

# Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)

# Create a binding on the entry box
my_entry.bind("<KeyRelease>", check)

def creation():
    global creation1
    creation1 = Toplevel(root)
    creation1.title("Creation Page")
    creation1.state("zoomed")
    def tittle():
        global textbox
        labelmangacreation = Label(creation1,image=mangacreationpage,bd=0,bg="white",activebackground="white")
        labelmangacreation.place(x=20,y=20)
        tittle2 = Label(creation1, image=tittle1, bd=0, bg="white", activebackground="white")
        tittle2.pack(pady=20)
        textbox = Text(creation1, font=("Times", 15, "bold"),height=1 ,width=70, bd=2, bg="white")
        textbox.pack()

    def sypnosis():
        global textbox2
        description2 = Label(creation1, image=description, bd=0, bg="white", activebackground="white")
        description2.pack(pady=20)
        textbox2 = Text(creation1, font=("Times", 15, "bold"), width=70)
        textbox2.pack()
    def result():
        global testing, testing2
        testing = textbox.get(1.0, "end-1c")
        print("Title:", testing)
        #print(testing)
        testing2 = textbox2.get(1.0, "end-1c")
        print("Description:", testing2)
        #print(testing2)
        creation2()

    def submit():
        btn = Button(creation1, text="Next", font=("Times", 17, "bold"),bd=5,width=20,command=result)
        btn.pack(pady=20)
    tittle()
    sypnosis()
    submit()

def creation2():
    global creation3, second_frame7, my_canvas7, panel

    creation3 = Toplevel(root)
    creation3.title("Results")
    creation3.state('zoomed')

    # Create a main frame
    main_frame7 = Frame(creation3)
    main_frame7.pack(fill=BOTH, expand=1)

    # Create a Canvas
    my_canvas7 = Canvas(main_frame7, bg="white")
    my_canvas7.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar to the canvas
    my_scrollbar7 = ttk.Scrollbar(main_frame7, orient=VERTICAL, command=my_canvas7.yview)
    my_scrollbar7.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas7.configure(yscrollcommand=my_scrollbar7.set)
    my_canvas7.bind('<Configure>', lambda e: my_canvas7.configure(scrollregion=my_canvas7.bbox("all")))

    # Creates ANOTHER Frame INSIDE the Canvas
    second_frame7 = Frame(my_canvas7, bg="white")

    # Add that New Frame To a window In the Canvas
    my_canvas7.create_window((0, 0), window=second_frame7, anchor="center")

    def openfn():
        global createlist, filename
        filename = filedialog.askopenfilename(title='open')
        createlist = []
        createlist.append(filename)
        print("Image Location:",filename)
        #print(createlist)
        return filename

    def open_img():
        global img, panel
        x = openfn()
        img = Image.open(x)
        img = ImageTk.PhotoImage(img)
        panel = Label(second_frame7, image=img)
        panel.image = img
        panel.grid(column=4,row=3)
    #labelisempty = Label(second_frame7,text="                                                                                     ",bg="white")
    #labelisempty.grid(column=1, row= 1)
    labelisempty = Label(second_frame7, text="                                                                                                         ",bg="white")
    labelisempty.grid(column=2,row=1)
    labelmangacreation2 = Label(second_frame7, image=mangacreationpage2, bd=0, bg="white", activebackground="white")
    labelmangacreation2.grid(column=4, row=1)
    labelisempty = Label(second_frame7,text="                                                                                                          ",bg="white")
    labelisempty.grid(column=1, row=1)

    buttonforimage = Button(second_frame7, text="Open image File",font=("Times", 15), bd=3, width=18,command=open_img)
    buttonforimage.grid(column=4,row=2)
    def answer2():
        answer2 = tkinter.messagebox.showinfo("Approval", "Please wait for the Approval of the admin. Thank you!")
    def answer():
        answer = tkinter.messagebox.askquestion('Submit', "Do you want to submit")
        if answer =="yes":
            answer2()
            destroy()
    buttonforsubmit = Button(second_frame7, text="Submit",font=("Times", 15), bd=3, width=18,command=answer)
    buttonforsubmit.grid(column=4, row=5)

    creation3.mainloop()
def destroy():
    creation1.destroy()
    creation3.destroy()
def register_user(event2):
    accountlist = []
    create = str(user.get())
    create1 = str(password.get())
    create2 = str(subp.get())

    accountlist.append(create)
    accountlist.append(create1)
    accountlist.append(create2)
    print("Registering New Account")
    print(accountlist)

    users = list(account.keys())

    if create not in users:
        if len(create1) > 1:
            if create1 == create2:
                account[create] = create1
                print("New Account has been made")
                print(account)
                Label(page1, text="Registration Success", fg="green", font=("Calibri", 11)).pack()
                page1.destroy()
            else:
                password.delete(0, 'end')
                subp.delete(0, 'end')
                print("Invalid Password")
                print(account)
                Label(page1, text="Invalid User or Pass", fg="green", font=("Calibri", 11)).pack()
                return
        else:
            password.delete(0, 'end')
            subp.delete(0, 'end')
            print("Invalid Password")
            Label(page1, text="Invalid User or Pass", fg="green", font=("Calibri", 11)).pack()
            print(account)
            return
    else:
        user.delete(0, 'end')
        password.delete(0, 'end')
        subp.delete(0, 'end')
        print("Invalid User")
        print(account)
        return


def register():
    global page1
    page1 = Toplevel(root)
    page1.title("Register")
    page1.geometry("300x250")

    global user
    global password
    global subp

    Label(page1, text="Please enter details below",font=("Arial",15,"bold")).pack()
    Label(page1, text="").pack()
    Label(page1, text="Username").pack()
    user = Entry(page1)
    user.pack()
    Label(page1, text="Password").pack()
    password = Entry(page1, show="*")
    password.pack()
    Label(page1, text="Confirm_Password").pack()
    subp = Entry(page1, show="*")
    subp.pack()
    bindregister = Button(page1, text="Register", width=10, height=1)
    bindregister.bind("<Button-1>", register_user)
    page1.bind("<Return>",register_user)
    bindregister.pack()

def login_user(event):
    global user3, logout
    create1 = str(user1.get())
    create2 = str(password1.get())

    if create1 in account:
        x = str(list(account.values()))
        y = str(create2)
        if y in x:
            print("Successfully Log in")
            Label(page2, text="Successfully Log in", fg="green", font=("Calibri", 11)).pack()
            page2.destroy()
            login2.destroy()
            register2.destroy()
            user3_logout()
        else:
            print("Incorrect username or password")
            user1.delete(0, 'end')
            password1.delete(0, 'end')
            return
    else:
        print("Incorrect username or password")
        Label(page2, text="Incorrect username or password", fg="green", font=("Calibri", 11)).pack()
        user1.delete(0, 'end')
        password1.delete(0, 'end')
        return

def login():
    global page2
    page2 = Toplevel(root)
    page2.title("Login")
    page2.geometry("300x250")

    global user1
    global password1

    Label(page2, text="Please enter details below",font=("Arial",15,"bold")).pack()
    Label(page2, text="").pack()
    Label(page2, text="Username").pack()
    user1 = Entry(page2)
    user1.pack()
    Label(page2, text="Password").pack()
    password1 = Entry(page2, show="*")
    password1.pack()
    bindlogin = Button(page2, text="Login", width=10, height=1)
    bindlogin.bind("<Button-1>", login_user)
    page2.bind("<Return>", login_user)
    bindlogin.pack()

def log_out():
    user3.destroy()
    logout.destroy()
    create_file.destroy()
    main_page()

def main_page():
    global login2, register2
    # Login Label
    login2 = Button(second_frame, text="Login", height="2", width="30", command=login)
    login2.place(x=100, y=50)
    # Register Label
    register2 = Button(second_frame, text="Register", height="2", width="30", command=register)
    register2.place(x=100, y=100)


def user3_logout():
    global logout, user3, create_file
    user3 = Label(second_frame, image=user2, bd=0, bg="white", activebackground="white")
    user3.place(x=100, y=50)
    logout = Button(second_frame, text="Logout", height="2", width="30", command=log_out)
    logout.place(x=205, y=150)
    create_file = Button(second_frame,text="Create",height="2",width="30",command=creation)
    create_file.place(x=205, y = 200)



button_mode2 = True


def customize2(event4):
    global button_mode2

    if button_mode2:
        button5.config(image=off2, bg="#121212", activebackground="#121212")
        second_frame2.config(bg="#121212")
        my_canvas2.config(bg="#121212")
        button_mode2 = False
    else:
        button5.config(image=on2, bg="white", activebackground="white")
        second_frame2.config(bg="white")
        my_canvas2.config(bg="White")
        button_mode2 = True
    event4 = None

def martialpeak():
    global martialpeak2, second_frame2, button5, my_canvas2

    martialpeak2 = Toplevel(root)
    martialpeak2.title("Martial Peak")
    martialpeak2.state('zoomed')

    # Create a main frame
    main_frame2 = Frame(martialpeak2)
    main_frame2.pack(fill=BOTH, expand=1)

    # Create a Canvas
    my_canvas2 = Canvas(main_frame2, bg="white")
    my_canvas2.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar to the canvas
    my_scrollbar2 = ttk.Scrollbar(main_frame2, orient=VERTICAL, command=my_canvas2.yview)
    my_scrollbar2.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas2.configure(yscrollcommand=my_scrollbar2.set)
    my_canvas2.bind('<Configure>', lambda e: my_canvas2.configure(scrollregion=my_canvas2.bbox("all")))

    # Creates ANOTHER Frame INSIDE the Canvas
    second_frame2 = Frame(my_canvas2, bg="white")

    # Add that New Frame To a window In the Canvas
    my_canvas2.create_window((0, 0), window=second_frame2, anchor="center")

    # Home Page
    home_button = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Home Page.png")
    home_button2 = Button(second_frame2, image=home_button, bd=0, bg="#0448cb", activebackground="#0448cb", command=martialpeak2.destroy)
    home_button2.place(x=60, y=20)

    # Button
    button5 = Button(second_frame2, image=on2, bd=0, bg="white")
    button5.place(x=1500, y=20)
    button5.bind("<Button-1>",customize2)
    martialpeak2.bind("<F5>",customize2)
    # Tittle
    my_label = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Tittle 1.png")
    my_label1 = Label(second_frame2, image=my_label, bd=0, bg="white", activebackground="white")
    my_label1.grid(column=5, row=1)

    # emptylabel = Label(second_frame2, text="",bg="white",activebackground="white")
    # emptylabel.grid(column=5, row=2)


    # First Page
    first_page = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Martial Peak\\3.png")
    label = ttk.Label(second_frame2, image=first_page)
    label.grid(column=5, row=3)

    # Second page
    second_page = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Martial Peak\\4.png")
    label2 = ttk.Label(second_frame2, image=second_page)
    label2.grid(column=5, row=4)

    # Third page
    third_page = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Martial Peak\\5.png")
    label3 = ttk.Label(second_frame2, image=third_page)
    label3.grid(column=5, row=5)
    # Fourth Page
    fourth_page = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Martial Peak\\6.png")
    label4 = ttk.Label(second_frame2, image=fourth_page)
    label4.grid(column=5, row=6)
    # Fifth Page
    fifth_page = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Martial Peak\\7.png")
    label5 = ttk.Label(second_frame2, image=fifth_page)
    label5.grid(column=5, row=7)
    # Sixth Page
    sixth_page = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Martial Peak\\8.png")
    label6 = ttk.Label(second_frame2, image=sixth_page)
    label6.grid(column=5, row=8)
    # Seventh Page
    seventh_page = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Martial Peak\\9.png")
    label7 = ttk.Label(second_frame2, image=seventh_page)
    label7.grid(column=5, row=9)
    # Eight Page
    eight_page = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Martial Peak\\10.png")
    label8 = ttk.Label(second_frame2, image=eight_page)
    label8.grid(column=5, row=10)

    # Ninth Page
    ninth_page = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Martial Peak\\11.png")
    label9 = ttk.Label(second_frame2, image=ninth_page)
    label9.grid(column=5, row=11)

    # Tenth Page
    tenth_page = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Martial Peak\\12.png")
    label10 = ttk.Label(second_frame2, image=tenth_page)
    label10.grid(column=5, row=12)

    # Eleven Page
    eleven_page = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Martial Peak\\13.png")
    label11 = ttk.Label(second_frame2, image=eleven_page)
    label11.grid(column=5, row=13)

    # Twelve Page
    twelve_page = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Martial Peak\\14.png")
    label12 = ttk.Label(second_frame2, image=twelve_page)
    label12.grid(column=5, row=14)

    # Thirteen Page
    thirteen_page = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Martial Peak\\15.png")
    label13 = ttk.Label(second_frame2, image=thirteen_page)
    label13.grid(column=5, row=15)

    # Fourteen Page
    fourteen_page = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Martial Peak\\16.png")
    label14 = ttk.Label(second_frame2, image=fourteen_page)
    label14.grid(column=5, row=16)

    # Fifteen Page
    fifteen_page = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Martial Peak\\17.png")
    label15 = ttk.Label(second_frame2, image=fifteen_page)
    label15.grid(column=5, row=17)

    # Sixteen Page
    sixteen_page = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Martial Peak\\18.png")
    label16 = ttk.Label(second_frame2, image=sixteen_page)
    label16.grid(column=5, row=18)

    # Seventeen Page
    seventeen_page = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Martial Peak\\19.png")
    label17 = ttk.Label(second_frame2, image=seventeen_page)
    label17.grid(column=5, row=19)

    # Eighteen Page
    eighteen_page = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Martial Peak\\20.png")
    label18 = ttk.Label(second_frame2, image=eighteen_page)
    label18.grid(column=5, row=20)

    martialpeak2.mainloop()

first_recommendation = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Recommendation\\Martial Peak 1.png")
first_recommendation2 = Button(second_frame, image=first_recommendation, bg="#0448cb", activebackground="#0448cb", command=martialpeak)
first_recommendation2.grid(column=5, row=10)

button_mode3 = True

def customize6(event4):
    global button_mode3

    if button_mode3:
        button6.config(image=off2, bg="#121212", activebackground="#121212")
        second_frame2.config(bg="#121212")
        my_canvas3.config(bg="#121212")
        button_mode3 = False
    else:
        button6.config(image=on2, bg="white", activebackground="white")
        second_frame2.config(bg="white")
        my_canvas3.config(bg="White")
        button_mode3 = True

def onepunchman():
    global onepunchman2, second_frame2, button6, my_canvas3

    onepunchman2 = Toplevel(root)
    onepunchman2.title("One Punch Man")
    onepunchman2.state('zoomed')

    # Create a main frame
    main_frame3 = Frame(onepunchman2)
    main_frame3.pack(fill=BOTH, expand=1)

    # Create a Canvas
    my_canvas3 = Canvas(main_frame3, bg="white")
    my_canvas3.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar to the canvas
    my_scrollbar3 = ttk.Scrollbar(main_frame3, orient=VERTICAL, command=my_canvas3.yview)
    my_scrollbar3.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas3.configure(yscrollcommand=my_scrollbar3.set)
    my_canvas3.bind('<Configure>', lambda e: my_canvas3.configure(scrollregion=my_canvas3.bbox("all")))

    # Creates ANOTHER Frame INSIDE the Canvas
    second_frame2 = Frame(my_canvas3, bg="white")

    # Add that New Frame To a window In the Canvas
    my_canvas3.create_window((0, 0), window=second_frame2, anchor="center")

    # Home Page
    home_button = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Home Page.png")
    home_button2 = Button(second_frame2, image=home_button, bd=0, bg="#0448cb", activebackground="#0448cb", command=onepunchman2.destroy)
    home_button2.place(x=60, y=20)

    # Button
    button6 = Button(second_frame2, image=on2, bd=0, bg="white")
    button6.place(x=1350, y=20)
    button6.bind("<Button-1>",customize6)
    onepunchman2.bind("<F5>",customize6)
    # Tittle
    my_label = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Tittle 1.png")
    my_label1 = Label(second_frame2, image=my_label, bd=0, bg="white", activebackground="white")
    my_label1.grid(column=5, row=1)

    # First Page
    first_page = PhotoImage("D:\\PycharmProjects\\FreshmanProject\\Final Project Pictures\\One Punch Man\\1.jpg")
    label = ttk.Label(second_frame, image=first_page)
    label.grid(column=5,row=2)

    # Second page
    second_page = PhotoImage("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\One Punch Man\\2.jpg")
    label2 = ttk.Label(second_frame2, image=second_page)
    label2.grid(column=5, row=3)

    # Third page
    third_page = PhotoImage("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\One Punch Man\\3.jpg")
    third_page2 = ImageTk.PhotoImage(third_page)
    label3 = ttk.Label(second_frame2, image=third_page2)
    label3.grid(column=5, row=4)

    # Fourth Page
    fourth_page = PhotoImage("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\One Punch Man\\4.jpg")
    fourth_page2 = ImageTk.PhotoImage(fourth_page)
    label4 = ttk.Label(second_frame2, image=fourth_page2)
    label4.grid(column=5, row=5)

    # Fifth Page
    fifth_page = PhotoImage("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\One Punch Man\\5.jpg")
    fifth_page2 = ImageTk.PhotoImage(fifth_page)
    label5 = ttk.Label(second_frame2, image=fifth_page2)
    label5.grid(column=5, row=6)

    # Sixth Page
    sixth_page = PhotoImage("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\One Punch Man\\6.jpg")
    sixth_page2 = ImageTk.PhotoImage(sixth_page)
    label6 = ttk.Label(second_frame2, image=sixth_page2)
    label6.grid(column=5, row=7)

    # Seventh Page
    seventh_page = PhotoImage("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\One Punch Man\\7.jpg")
    seventh_page2 = ImageTk.PhotoImage(seventh_page)
    label7 = ttk.Label(second_frame2, image=seventh_page2)
    label7.grid(column=5, row=8)

    # Eight Page
    eight_page = PhotoImage("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\One Punch Man\\8.jpg")
    eight_page2 = ImageTk.PhotoImage(eight_page)
    label8 = ttk.Label(second_frame2, image=eight_page2)
    label8.grid(column=5, row=9)

    # Ninth Page
    ninth_page = PhotoImage("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\One Punch Man\\9.jpg")
    ninth_page2 = ImageTk.PhotoImage(ninth_page)
    label9 = ttk.Label(second_frame2, image=ninth_page2)
    label9.grid(column=5, row=10)

    # Tenth Page
    tenth_page = PhotoImage("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\One Punch Man\\10.jpg")
    tenth_page2 = ImageTk.PhotoImage(tenth_page)
    label10 = ttk.Label(second_frame2, image=tenth_page2)
    label10.grid(column=5, row=11)

    # Eleven Page
    eleventh_page = PhotoImage("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\One Punch Man\\11.jpg")
    eleventh_page2 = ImageTk.PhotoImage(eleventh_page)
    label11 = ttk.Label(second_frame2, image=eleventh_page2)
    label11.grid(column=5, row=12)

    # Twelve Page
    twelveth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\One Punch Man\\12.jpg")
    twelveth_page2 = ImageTk.PhotoImage(twelveth_page)
    label12 = ttk.Label(second_frame2, image=twelveth_page2)
    label12.grid(column=5, row=13)

    # Thirteen Page
    thirteenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\One Punch Man\\13.jpg")
    thirteenth_page2 = ImageTk.PhotoImage(thirteenth_page)
    label13 = ttk.Label(second_frame2, image=thirteenth_page2)
    label13.grid(column=5, row=14)

    # Fourteen Page
    fourteenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\One Punch Man\\14.jpg")
    fourteenth_page2 = ImageTk.PhotoImage(fourteenth_page)
    label14 = ttk.Label(second_frame2, image=fourteenth_page2)
    label14.grid(column=5, row=15)

    # Fifteen Page
    fifteenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\One Punch Man\\15.jpg")
    fifteenth_page2 = ImageTk.PhotoImage(fifteenth_page)
    label15 = ttk.Label(second_frame2, image=fifteenth_page2)
    label15.grid(column=5, row=16)

    # Sixteen Page
    sixteenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\One Punch Man\\16.jpg")
    sixteenth_page2 = ImageTk.PhotoImage(sixteenth_page)
    label16 = ttk.Label(second_frame2, image=sixteenth_page2)
    label16.grid(column=5, row=17)

    # Seventeen Page
    seventeenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\One Punch Man\\17.jpg")
    seventeenth_page2 = ImageTk.PhotoImage(seventeenth_page)
    label17 = ttk.Label(second_frame2, image=seventeenth_page2)
    label17.grid(column=5, row=18)

    # Eighteen Page
    eighteenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\One Punch Man\\18.jpg")
    eighteenth_page2 = ImageTk.PhotoImage(eighteenth_page)
    label18 = ttk.Label(second_frame2, image=eighteenth_page2)
    label18.grid(column=5, row=19)

    # Ninteen Page
    nineteenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\One Punch Man\\19.jpg")
    nineteenth_page2 = ImageTk.PhotoImage(nineteenth_page)
    label19 = ttk.Label(second_frame2, image=nineteenth_page2)
    label19.grid(column=5, row=19)

    onepunchman2.mainloop()


on2 = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\black2.PNG")
off2 = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\black2.PNG")

second_recommendation = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Recommendation\\One Punch 1.png")
second_recommendation2 = Button(second_frame, image=second_recommendation, bg="#0448cb", activebackground="#0448cb", command=onepunchman)
second_recommendation2.grid(column=5, row=12)

button_mode4= True

def customize3(event4):
    global button_mode4

    if button_mode4:
        button7.config(image=off2, bg="#121212", activebackground="#121212")
        second_frame4.config(bg="#121212")
        my_canvas4.config(bg="#121212")
        button_mode4 = False
    else:
        button7.config(image=on2, bg="white", activebackground="white")
        second_frame4.config(bg="white")
        my_canvas4.config(bg="White")
        button_mode4 = True

def flymetothemoon():
    global flymetothemoon, second_frame4, button7, my_canvas4

    flymetothemoon2 = Toplevel(root)
    flymetothemoon2.title("Fly Me To The Moon")
    flymetothemoon2.state('zoomed')

    # Create a main frame
    main_frame4 = Frame(flymetothemoon2)
    main_frame4.pack(fill=BOTH, expand=1)

    # Create a Canvas
    my_canvas4 = Canvas(main_frame4, bg="white")
    my_canvas4.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar to the canvas
    my_scrollbar4 = ttk.Scrollbar(main_frame4, orient=VERTICAL, command=my_canvas4.yview)
    my_scrollbar4.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas4.configure(yscrollcommand=my_scrollbar4.set)
    my_canvas4.bind('<Configure>', lambda e: my_canvas4.configure(scrollregion=my_canvas4.bbox("all")))

    # Creates ANOTHER Frame INSIDE the Canvas
    second_frame4 = Frame(my_canvas4, bg="white")

    # Add that New Frame To a window In the Canvas
    my_canvas4.create_window((0, 0), window=second_frame4, anchor="center")

    # Home Page
    home_button = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Home Page.png")
    home_button2 = Button(second_frame4, image=home_button, bd=0, bg="#0448cb", activebackground="#0448cb", command=flymetothemoon2.destroy)
    home_button2.place(x=60, y=20)

    # Button
    button7 = Button(second_frame4, image=on2, bd=0, bg="white")
    button7.place(x=1350, y=20)
    button7.bind("<Button-1>",customize3)
    flymetothemoon2.bind("<F5>",customize3)
    # Tittle
    my_label = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Tittle 1.png")
    my_label1 = Label(second_frame4, image=my_label, bd=0, bg="white", activebackground="white")
    my_label1.grid(column=5, row=1)

    # First Page
    first_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\1.jpg")
    first_page2 = ImageTk.PhotoImage(first_page)
    label = ttk.Label(second_frame4, image=first_page2)
    label.grid(column=5,row=2)

    # Second page
    second_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\2.jpg")
    second_page2 = ImageTk.PhotoImage(second_page)
    label2 = ttk.Label(second_frame4, image=second_page2)
    label2.grid(column=5, row=3)

    # Third page
    third_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\3.jpg")
    third_page2 = ImageTk.PhotoImage(third_page)
    label3 = ttk.Label(second_frame4, image=third_page2)
    label3.grid(column=5, row=4)

    # Fourth Page
    fourth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\4.jpg")
    fourth_page2 = ImageTk.PhotoImage(fourth_page)
    label4 = ttk.Label(second_frame4, image=fourth_page2)
    label4.grid(column=5, row=5)

    # Fifth Page
    fifth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\5.jpg")
    fifth_page2 = ImageTk.PhotoImage(fifth_page)
    label5 = ttk.Label(second_frame4, image=fifth_page2)
    label5.grid(column=5, row=6)

    # Sixth Page
    sixth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\6.jpg")
    sixth_page2 = ImageTk.PhotoImage(sixth_page)
    label6 = ttk.Label(second_frame4, image=sixth_page2)
    label6.grid(column=5, row=7)

    # Seventh Page
    seventh_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\7.jpg")
    seventh_page2 = ImageTk.PhotoImage(seventh_page)
    label7 = ttk.Label(second_frame4, image=seventh_page2)
    label7.grid(column=5, row=8)

    # Eight Page
    eight_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\8.jpg")
    eight_page2 = ImageTk.PhotoImage(eight_page)
    label8 = ttk.Label(second_frame4, image=eight_page2)
    label8.grid(column=5, row=9)

    # Ninth Page
    ninth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\9.jpg")
    ninth_page2 = ImageTk.PhotoImage(ninth_page)
    label9 = ttk.Label(second_frame4, image=ninth_page2)
    label9.grid(column=5, row=10)

    # Tenth Page
    tenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\10.jpg")
    tenth_page2 = ImageTk.PhotoImage(tenth_page)
    label10 = ttk.Label(second_frame4, image=tenth_page2)
    label10.grid(column=5, row=11)

    # Eleven Page
    eleventh_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\11.jpg")
    eleventh_page2 = ImageTk.PhotoImage(eleventh_page)
    label11 = ttk.Label(second_frame4, image=eleventh_page2)
    label11.grid(column=5, row=12)

    # Twelve Page
    twelveth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\12.jpg")
    twelveth_page2 = ImageTk.PhotoImage(twelveth_page)
    label12 = ttk.Label(second_frame4, image=twelveth_page2)
    label12.grid(column=5, row=13)

    # Thirteen Page
    thirteenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\13.jpg")
    thirteenth_page2 = ImageTk.PhotoImage(thirteenth_page)
    label13 = ttk.Label(second_frame4, image=thirteenth_page2)
    label13.grid(column=5, row=14)

    # Fourteen Page
    fourteenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\14.jpg")
    fourteenth_page2 = ImageTk.PhotoImage(fourteenth_page)
    label14 = ttk.Label(second_frame4, image=fourteenth_page2)
    label14.grid(column=5, row=15)

    # Fifteen Page
    fifteenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\15.jpg")
    fifteenth_page2 = ImageTk.PhotoImage(fifteenth_page)
    label15 = ttk.Label(second_frame4, image=fifteenth_page2)
    label15.grid(column=5, row=16)

    # Sixteen Page
    sixteenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\16.jpg")
    sixteenth_page2 = ImageTk.PhotoImage(sixteenth_page)
    label16 = ttk.Label(second_frame4, image=sixteenth_page2)
    label16.grid(column=5, row=17)

    # Seventeen Page
    seventeenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\17.jpg")
    seventeenth_page2 = ImageTk.PhotoImage(seventeenth_page)
    label17 = ttk.Label(second_frame4, image=seventeenth_page2)
    label17.grid(column=5, row=18)

    # Eighteen Page
    eighteenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\18.jpg")
    eighteenth_page2 = ImageTk.PhotoImage(eighteenth_page)
    label18 = ttk.Label(second_frame4, image=eighteenth_page2)
    label18.grid(column=5, row=19)

    # Ninteen Page
    nineteenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\19.jpg")
    nineteenth_page2 = ImageTk.PhotoImage(nineteenth_page)
    label19 = ttk.Label(second_frame4, image=nineteenth_page2)
    label19.grid(column=5, row=19)

    # Twenty
    twenty = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\20.jpg")
    twenty2 = ImageTk.PhotoImage(twenty)
    label20 = ttk.Label(second_frame4, image=twenty2)
    label20.grid(column=5, row=20)

    # twenty-one Page
    twentyone = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\21.jpg")
    twentyone2 = ImageTk.PhotoImage(twentyone)
    label21 = ttk.Label(second_frame4, image=twentyone2)
    label21.grid(column=5, row=21)

    # twenty-two Page
    twentytwo = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\22.jpg")
    twentytwo2 = ImageTk.PhotoImage(twentytwo)
    label22 = ttk.Label(second_frame4, image=twentytwo2)
    label22.grid(column=5, row=22)

    # twenty-three Page
    twentythree = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\23.jpg")
    twentythree2 = ImageTk.PhotoImage(twentythree)
    label23 = ttk.Label(second_frame4, image=twentythree2)
    label23.grid(column=5, row=23)

    # twenty-four Page
    twentyfour = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\24.jpg")
    twentyfour2 = ImageTk.PhotoImage(twentyfour)
    label24 = ttk.Label(second_frame4, image=twentyfour2)
    label24.grid(column=5, row=24)

    # twenty-five Page
    twentyfive = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Fly me to the moon\\25.jpg")
    twentyfive2 = ImageTk.PhotoImage(twentyfive)
    label25 = ttk.Label(second_frame4, image=twentyfive2)
    label25.grid(column=5, row=25)

    flymetothemoon2.mainloop()

emptylabelfourth = Label(second_frame,text=" ",bg="white",activebackground="white")
emptylabelfourth.grid(column=5,row=15)

fourth_recommendation = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Recommendation\\Fly me to the moon.png")
fourth_recommendation2 = Button(second_frame, image=fourth_recommendation, bg="#0448cb", activebackground="#0448cb", command=flymetothemoon)
fourth_recommendation2.grid(column=5,row=16)

button_mode5= True

def customize4(event4):
    global button_mode5

    if button_mode5:
        button7.config(image=off2, bg="#121212",activebackground="#121212")
        second_frame5.config(bg="#121212")
        my_canvas5.config(bg="#121212")
        button_mode5 = False
    else:
        button7.config(image=on2, bg="white", activebackground="white")
        second_frame5.config(bg="white")
        my_canvas5.config(bg="White")
        button_mode5 = True

def sousounofrieren():
    global sousounofrieren2, second_frame5, button7, my_canvas5

    sousounofrieren2 = Toplevel(root)
    sousounofrieren2.title("Sousouno Frieren")
    sousounofrieren2.state('zoomed')

    # Create a main frame
    main_frame5 = Frame(sousounofrieren2)
    main_frame5.pack(fill=BOTH, expand=1)

    # Create a Canvas
    my_canvas5 = Canvas(main_frame5, bg="white")
    my_canvas5.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar to the canvas
    my_scrollbar5 = ttk.Scrollbar(main_frame5, orient=VERTICAL, command=my_canvas5.yview)
    my_scrollbar5.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas5.configure(yscrollcommand=my_scrollbar5.set)
    my_canvas5.bind('<Configure>', lambda e: my_canvas5.configure(scrollregion=my_canvas5.bbox("all")))

    # Creates ANOTHER Frame INSIDE the Canvas
    second_frame5 = Frame(my_canvas5, bg="white")

    # Add that New Frame To a window In the Canvas
    my_canvas5.create_window((0, 0), window=second_frame5, anchor="center")

    # Home Page
    home_button = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Home Page.png")
    home_button2 = Button(second_frame5, image=home_button, bd=0, bg="#0448cb", activebackground="#0448cb", command=sousounofrieren2.destroy)
    home_button2.place(x=60, y=20)

    # Button
    button7 = Button(second_frame5, image=on2, bd=0, bg="white")
    button7.place(x=1350, y=20)
    button7.bind("<Button-1>",customize4)
    sousounofrieren2.bind("<F5>",customize4)
    # Tittle
    my_label = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Tittle 1.png")
    my_label1 = Label(second_frame5, image=my_label, bd=0, bg="white", activebackground="white")
    my_label1.grid(column=5, row=1)

    # First Page
    first_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c000.jpg")
    first_page2 = ImageTk.PhotoImage(first_page)
    label = ttk.Label(second_frame5, image=first_page2)
    label.grid(column=5,row=2)

    # Second page
    second_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c001.jpg")
    second_page2 = ImageTk.PhotoImage(second_page)
    label2 = ttk.Label(second_frame5, image=second_page2)
    label2.grid(column=5, row=3)

    # Third page
    third_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c002.jpg")
    third_page2 = ImageTk.PhotoImage(third_page)
    label3 = ttk.Label(second_frame5, image=third_page2)
    label3.grid(column=5, row=4)

    # Fourth Page
    fourth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c003.jpg")
    fourth_page2 = ImageTk.PhotoImage(fourth_page)
    label4 = ttk.Label(second_frame5, image=fourth_page2)
    label4.grid(column=5, row=5)

    # Fifth Page
    fifth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c004.jpg")
    fifth_page2 = ImageTk.PhotoImage(fifth_page)
    label5 = ttk.Label(second_frame5, image=fifth_page2)
    label5.grid(column=5, row=6)

    # Sixth Page
    sixth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c005.jpg")
    sixth_page2 = ImageTk.PhotoImage(sixth_page)
    label6 = ttk.Label(second_frame5, image=sixth_page2)
    label6.grid(column=5, row=7)

    # Seventh Page
    seventh_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c006.jpg")
    seventh_page2 = ImageTk.PhotoImage(seventh_page)
    label7 = ttk.Label(second_frame5, image=seventh_page2)
    label7.grid(column=5, row=8)

    # Eight Page
    eight_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c007.jpg")
    eight_page2 = ImageTk.PhotoImage(eight_page)
    label8 = ttk.Label(second_frame5, image=eight_page2)
    label8.grid(column=5, row=9)

    # Ninth Page
    ninth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c008.jpg")
    ninth_page2 = ImageTk.PhotoImage(ninth_page)
    label9 = ttk.Label(second_frame5, image=ninth_page2)
    label9.grid(column=5, row=10)

    # Tenth Page
    tenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c009.jpg")
    tenth_page2 = ImageTk.PhotoImage(tenth_page)
    label10 = ttk.Label(second_frame5, image=tenth_page2)
    label10.grid(column=5, row=11)

    # Eleven Page
    eleventh_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c010.jpg")
    eleventh_page2 = ImageTk.PhotoImage(eleventh_page)
    label11 = ttk.Label(second_frame5, image=eleventh_page2)
    label11.grid(column=5, row=12)

    # Twelve Page
    twelveth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c011.jpg")
    twelveth_page2 = ImageTk.PhotoImage(twelveth_page)
    label12 = ttk.Label(second_frame5, image=twelveth_page2)
    label12.grid(column=5, row=13)

    # Thirteen Page
    thirteenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c012.jpg")
    thirteenth_page2 = ImageTk.PhotoImage(thirteenth_page)
    label13 = ttk.Label(second_frame5, image=thirteenth_page2)
    label13.grid(column=5, row=14)

    # Fourteen Page
    fourteenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c013.jpg")
    fourteenth_page2 = ImageTk.PhotoImage(fourteenth_page)
    label14 = ttk.Label(second_frame5, image=fourteenth_page2)
    label14.grid(column=5, row=15)

    # Fifteen Page
    fifteenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c014.jpg")
    fifteenth_page2 = ImageTk.PhotoImage(fifteenth_page)
    label15 = ttk.Label(second_frame5, image=fifteenth_page2)
    label15.grid(column=5, row=16)

    # Sixteen Page
    sixteenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c015.jpg")
    sixteenth_page2 = ImageTk.PhotoImage(sixteenth_page)
    label16 = ttk.Label(second_frame5, image=sixteenth_page2)
    label16.grid(column=5, row=17)

    # Seventeen Page
    seventeenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c016.jpg")
    seventeenth_page2 = ImageTk.PhotoImage(seventeenth_page)
    label17 = ttk.Label(second_frame5, image=seventeenth_page2)
    label17.grid(column=5, row=18)

    # Eighteen Page
    eighteenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c017.jpg")
    eighteenth_page2 = ImageTk.PhotoImage(eighteenth_page)
    label18 = ttk.Label(second_frame5, image=eighteenth_page2)
    label18.grid(column=5, row=19)

    # Ninteen Page
    nineteenth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c018.jpg")
    nineteenth_page2 = ImageTk.PhotoImage(nineteenth_page)
    label19 = ttk.Label(second_frame5, image=nineteenth_page2)
    label19.grid(column=5, row=19)

    # Twenty
    twenty = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c019.jpg")
    twenty2 = ImageTk.PhotoImage(twenty)
    label20 = ttk.Label(second_frame5, image=twenty2)
    label20.grid(column=5, row=20)

    # twenty-one Page
    twentyone = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c020.jpg")
    twentyone2 = ImageTk.PhotoImage(twentyone)
    label21 = ttk.Label(second_frame5, image=twentyone2)
    label21.grid(column=5, row=21)

    # twenty-two Page
    twentytwo = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c021.jpg")
    twentytwo2 = ImageTk.PhotoImage(twentytwo)
    label22 = ttk.Label(second_frame5, image=twentytwo2)
    label22.grid(column=5, row=22)

    # twenty-three Page
    twentythree = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c022.jpg")
    twentythree2 = ImageTk.PhotoImage(twentythree)
    label23 = ttk.Label(second_frame5, image=twentythree2)
    label23.grid(column=5, row=23)

    # twenty-four Page
    twentyfour = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c023.jpg")
    twentyfour2 = ImageTk.PhotoImage(twentyfour)
    label24 = ttk.Label(second_frame5, image=twentyfour2)
    label24.grid(column=5, row=24)

    # twenty-five Page
    twentyfive = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c024.jpg")
    twentyfive2 = ImageTk.PhotoImage(twentyfive)
    label25 = ttk.Label(second_frame5, image=twentyfive2)
    label25.grid(column=5, row=25)

    # twenty-six Page
    twentysix = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c025.jpg")
    twentysix2 = ImageTk.PhotoImage(twentysix)
    label26 = ttk.Label(second_frame5, image=twentysix2)
    label26.grid(column=5, row=25)

    # twenty-seven Page
    twentyseven = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c026.jpg")
    twentyseven2 = ImageTk.PhotoImage(twentyseven)
    label27 = ttk.Label(second_frame5, image=twentyseven2)
    label27.grid(column=5, row=25)

    # twenty-eight Page
    twentyeight = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c027.jpg")
    twentyeight2 = ImageTk.PhotoImage(twentyeight)
    label28 = ttk.Label(second_frame5, image=twentyeight2)
    label28.grid(column=5, row=25)

    # twenty-nine Page
    twentynine = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c028.jpg")
    twentynine2 = ImageTk.PhotoImage(twentynine)
    label29 = ttk.Label(second_frame5, image=twentynine2)
    label29.grid(column=5, row=25)

    # thirty Page
    thirty = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c029.jpg")
    thirty2 = ImageTk.PhotoImage(thirty)
    label30 = ttk.Label(second_frame5, image=thirty2)
    label30.grid(column=5, row=25)

    # thirty-one Page
    thirtyone = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c030.jpg")
    thirtyone2 = ImageTk.PhotoImage(thirtyone)
    label31 = ttk.Label(second_frame5, image=thirtyone2)
    label31.grid(column=5, row=25)

    # thirty-two Page
    thirtytwo = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c031.jpg")
    thirtytwo2 = ImageTk.PhotoImage(thirtytwo)
    label32 = ttk.Label(second_frame5, image=thirtytwo2)
    label32.grid(column=5, row=25)

    # thirty-three Page
    thirtythree = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c032.jpg")
    thirtythree2 = ImageTk.PhotoImage(thirtythree)
    label33 = ttk.Label(second_frame5, image=thirtythree2)
    label33.grid(column=5, row=25)

    # thirty-four Page
    thirtyfour = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c033.jpg")
    thirtyfour2 = ImageTk.PhotoImage(thirtyfour)
    label34 = ttk.Label(second_frame5, image=thirtyfour2)
    label34.grid(column=5, row=25)

    # thirty-five Page
    thirtyfive = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Sousou no Frieren\\c034.jpg")
    thirtyfive2 = ImageTk.PhotoImage(thirtyfive)
    label35 = ttk.Label(second_frame5, image=thirtyfive2)
    label35.grid(column=5, row=25)

    sousounofrieren2.mainloop()

emptylabelfifth = Label(second_frame,text=" ",bg="white",activebackground="white")
emptylabelfifth.grid(column=5,row=17)

fifth_recommendation = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Recommendation\\Sousou no Frieren.png")
fifth_recommendation2 = Button(second_frame, image=fifth_recommendation, bg="#0448cb", activebackground="#0448cb",command=sousounofrieren)
fifth_recommendation2.grid(column=5,row=18)

button_mode6= True

def customize5(event4):
    global button_mode6

    if button_mode6:
        button7.config(image=off2, bg="#121212", activebackground="#121212")
        second_frame6.config(bg="#121212")
        my_canvas6.config(bg="#121212")
        button_mode6 = False
    else:
        button7.config(image=on2, bg="white", activebackground="white")
        second_frame6.config(bg="white")
        my_canvas6.config(bg="White")
        button_mode6 = True

def sololeveling():
    global sololeveling1, second_frame6, button7, my_canvas6

    sololeveling1 = Toplevel(root)
    sololeveling1.title("Solo Leveling")
    sololeveling1.state('zoomed')

    # Create a main frame
    main_frame6 = Frame(sololeveling1)
    main_frame6.pack(fill=BOTH, expand=1)

    # Create a Canvas
    my_canvas6 = Canvas(main_frame6, bg="white")
    my_canvas6.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar to the canvas
    my_scrollbar6 = ttk.Scrollbar(main_frame6, orient=VERTICAL, command=my_canvas6.yview)
    my_scrollbar6.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas6.configure(yscrollcommand=my_scrollbar6.set)
    my_canvas6.bind('<Configure>', lambda e: my_canvas6.configure(scrollregion=my_canvas6.bbox("all")))

    # Creates ANOTHER Frame INSIDE the Canvas
    second_frame6 = Frame(my_canvas6, bg="white")

    # Add that New Frame To a window In the Canvas
    my_canvas6.create_window((0, 0), window=second_frame6, anchor="center")

    # Home Page
    home_button = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Home Page.png")
    home_button2 = Button(second_frame6, image=home_button, bd=0, bg="#0448cb", activebackground="#0448cb", command=sololeveling1.destroy)
    home_button2.place(x=60, y=20)

    # Button
    button7 = Button(second_frame6, image=on2, bd=0, bg="white")
    button7.place(x=1300, y=20)
    button7.bind("<Button-1>",customize5)
    sololeveling1.bind("<F5>",customize5)

    # Tittle
    my_label = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Tittle 1.png")
    my_label1 = Label(second_frame6, image=my_label, bd=0, bg="white", activebackground="white")
    my_label1.grid(column=5, row=1)

    # zero Page
    zero = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Solo Leveling 2\\sololeveling1.png")
    zero2 = ImageTk.PhotoImage(zero)
    label1 = ttk.Label(second_frame6, image=zero2)
    label1.grid(column=5,row=2)

    # First Page
    first_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Solo Leveling 2\\sololeveling2.png")
    first_page2 = ImageTk.PhotoImage(first_page)
    label = ttk.Label(second_frame6, image=first_page2)
    label.grid(column=5,row=3)

    # Second page
    second_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Solo Leveling 2\\sololeveling3.png")
    second_page2 = ImageTk.PhotoImage(second_page)
    label2 = ttk.Label(second_frame6, image=second_page2)
    label2.grid(column=5, row=4)

    # Third page
    third_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Solo Leveling 2\\sololeveling4.png")
    third_page2 = ImageTk.PhotoImage(third_page)
    label3 = ttk.Label(second_frame6, image=third_page2)
    label3.grid(column=5, row=5)

    # Fourth Page
    fourth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Solo Leveling 2\\sololeveling5.png")
    fourth_page2 = ImageTk.PhotoImage(fourth_page)
    label4 = ttk.Label(second_frame6, image=fourth_page2)
    label4.grid(column=5, row=6)

    # Fifth Page
    fifth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Solo Leveling 2\\sololeveling6.png")
    fifth_page2 = ImageTk.PhotoImage(fifth_page)
    label5 = ttk.Label(second_frame6, image=fifth_page2)
    label5.grid(column=5, row=7)

    # Sixth Page
    sixth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Solo Leveling 2\\sololeveling7.png")
    sixth_page2 = ImageTk.PhotoImage(sixth_page)
    label6 = ttk.Label(second_frame6, image=sixth_page2)
    label6.grid(column=5, row=8)

    # Seventh Page
    seventh_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Solo Leveling 2\\sololeveling8.png")
    seventh_page2 = ImageTk.PhotoImage(seventh_page)
    label7 = ttk.Label(second_frame6, image=seventh_page2)
    label7.grid(column=5, row=9)

    # Eight Page
    eight_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Solo Leveling 2\\sololeveling9.png")
    eight_page2 = ImageTk.PhotoImage(eight_page)
    label8 = ttk.Label(second_frame6, image=eight_page2)
    label8.grid(column=5, row=10)

    # Ninth Page
    ninth_page = Image.open("C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Solo Leveling 2\\sololeveling10.png")
    ninth_page2 = ImageTk.PhotoImage(ninth_page)
    label9 = ttk.Label(second_frame6, image=ninth_page2)
    label9.grid(column=5, row=11)

    sololeveling1.mainloop()

# Recommendation Solo Leveling
third_recommendation = PhotoImage(file="C:\\Users\\TUF\\OneDrive\\Pictures\\Final Project Pictures\\Recommendation\\Solo Leveling 1.png")
third_recommendation2 = Button(second_frame, image=third_recommendation, bd=0, bg="white", activebackground="white", command=sololeveling)
third_recommendation2.grid(column=5, row=14)

main_page()
root.mainloop()