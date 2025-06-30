

from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int
    genre: str
    pages: int

book1 = Book(
    title="1984",
    author="George Orwell",
    year=1949,
    genre="Dystopian",
    pages=328
)

print(book1)
print(f"{book1.title} foi escrito por {book1.author} em {book1.year}.")