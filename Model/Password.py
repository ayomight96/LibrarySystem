import base64


class Password:
    @staticmethod
    def hash(password: str) -> str:
        return base64.b64encode(password)

    @staticmethod
    def unHash(hashedPassword: str) -> str:
        return base64.b64decode(hashedPassword)


password = 'ayomide'
hashedPassword = Password.hash(password)
print (hashedPassword)
print (Password.unHash(hashedPassword))