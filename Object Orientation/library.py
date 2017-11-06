'''
An example implementation of a libray
'''

class Book:
    ''' A class for creating book objects '''
    
    def __init__(self, author, title):
        '''Initialization method, is called when a book object
        is created.
        '''
        self.author = author
        self.title = title
        # the user who has borrowed the book.
        # points to the user object of that user.
        self.user = None
    
    def is_available(self):
        '''the book is available if no one has borrowed it.'''
        return self.user == None
    
    def borrowed_by(self, user):
        '''assign the book to the user'''
        self.user = user
    
    def returned(self):
        self.user = None
    
    def __str__(self):
        '''
        __str__ is a hook method, called when a string representation
        of a book object is request, e.g. by calling str(bookObject)
        or print(bookObject)
        '''
        s = "\nBOOK:"
        s += "\nTitle: " + self.title
        s += "\nAuthor: " + self.author
        s += "\nAvailable: " + str(self.is_available())
        if not self.user is None:
            s += "\nBorrowed by: " + self.user.username
        return s


class User:
    ''' A class for creating user objects '''    

    def __init__(self, uname, email):
        '''Initialization method, is called when a user object
        is created.
        '''
        self.username = uname
        self.emailaddress = email
        # The list of books that the user has currently borrowed.
        self.borrowed_books = []
    
    def borrow_book(self, book):
        ''' The user on whose user object this method is called
        borrows the book which is given as a parameter. The value
        of this parameter is the book object!
        '''
        self.borrowed_books.append(book)
        book.borrowed_by(self)
    
    def return_book(self, book):
        ''' The user on whose user object this method is called
        returns the book which is given as a parameter. The value
        of this parameter is the book object! '''
        self.borrowed_books.remove(book)
        book.returned()


def create_book():
    '''
    Creates a new book object.
    '''
    title = input("Please enter title:")
    author = input("Please enter author:")
    return Book(author, title)


if __name__ == "__main__":
    book1 = Book("Dickens", "Christmas Carol")
    book2 = Book("Rowling", "Harry Potter")

    books = [book1, book2]

    print("Books right after creating them:")
    for book in books:
        print(book)

    user1 = User("Stefan", "stth@coli.uni-saarland.de")

    user1.borrow_book(book1)

    print("\nAfter Stefan borrowed Christmas Carol:")

    for book in books:
        print(book)

    print("\nBooks borrowed by Stefan:")
    
    for book in user1.borrowed_books:
        print(book.title)

    user1.return_book(book1)

    print("\nAfter Stefan returned Christmas Carol:")

    for book in books:
        print(book)

    ''' Usually, the book / user objects would not be created directly
    as here, but via some function where the user can enter some information
    and the object is returned.
    '''
#    book3 = create_book()
#    books.append(book3)
#    print("A new book created:")
#    print(book3)
