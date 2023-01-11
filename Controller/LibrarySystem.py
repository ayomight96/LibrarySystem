from PIL import Image, ImageTk
from tkinter.ttk import *
import tkinter as tk
import sys
import tkinter.messagebox

sys.path.insert(1, '/Users/mac/Documents/PYTHON FOLDER/LibrarySystem')
from Controller.GuiFunctions import GuiFunctions



class LibrarySystem:

    userData = []

    def __init__(self, root):
        root.title('Library Management System')
        mainframe = Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        canvas = tk.Canvas(mainframe, width=800, height=500)
        canvas.grid(columnspan=3, rowspan=7)

        logo = Image.open('libraryImage.jpeg')
        logo = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(mainframe, image=logo, width=700, height=400)
        logo_label.image = logo
        logo_label.grid(column=1, row=1)

        # Instructions
        instructions = tk.Label(
            mainframe, text='Sign Up to Use the Library System. Log In if you are a returning User', font='Raleway')
        instructions.grid(columnspan=3, column=0, row=2)

        # Sign Up Button
        signUpText = tk.StringVar()
        signUpBtn = tk.Button(mainframe, textvariable=signUpText,
                              command=lambda: self.signUp(root), font='Raleway', height=2, width=15)
        signUpText.set('Sign Up')
        signUpBtn.grid(column=1, row=3)

        # Sign In Button
        signInText = tk.StringVar()
        signInBtn = tk.Button(mainframe, textvariable=signInText,
                              command=lambda: self.signIn(root),
                              font='Raleway', height=2, width=15)
        signInText.set('Sign In')
        signInBtn.grid(column=1, row=4)

        canvas = tk.Canvas(mainframe, width=600, height=250)
        canvas.grid(columnspan=3)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def signUp(self, root):
        signUpWindow = tk.Toplevel(root)
        signUpWindow.geometry('600x600')
        signUpWindow.resizable(False, False)
        signUpWindow.title('Sign Up Form')
        signUpFormLabel = tk.Label(signUpWindow, text='Sign Up form',
                                   width=20, font=('bold', 20))
        signUpFormLabel.place(x=180, y=20)
        fullNameLabel = tk.Label(signUpWindow, text='FullName',
                                 width=20, font=('bold', 10))
        fullNameLabel.place(x=80, y=130)
        fullNameEntry = tk.Entry(signUpWindow)
        fullNameEntry.place(x=240, y=130)
        UserNameLabel = tk.Label(
            signUpWindow, text='UserName', width=20, font=('bold', 10))
        UserNameLabel.place(x=80, y=180)
        userNameEntry = tk.Entry(signUpWindow)
        userNameEntry.place(x=240, y=180)
        passwordLabel = tk.Label(
            signUpWindow, text='Password', width=20, font=('bold', 10))
        passwordLabel.place(x=80, y=230)
        passwordEntry = tk.Entry(signUpWindow, show="*")
        passwordEntry.place(x=240, y=230)
        confirmPasswordLabel = tk.Label(
            signUpWindow, text='Confirm Password', width=20, font=('bold', 10))
        confirmPasswordLabel.place(x=80, y=280)
        confirmPasswordEntry = tk.Entry(signUpWindow, show="*")
        confirmPasswordEntry.place(x=240, y=280)
        userTypeList = ('Student', 'Staff')
        userTypeText = tk.StringVar(signUpWindow)
        userTypeText.set('None')
        dropDownlist = OptionMenu(signUpWindow, userTypeText, *userTypeList)
        dropDownlist.pack()
        userTypeLabel = Label(signUpWindow, text='Who are you?',
                              width=20, font=('arial', 12))
        userTypeLabel.place(x=120, y=330)
        dropDownlist.place(x=300, y=330)
        guiFunctions = GuiFunctions()
        tk.Button(signUpWindow, text='Submit', width=20, height=1, bg='white',
                  fg='black', command=lambda: guiFunctions.signUpSubmitButton(
                      userName=str(userNameEntry.get()),
                      fullName=str(fullNameEntry.get()),
                      password=str(passwordEntry.get()),
                      confirmPassword=str(confirmPasswordEntry.get()),
                      userType='Student'
                  )
                  ).place(x=230, y=380)

    def setCurrrentLoggedInUser(self, userName, password):
        if userName is not None and password is not None:
            guiFunctions = GuiFunctions()
            data = guiFunctions.signInSubmitButton(
                userName=userName,
                password=password
            )
            self.userData.append(data)
            tkinter.messagebox.showinfo(
                "Welcome ", "Welcome " + data['fullName'] + ", The Buttons on this page are now accessible to you!")
        else:
            tkinter.messagebox.showinfo('No Entry', 'Fill all fields')
        # call a new window
        # destroy current

    def booksBorrowed(self):
        if len(self.userData) > 0:
            tkinter.messagebox.showinfo(
                "Welcome ", "Welcome " + self.userData[0]['fullName'])
        else:
            tkinter.messagebox.showinfo(
                'No Logged in User', 'Kindly log in to assess this button')

    def booksReturned(self):
        if len(self.userData) > 0:
            tkinter.messagebox.showinfo(
                "Welcome ", "Welcome " + self.userData[0]['fullName'])
        else:
            tkinter.messagebox.showinfo(
                'No Logged in User', 'Kindly log in to assess this button')

    def booksReserved(self):
        if len(self.userData) > 0:
            tkinter.messagebox.showinfo(
                "Welcome ", "Welcome " + self.userData[0]['fullName'])
        else:
            tkinter.messagebox.showinfo(
                'No Logged in User', 'Kindly log in to assess this button')

    def booksLost(self):
        if len(self.userData) > 0:
            tkinter.messagebox.showinfo(
                "Welcome ", "Welcome " + self.userData[0]['fullName'])
        else:
            tkinter.messagebox.showinfo(
                'No Logged in User', 'Kindly log in to assess this button')

    def signIn(self, root):
        signInWindow = tk.Toplevel(root)
        signInWindow.geometry('1000x700')
        signInWindow.resizable(False, False)
        signInWindow.title('User Library Iterface')
        signInFormLabel = tk.Label(signInWindow, text='Sign in to access the Library System',
                                   width=30, font=('bold', 20))
        signInFormLabel.place(x=-20, y=6)
        UserNameLabel = tk.Label(
            signInWindow, text='UserName', width=25, font=('bold', 20))
        UserNameLabel.place(x=-90, y=60)
        userNameEntry = tk.Entry(signInWindow)
        userNameEntry.place(x=150, y=60)
        passwordLabel = tk.Label(
            signInWindow, text='Password', width=25, font=('bold', 20))
        passwordLabel.place(x=-90, y=110)
        passwordEntry = tk.Entry(signInWindow, show="*")
        passwordEntry.place(x=150, y=110)
        tk.Button(signInWindow, text='Unlock', width=15, height=1, bg='white',
                  fg='black', activebackground='grey', command=lambda: self.setCurrrentLoggedInUser(
                      userName=str(userNameEntry.get()),
                      password=str(passwordEntry.get())
                  )
                  ).place(x=155, y=150)
        tk.Button(signInWindow, text='Books Borrowed', width=15, height=1, bg='white',
                  fg='black', activebackground='grey', command=lambda: self.booksBorrowed(
                      userData=self.userData
                  )
                  ).place(x=100, y=280)
        tk.Button(signInWindow, text='Books Returned', width=15, height=1, bg='white',
                  fg='black', activebackground='grey', command=lambda: self.booksReturned(
                      userData=self.userData
                  )
                  ).place(x=100, y=310)
        tk.Button(signInWindow, text='Books Reserved', width=15, height=1, bg='white',
                  fg='black', activebackground='grey', command=lambda: self.booksReserved(
                      userData=self.userData
                  )
                  ).place(x=100, y=340)
        tk.Button(signInWindow, text='Books Lost', width=15, height=1, bg='white',
                  fg='black', activebackground='grey', command=lambda: self.booksLost(
                      userData=self.userData
                  )
                  ).place(x=100, y=370)
        infoFrame = Frame(signInWindow, height=200, width=500)
        infoFrame.pack_propagate(0)
        infoFrame.place(x=100, y=410)
        infoLabel = tk.Label(
            infoFrame, text='', width=20, font=('bold', 20), background='white')
        infoLabel.pack(fill='both', expand=1)
