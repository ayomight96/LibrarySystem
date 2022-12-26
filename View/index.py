# import sys

# sys.path.insert(1, '/Users/mac/Documents/PYTHON FOLDER/LibrarySystem')

# from Model.Book import Book


# book = Book(
#     1,
#     'boy',
#     'boy',
#     'boy',
#     'boy',
#     'boy',
#     'boy',
#     'boy',
#     'boy',
#     'boy',
#     'boy',
#     'boy',
#     'boy',
#     'boy'
# )

# book.setLendingDateTest('12/8/2022')

# print(book.toString(book.lendingDate))
# # print(book.toString(book.lendingDate))

# print (book.lendingAge())

import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=7)

logo = Image.open('libLogo.jpeg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=1)

# Instructions
instructions = tk.Label(
    root, text='Sign Up to Use the Library System. Log In if you are a returning User', font='Raleway')
instructions.grid(columnspan=3, column=0, row=2)


def signUp():
    signUpWindow = tk.Toplevel(root)
    signUpWindow.geometry('600x600')
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
    passwordEntry = tk.Entry(signUpWindow)
    passwordEntry.place(x=240, y=230)
    confirmPasswordLabel = tk.Label(
        signUpWindow, text='Confirm Password', width=20, font=('bold', 10))
    confirmPasswordLabel.place(x=80, y=280)
    confirmPasswordEntry = tk.Entry(signUpWindow)
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
    if fullNameEntry.get() and userNameEntry.get() and passwordEntry.get() and confirmPasswordEntry.get() and (passwordEntry.get() == confirmPasswordEntry.get()):
        
    signUpDetails = {
        'fullName': fullNameEntry.get(),
        'userName': userNameEntry.get(),
        'password': passwordEntry.get(),
        'confirmPassword': confirmPasswordEntry.get()
    }
    tk.Button(signUpWindow, text='Submit', width=20, height=1, bg='white',
              fg='black', command=lambda: verifySignUpDetails(signUpDetails)).place(x=230, y=380)


def verifySignUpDetails(signUpDetails):


    # Sign Up Button
signUpText = tk.StringVar()
signUpBtn = tk.Button(root, textvariable=signUpText,
                      command=lambda: signUp(), font='Raleway', height=2, width=15)
signUpText.set('Sign Up')
signUpBtn.grid(column=1, row=3)

# Sign In Button
signInText = tk.StringVar()
signInBtn = tk.Button(root, textvariable=signInText,
                      font='Raleway', height=2, width=15)
signInText.set('Sign In')
signInBtn.grid(column=1, row=4)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)


root.mainloop()
