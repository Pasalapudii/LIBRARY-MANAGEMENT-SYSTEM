import customtkinter
import bcrypt
import sqlite3
from tkinter import *
from tkinter import messagebox
import subprocess

app = customtkinter.CTk()
app.title('Login')
app.geometry("950x500")
app.config(bg='lightblue')

font1 = ('Helvetica',25,'bold')
font2 = ('Arial',17,'bold')
font3 =('Arial',13,'bold')
font4 = ('Arial',13,'bold','underline')

conn = sqlite3.connect('sign.db')
cursor = conn.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS users(
               username TEXT NOT NULL,
               password TEXT NOT NULL)''')

def signup():
    username = username_entry.get()
    password = password_entry.get()
    if username != '' and password != '':
        cursor.execute('SELECT username FROM users WHERE username=?',[username])
        if cursor.fetchone() is not None:
            messagebox.showerror('Error','Username already exists.')
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password,bcrypt.gensalt())
            cursor.execute('INSERT INTO users VALUES (?,?)',[username,hashed_password])
            conn.commit()
            messagebox.showinfo('Succes','Account has been created.')
    else:
        messagebox.showerror('Error','Enter all data.')

def logof():
    username2 = username_entry2.get()
    password2 = password_entry2.get()
    if username2 != '' and password2 != '':
        cursor.execute('SELECT username,password FROM users WHERE username=?',[username2])
        user = cursor.fetchone()
        if user:
            hashed_password_from_db = user[1]
            if bcrypt.checkpw(password2.encode('utf-8'), hashed_password_from_db):
                messagebox.showinfo('Success', 'Login Successful!')
                return True
            else:
                messagebox.showerror('Error','Username or password is invalid!!!')
                return False
        else:
            messagebox.showerror('Error','Username or password is invalid!!!')
            return False
    else:
        messagebox.showerror('Error','Enter all data.')
        return False

def library():
    subprocess.run(["python", "C:/Users/lohit/OneDrive/Desktop/WiseProject/librarymanagementsystem.py"])

def log_in():
    frame1.destroy()
    frame2 = customtkinter.CTkFrame(app,bg_color='lightblue',fg_color='white',width=450,height=300)
    frame2.place(relx=0.5, rely=0.5, anchor=CENTER) 

    login_label2 = customtkinter.CTkLabel(frame2,font=font1,text='LOGIN',text_color='red',bg_color='white')
    login_label2.place(x=200,y=20)

    global username_entry2
    global password_entry2

    username_entry2=customtkinter.CTkEntry(frame2,font=font2,text_color='black',bg_color='lightblue',border_color='black',border_width=3,placeholder_text='Username',placeholder_text_color='grey',width=200,height=50)
    username_entry2.place(x=150,y=80)

    password_entry2=customtkinter.CTkEntry(frame2,font=font2,show='*',text_color='black',bg_color='lightblue',border_color='black',border_width=3,placeholder_text='Password',placeholder_text_color='grey',width=200,height=50)
    password_entry2.place(x=150,y=150)

    login_button2 = customtkinter.CTkButton(frame2,command=user,font=font4,text_color='red',text='LOGIN',fg_color='green',hover_color='darkgreen',cursor='hand2',bg_color='lightblue',corner_radius=5,width=120)
    login_button2.place(x=150,y=220)
def user():
    if logof():
        library()


frame1 = customtkinter.CTkFrame(app,bg_color='lightblue',fg_color='white',width=550,height=500)
frame1.place(relx=0.5, rely=0.5, anchor=CENTER) 

signup_label = customtkinter.CTkLabel(frame1,font=font1,text='Sign up',text_color='red',)
signup_label.place(x=200,y=20)

username_entry = customtkinter.CTkEntry(frame1,font=font2,text_color='black',border_color='black',border_width=3,placeholder_text='Username',placeholder_text_color='#a3a3a3',width=200,height=50)
username_entry.place(x=150,y=80)

password_entry = customtkinter.CTkEntry(frame1,font=font2,show='*',text_color='black',fg_color='white',bg_color='lightblue',border_color='black',border_width=3,placeholder_text='Password',placeholder_text_color='#a3a3a3',width=200,height=50)
password_entry.place(x=150,y=150)

signup_button = customtkinter.CTkButton(frame1,command=signup,font=font2,text_color='Red',text='Sign up',fg_color='#00965d',hover_color='#006e44',bg_color='lightblue',cursor='hand2',corner_radius=5,width=120)
signup_button.place(x=150,y=220)

login_label=customtkinter.CTkLabel(frame1,font=font3,text='Already have an account?',text_color='black',bg_color='white')
login_label.place(x=150,y=250)

login_button = customtkinter.CTkButton(frame1,font=font4,command=log_in,text_color='green',text='Login',hover_color='lightblue',fg_color='skyblue',cursor='hand2',width=40)
login_button.place(x=320,y=250)


# app.iconbitmap("favicon.ico")


app.mainloop()