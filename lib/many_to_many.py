class Author:
    auth_all = []

    def __init__(self, name=None):
        self.name = name
        Author.auth_all.append(self)

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]


class Book:
    book_all = []

    def __init__(self, title=None):
        self.title=title
        Book.book_all.append(self)

    def set_title(self, title):
        if isinstance(title, str):
            self._title=title
        else:
            raise Exception
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]
    



class Contract:
    all = []

    def __init__ (self, author="def", book="def", date="def", royalties="def"):
        self.author=author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda contract: contract.date)

        
    
    @property
    def author(self):
        return self._author


    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author= author
        else:
            raise Exception
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book= book
        else:
            raise Exception

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception

book = Book("Title")
author = Author("Name")
date = '01/01/2001'
royalties = 40000
contract = Contract(author, book, date, royalties)

author.contracts()