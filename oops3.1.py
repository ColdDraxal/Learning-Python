class Book:

    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    @staticmethod
    def check(string):
        return "Yes" if 1970>string else "No"

    def info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nClassic: {Book.check(self.year)}"

book1 = Book("1984", "George Orwell", 1949)
book2 = Book("The Hunger Games", "Suzanne Collins", 2008)

print(book2.info())