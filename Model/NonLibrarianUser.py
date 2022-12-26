import sys

sys.path.insert(1, '/Users/mac/Documents/PYTHON FOLDER/LibrarySystem')

from Model.User import User
from datetime import datetime

class NonLibrarianUser(User):
    borrowedBooks = []
    reservedBooks = []
    returnedBooks = []
    lostBooks = []
    fine = 0.0

    def borrowBook(self, id:str):
        self.borrowedBooks[id] = {
            'id':id,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def reserveBook(self, id:str):
        self.reservedBooks[id] = {
            'id':id,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def returnBook(self, id:str):
        self.returnedBooks[id] = {
            'id':id,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }