import uuid

class User:
    def __init__(
            self,
            userType,
            userName, 
            password, 
            name):
        self.userType = userType
        self.userName = userName
        self.password = password
        self.name = name
        self.id = uuid.uuid4()
        match userType:
            case 'Staff':
                 self.station = 'Department'
            case 'Admin':
               self.station = 'Library'
            case _:
               self.station = 'Class'


user = User('Student', 'Ayo111', '1234567890', 'Ayomide Israel Adekoya')
print (user.id)
print (user.station)

