import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import mysql.connector
from PIL import Image
import tempfile
import subprocess
import os
import tkinter.messagebox
global db
db = mysql.connector.connect(
        host='localhost',
        user='root',
        port = '3306',
        password='',
        database="hms"
        )
    

user_o = 'Chanda'
pass_o = '123456'



def tab1( tab2, interface1):
    global window
    window = ctk.CTk()
    window.geometry('1000x700')
    window.title('Chanda HPS')
    #window._set_appearance_mode("dark")
    #======================================================widget calling======================================================
    interface1(tab2) 
    
    window.resizable(False,False)
    window.mainloop()    


    

def tab2(value):
    for i in value:
        i.destroy()
    #======================================================frame in tab2====================================================== 
    window.rowconfigure(0,weight=5)  
    window.rowconfigure(1,weight=5)
    window.rowconfigure(2,weight=5)
    window.config(bg='white')
    frame1= ctk.CTkFrame(window, width= 1000, height= 75, fg_color= '#141414', corner_radius=-1)
    frame1.grid(column= 0, row = 0)
    frame2= ctk.CTkFrame(window, width= 1000, height= 300, fg_color= '#141414', corner_radius=-1)
    frame2.grid(column= 0, row = 1, pady =5) 
    frame4= ctk.CTkFrame(frame2, width= 690, height= 280, fg_color= 'white', corner_radius=-1)
    frame4.grid(column= 0, row = 1, padx= 3,  pady= 5)
    frame5= ctk.CTkFrame(frame2, width= 290, height= 280, fg_color= 'white', corner_radius=-1,)
    frame5.grid(column= 1, row = 1, padx =3, pady =5)
    frame3= ctk.CTkFrame(window, width= 1000, height= 325, fg_color= '#141414', corner_radius=-1)
    frame3.grid(column= 0, row = 2)
    f = ('Lexend', 45, 'bold')
    plus = ctk.CTkLabel(frame1, text='+', font=('lexend', 80, 'bold'), text_color='red')
    plus.place(x= 1000/2 - 450, y = 75/2 - 50)
    Hos = ctk.CTkLabel(frame1, text='Chanda Hospital Management System', font=f, text_color='#48ff00')
    Hos.place(x= 1000/2 - 380, y = 75/2 - 30)
    
    
    #======================================================entry box======================================================
    entry1 = tk.Entry(frame4, width=15, font=('Arial',20), fg='#d4d4d4', bg="white",background='#696969', relief="solid")
    entry1.place(x=120, y=20)
    entry2 = tk.Entry(frame4, width=15, font=('Arial',20), fg='#d4d4d4', bg="white",background='#696969', relief="solid")
    entry2.place(x=120, y=90)
    entry3 = tk.Entry(frame4, width=15, font=('Arial',20), fg='#d4d4d4', bg="white",background='#696969', relief="solid")
    entry3.place(x=120, y=160)
    entry4 = tk.Entry(frame4, width=15, font=('Arial',20), fg='#d4d4d4', bg="white",background='#696969', relief="solid")
    entry4.place(x=120, y=230)
    entry5 = tk.Entry(frame4, width=15, font=('Arial',20), fg='#d4d4d4', bg="white",background='#696969', relief="solid")
    entry5.place(x=550, y=20)
    entry6 = tk.Entry(frame4, width=15, font=('Arial',20), fg='#d4d4d4', bg="#696969",background='#696969', relief="solid")
    entry6.place(x=550, y=90)
    entry7 = tk.Entry(frame4, width=15, font=('Arial',20), fg='#d4d4d4', bg="#696969",background='#696969', relief="solid")
    entry7.place(x=550, y=160)
    entry8 = tk.Entry(frame4, width=15, font=('Arial',20), fg='#d4d4d4', bg="#696969",background='#696969', relief="solid")
    entry8.place(x=550, y=230)
    
    
    #======================================================string for label======================================================
    Id =  ctk.CTkLabel(frame4, text='ID:', font=('Arial', 16, 'bold'), text_color='#000000')
    Id.place(x= 70, y=15)
    Name =  ctk.CTkLabel(frame4, text='Name:', font=('Arial', 16, 'bold'), text_color='#000000')
    Name.place(x= 45, y=70)
    D_Name =  ctk.CTkLabel(frame4, text='Blood:', font=('Arial',16 , 'bold'), text_color='#000000')
    D_Name.place(x= 35, y=126)
    Phone =  ctk.CTkLabel(frame4, text='Phone:', font=('Arial', 16, 'bold'), text_color='#000000')
    Phone.place(x= 38, y=182)
    Medi =  ctk.CTkLabel(frame4, text='Medicine:', font=('Arial', 16, 'bold'), text_color='#000000')
    Medi.place(x= 360, y=15)
    Gender =  ctk.CTkLabel(frame4, text='Gender:', font=('Arial', 16, 'bold'), text_color='#000000')
    Gender.place(x= 370, y=70)
    Date =  ctk.CTkLabel(frame4, text='Birth:', font=('Arial',16 , 'bold'), text_color='#000000')
    Date.place(x= 392, y=126)
    Time =  ctk.CTkLabel(frame4, text='Time:', font=('Arial', 16, 'bold'), text_color='#000000')
    Time.place(x= 390, y=182)
    #======================================================function======================================================
    def bac(d):
        for l in d:
            l.destroy()
        tab1(interface1(tab2))
    def iprint():
        q = text.get("1.0","end-1c")
        filename = tempfile.mktemp(".text")
        with open (filename, "w") as file:
            file.write(q)
        subprocess.Popen(['notepad.exe', '/p', filename], shell=True)
        
    def add_data():
        value = (entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get(), entry7.get(), entry8.get())
        db_cursor = db.cursor()
        db_cursor.execute("INSERT INTO hms1(id, name, doctor, phone, medicine, gender, date, time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", value)
        db.commit()
        db_cursor.close()
    
        tree.insert('', 'end', values=value)  # Update Treeview with new data 
        global all_entry
        all_entry = [entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8]
        for b in all_entry:
            b.delete(0, 'end')

                
    def remove_row():
        selected_item = tree.selection()  # Get selected item in Treeview
        if selected_item:  # Check if item is selected
            item_id = selected_item[0]  # Get ID of selected item
            values = tree.item(item_id, 'values')  # Get values of selected item
            db_cursor = db.cursor()
            db_cursor.execute("DELETE FROM hms1 WHERE id = %s", (values[0],))  # Delete record from database
            db.commit()
            db_cursor.close()
            tree.delete(item_id)  # Delete selected item from Treeview
    
    def res():
        all_entry = [entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8,]
        for b in all_entry:
            b.delete(0, 'end')
        text.delete('1.0', 'end')
            
    def populate_treeview():
        cursor = db.cursor()
        cursor.execute("SELECT * FROM hms1")  # Assuming hms1 is your table name
        rows = cursor.fetchall()
        for row in rows:
            tree.insert('', 'end', values=row)
        cursor.close()
    # Define tree globally
    global tree
    
    def display():
        selected_item = tree.selection()
        if selected_item:
            item = tree.item(selected_item)
            values = item['values']
            line1 = "=" * 51  # Adjust to match the width of the text box
            text.insert(tk.END, f"\n{line1}\n\n")
            invoice_text = "\tChanda HMS\n\n"
            
            for header, value in zip(tree['columns'], values):
                
                invoice_text += f"              {header}:    {value}\n"
        
        # Clear previous content of the text widget
            text.delete('1.0', tk.END)
        
        # Insert the invoice text into the text widget with font styling
            text.insert(tk.END, invoice_text)
            text.tag_configure("header", font=("Times New Roman", 20, "bold"))  # Font styling for the header
            text.tag_add("header", "1.0", "1.0 lineend")  # Apply the font styling to the header
        
        # Add decorative lines
            line2 = "=" * 51  # Adjust to match the width of the text box
            text.insert(tk.END, f"\n{line2}\n\n")



    # Create a text widget to display the invoice-like text

    # Create a label to display the invoice-like text

    #======================================================button in frame4======================================================
    add = ctk.CTkButton(frame4, width= 70 ,text='Add', font=('Arial', 14, 'bold'), text_color='#ff0000',fg_color='transparent', bg_color='#141414', hover_color='#c7c7c7', corner_radius=-1, command= add_data)
    add.place(x=40, y=250)
    delete = ctk.CTkButton(frame4, width= 70 ,text='Delete', font=('Arial', 14, 'bold'), text_color='#ff0000',fg_color='transparent', bg_color='#141414', hover_color='#c7c7c7', corner_radius=-1, command= remove_row)
    delete.place(x=115, y=250)
    show = ctk.CTkButton(frame4, width= 100 ,text='Show', font=('Arial', 14, 'bold'), text_color='#ff0000',fg_color='transparent', bg_color='#141414', hover_color='#c7c7c7', corner_radius=-1, command=  display)
    show.place(x=190, y=250)
    reset = ctk.CTkButton(frame4, width= 115 ,text='Reset', font=('Arial', 14, 'bold'), text_color='#ff0000',fg_color='transparent', bg_color='#141414', hover_color='#c7c7c7', corner_radius=-1, command=res)
    reset.place(x=295, y=250)
    back = ctk.CTkButton(frame4, width= 120 ,text='Back', font=('Arial', 14, 'bold'), text_color='#ff0000',fg_color='transparent', bg_color='#141414', hover_color='#c7c7c7', corner_radius=-1,
    command= lambda: bac([frame1,frame2,frame3,frame4,frame5, plus, Hos, entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,Id,Name,D_Name,Phone,Medi,Gender,Date,Time,add,delete,show,reset]) )
    back.place(x=415, y=250)
    Print =  ctk.CTkButton(frame4, width= 100 ,text='Print', font=('Arial', 14, 'bold'), text_color='#ff0000',fg_color='transparent', bg_color='#141414', hover_color='#c7c7c7', corner_radius=-1, command=iprint,state='normal')
    Print.place(x=540, y=250)
    #======================================================text-widget======================================================
    text = tk.Text(frame5, bg='#cfcfcf', fg='black',font=('Arial', 14, 'bold') ,width= 51, height=21)
    text.place(x = 1, y=5)
    
    
    #======================================================treeview======================================================
    

    tree = ttk.Treeview(frame3,height=200, selectmode='browse',
                      columns=('ID', "Name", "Blood", "Phone", "Medicine","Gender", "Birth", "Time"))
    s = ttk.Style(frame3)
    s.theme_use('clam')
    s.configure("Treeview.Heading", background = '#141414' ,foreground = '#48ff00', font=('Arial',15, 'bold'))
    s.configure("Treeview", font=('Arial', 14))
    X_scroller = tk.Scrollbar(tree, orient='horizontal', command=tree.xview)
    Y_scroller = tk.Scrollbar(tree, orient='vertical', command=tree.yview)
    X_scroller.pack(side='bottom', fill='x')
    Y_scroller.pack(side='right', fill='y')
    tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
    tree.heading('ID', text='ID', anchor='center')
    tree.heading('Name', text='Name', anchor='center')
    tree.heading('Blood', text='Blood', anchor='center')
    tree.heading('Phone', text='Phone', anchor='center')
    tree.heading('Gender', text='Gender', anchor='center')
    tree.heading('Medicine', text='Medicine', anchor='center')
    tree.heading('Birth', text='Birth', anchor='center')
    tree.heading('Time', text='TIME', anchor='center')
    tree.column('#0', width=0, stretch='no', anchor='center')
    tree.column('#1', width=70, minwidth=100, stretch='yes', anchor='center')
    tree.column('#2', width=120, minwidth=100, stretch='yes', anchor='center')
    tree.column('#3', width=150, minwidth=100, stretch='yes', anchor='center')
    tree.column('#4', width=120, minwidth=100, stretch='yes', anchor='center')
    tree.column('#5', width=120, minwidth=100, stretch='yes', anchor='center')
    tree.column('#6', width=120, minwidth=100, stretch='yes', anchor='center')
    tree.column('#7', width=120, minwidth=100, stretch='yes', anchor='center')
    tree.column('#8', width=120, minwidth=100, stretch='yes', anchor='center')
    tree.place(y=0, relwidth=1, relheight=0.9, relx=0)
    populate_treeview()
    
    
    
    
  


    
def interface1(tab2):
    global home, frame0, login, Username, Password, issue, hospital
    
    mountain = ctk.CTkImage(light_image=Image.open('mountain.jpg'),
                            dark_image=Image.open('mountain.jpg'), size=(1000,700))
    home = ctk.CTkLabel(window, text='', image=mountain)
    home.place(x=0, y=0)
    frame0 = tk.Frame(home, width=570, height=500, background='#141414', bg=None)
    frame0.place(x=320, y=150)
    f = ('Lexend', 45, 'bold')
    login = ctk.CTkLabel(frame0, text='SIGN IN', font=f, text_color='#48ff00')
    login.place(x=500/2 - 110, y=50)
    Username = tk.Entry(frame0, width=20, font=('Arial',30), fg='#a3a6a2', bg="#2a2b2a", relief='flat')
    Username.place(x=60, y=500/2 - 70)
    Username.insert(0, 'username')
    Password = tk.Entry(frame0, width=20, font=('Arial',30), fg='#a3a6a2', bg="#2a2b2a", relief='flat')
    Password.place(x=60, y=500/2 + 20)
    Password.insert(0, 'password')
    hospital = ctk.CTkLabel(frame0, text='HOSPITAL MS', font=('Arial', 14, 'bold'), text_color='#48ff00')
    hospital.place(x=300, y=500/2 + 20) 
    
    #======================================================function======================================================
    def IT(): 
        new_w = ctk.CTk()
        new_w.title('IT contact')
        new_w.geometry('300x300')
    
    
        new_w.resizable(False,False)
        new_w.mainloop()
        
    def wrong():
        print('Hello bro!')
        la = ctk.CTkLabel(frame0, fg_color='transparent', bg_color="transparent",text= 'Wrong Password!', font= ('Arial', 12, 'bold'), text_color='red')
        la.place(x= 400/2 - 20, y= 500/2 + 110)
        
    
    
        
    #======================================================button======================================================      
    issue = ctk.CTkButton(frame0, text='CONTACT TO IT', font=('Arial', 14, 'bold'), text_color='#a3a6a2',
                          fg_color='transparent', bg_color='#141414', hover_color='#141414', command=IT)
    issue.place(x=35, y=500/2 + 20)
    button_login = ctk.CTkButton(frame0, height=40, hover_color='grey', width=355, corner_radius=-3,
                                 text='login', font=('Lexend', 25, 'bold'), text_color='#121212',
                                 fg_color='#48ff00',
                                 command=
    lambda: (tab2([home, frame0, login, Username, Password, issue, hospital]) if (Username.get() == user_o) and (Password.get()==pass_o) else wrong()))
    button_login.place(x=47, y=500/2 + 70)    



tab1( tab2, interface1)



