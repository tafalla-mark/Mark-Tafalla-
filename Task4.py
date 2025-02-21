class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear Published: {self.year_published}"

# Create three book objects
book1 = Book("The Hunger Games", "Suzanne Collins", 2008)
book2 = Book("Red Rising", "Pierce Brown", 2014)
book3 = Book("The Sentinel", "Lee Child", 2020)

print(book1.describe())
print("\n" + "-"*30 + "\n")
print(book2.describe())
print("\n" + "-"*30 + "\n")
print(book3.describe())
