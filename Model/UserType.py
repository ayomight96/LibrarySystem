from enum import Enum

class UserType(Enum):
    STUDENT = 'Student'
    STAFF = 'Staff'
    ADMIN = 'Admin'
    
    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_ 

print(UserType.has_value('Staff'))  # True
print(UserType.has_value(7))  # False
print(UserType.STUDENT.value)