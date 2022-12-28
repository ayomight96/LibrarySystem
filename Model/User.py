import uuid


class User:
    def __init__(
            self,
            userType,
            userName,
            password,
            fullName):
        self.userType = userType
        self.userName = userName
        self.password = password
        self.fullName = fullName
        self.id = uuid.uuid4()
        match userType:
            case 'Staff':
                self.station = 'Department'
            case 'Admin':
                self.station = 'Library'
            case _:
                self.station = 'Class'

    def data(self):
        return {
            'id': str(self.id),
            'fullName': self.fullName,
            'userName': self.userName,
            'password': self.password,
            'userType': self.userType
        }
    
    @staticmethod
    def userDataFromDatabase(data):
        return {
            'id': data[0][0],
            'fullName': data[0][1],
            'userName': data[0][2],
            'password': data[0][3],
            'userType': data[0][4],
            'userStation': data[0][5],
            'fine': data[0][6],
        }
