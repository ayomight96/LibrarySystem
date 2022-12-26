import sqlite3


class DatabaseConnection:
    def __init__(self) -> any:
        connection = self.openConnection()
        cursor = connection.cursor()
        cursor.execute(
            """create table User(
                id text,
                name text,
                userName text,
                password text,
                userType text,
                userStation text,
                fine real
                )""")
        cursor.execute(
            """create table Book(
                id integer,
                title text,
                authors text,
                averageRating real,
                isbn integer,
                isbn13 integer,
                languageCode text,
                numberOfPages integer,
                ratingsCount integer,
                textReviewsCount integer,
                publicationDate text,
                copy integer,
                copies integer,
                isReserved integer,
                isBookRequested integer,
                isBookAvailable integer,
                feedback text
                )""")
        cursor.execute(
            """create table BorrowedBooks(
                id text,
                bookId integer,
                dateBorrowed text,
                dueDate text
                )""")
        cursor.execute(
            """create table ReturnedBooks(
                id text,
                bookId integer,
                dateReturned text
                )""")
        cursor.execute(
            """create table ReservedBooks(
                id text,
                bookId integer,
                dateReserved text
                )""")
        cursor.execute(
            """create table LostBooks(
                id text,
                bookId integer,
                dateLost text
                )""")
        connection.commit()
        self.connection.close
        print('Database and Tables Succesfully created')

    def openConnection(self):
        connection = sqlite3.connect("LibrarySystem.db")
        self.connection = connection
        return connection

    def closeConnection(self):
        self.connection.close()

    def insert(self, tableName: str, data: dict) -> bool:
        connection = self.openConnection()
        cursor = connection.cursor()
        for key in data:
            if key == 'id':
                uniqueId = key
                cursor.execute(
                    "insert into " + tableName + " (" + key + ")values (?)", (data[key],))
                connection.commit()
                self.closeConnection()
                return True
            else:
                self.update(tableName, data[uniqueId], data)

    def update(self, tableName: str, uniqueId: any, data: dict) -> bool:
        connection = self.openConnection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM " + tableName + " WHERE id = :id", {"id": uniqueId})
        rowData = cursor.fetchall()
        if len(rowData) != 0:
            for key in data:
                if key != 'id':
                    cursor.execute(
                        "UPDATE " + tableName + " SET " + key + "=%s" + " WHERE id =%s", (data[key], uniqueId))
                    connection.commit()
                    self.connection.close()
                    return print(True)
        else:
            raise Exception("Invalid SearchParameters")

# remeber to put a limit to the search parameters passed
    def retrieve(self, tableName: str, searchParameter: any, searchParameterValue=None):
        connection = self.openConnection()
        cursor = connection.cursor()
        if type(searchParameter) is dict:
            dictCount = len(searchParameter)
            if dictCount < 2 or dictCount > 4:
                raise Exception("Invalid SearchParameters")
            counter = 0
            queryString = ""
            queryVaraibles = []
            for key in searchParameter:
                queryString += key + " = :" + key
                queryVaraibles[counter] = searchParameter[key]
                if counter < dictCount:
                    queryString += "AND "
                counter += 1
            fullQueryString = "SELECT * FROM " + tableName + " WHERE " + queryString
            match dictCount:
                case 2:
                    cursor.execute(fullQueryString,
                                   (searchParameter[0], searchParameter[1]))
                    data = cursor.fetchall()
                    if len(data) != 0:
                        return data
                    else:
                        return False
                case 3:
                    cursor.execute(
                        fullQueryString, (searchParameter[0], searchParameter[1], searchParameter[2]))
                    data = cursor.fetchall()
                    if len(data) != 0:
                        return data
                    else:
                        return False
                case 4:
                    cursor.execute(
                        fullQueryString, (searchParameter[0], searchParameter[1], searchParameter[2], searchParameter[3]))
                    data = cursor.fetchall()
                    if len(data) != 0:
                        return data
                    else:
                        return False
        else:
            cursor.execute(
                "SELECT * FROM " + tableName + " WHERE " + searchParameter + " = ?", (searchParameterValue,))
        self.closeConnection()


databaseConnection = DatabaseConnection()
databaseConnection.insert(
    "BorrowedBooks", {
        "id": "oop1235",
        "bookId": 1,
        "dueDate": "26/12/2022"
    }
)
list = databaseConnection.retrieve(
    "BorrowedBooks",
    "id",
    "oop1235"
)

print(list)
