from datetime import datetime, timedelta


class Book:
    dueDate = datetime.now()
    lendingDate = datetime.now()
    lendingDuration = 7
    age = 0
    isReserved = False
    feedback = ''
    isBookRequested = False
    isBookAvailable = True

    def __init__(
            self,
            id,
            title,
            authors,
            averageRating,
            isbn,
            isbn13,
            languageCode,
            numberOfPages,
            ratingsCount,
            textReviewsCount,
            publicationDate,
            publisher,
            copy=1,
            copies=1
    ):
        self.id = id
        self.title = title
        self.authors = authors
        self.averageRating = averageRating
        self.isbn = isbn
        self.isbn13 = isbn13
        self.languageCode = languageCode
        self.numberOfPages = numberOfPages
        self.ratingsCount = ratingsCount
        self.textReviewsCount = textReviewsCount
        self.publicationDate = publicationDate
        self.publisher = publisher
        self.copy = copy
        self.copies = copies

    def data(self):
        return {
            'id': self.id,
            'title': self.title,
            'authors': self.authors,
            'averageRating': self.averageRating,
            'isbn': self.isbn,
            'isbn13': self.isbn13,
            'languageCode': self.languageCode,
            'numberOfPages': self.numberOfPages,
            'ratingsCount': self.ratingsCount,
            'textReviewsCount': self.textReviewsCount,
            'publicationDate': self.publicationDate,
            'publisher': self.publisher,
            'copy': self.copy,
            'copies': self.copies,
            'dueDate': self.dueDate.strftime("%Y-%m-%d %H:%M:%S")
        }

    def setLendingDateTest(self, date):
        self.lendingDate = datetime.strptime(date, "%m/%d/%Y")

    def setLendingDate(self):
        self.lendingDate = datetime.now()
        self.dueDate = self.lendingDate + timedelta(days=self.lendingDuration)

    def lendingAge(self):
        dateDifference = datetime.now() - self.lendingDate
        return dateDifference.days

    def showDueDate(self):
        return self.dueDate

    def reservationStatus(self):
        dateDifference = datetime.now() - self.lendingDate
        return dateDifference.days

    def setFeedback(self, feedback: str):
        self.feedback = feedback

    def getFeedback(self):
        return self.feedback

    def toString(self, date: datetime):
        return date.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def renewBookInfo(
            self,
            title,
        authors,
        averageRating,
        isbn,
        isbn13,
        languageCode,
        numberOfPages,
        ratingsCount,
        textReviewsCount,
        publicationDate,
        publisher
    ) -> None:
        self.title = title
        self.authors = authors
        self.averageRating = averageRating
        self.isbn = isbn
        self.isbn13 = isbn13
        self.languageCode = languageCode
        self.numberOfPages = numberOfPages
        self.ratingsCount = ratingsCount
        self.textReviewsCount = textReviewsCount
        self.publicationDate = publicationDate
        self.publisher = publisher
