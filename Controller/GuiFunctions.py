from Model.User import User
import sys
import tkinter.messagebox

sys.path.insert(1, '/Users/mac/Documents/PYTHON FOLDER/LibrarySystem')
from Controller.DatabaseConnection import DatabaseConnection

class GuiFunctions:

    def signUpSubmitButton(
        self,
            fullName: str,
            userName: str,
            userType: str,
            password: str,
            confirmPassword: str):
        if password != confirmPassword:
            tkinter.messagebox.showinfo(
                "Invalid Entry", "Password does not match")
        if fullName is not None and userName is not None:
            if self.verifyIfUserExist(userName=userName, password=password) == False:
                databaseConnection = self.instantiateConnection()
                user = User(
                    userType=userType,
                    userName=userName,
                    password=password,
                    fullName=fullName
                )
                databaseConnection.insert('User', user.data())
                tkinter.messagebox.showinfo(
                    "Success", "User succesfully created")
            else:
                tkinter.messagebox.showinfo(
                    "Duplicate Entry", "This User Already Exists. Kindly sign in")
        else:
            tkinter.messagebox.showinfo(
                "Invalid Entry", "Fields cannot be empty")

    def signInSubmitButton(
        self,
            userName: str,
            password: str,
    ):
        data = self.verifyIfUserExist(userName=userName, password=password)
        if data != False:
            userData = User.userDataFromDatabase(data=data)
            return userData
        else:
            tkinter.messagebox.showinfo(
                "Invalid Sign in", "Password or Username incorrect")

    def verifyIfUserExist(
        self,
            userName: str,
            password: str
    ):
        databaseConnection = self.instantiateConnection()
        status = databaseConnection.retrieve(
            'User', searchParameter={
                'userName': userName,
                'password': password
            })
        if status == False:
            return False
        else:
            return status

    def instantiateConnection(
            self):
        databaseConnection = DatabaseConnection()
        return databaseConnection
