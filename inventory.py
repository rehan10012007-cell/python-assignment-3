import json
from pathlib import Path
import logging
from .book import Book

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

class LibraryInventory:
    def __init__(self, file_path="catalog.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load()

    def load(self):
        try:
            if self.file_path.exists():
                text = self.file_path.read_text(encoding="utf-8")
                if text.strip():
                    data = json.loads(text)
                    for item in data:
                        book = Book(
                            item.get("title", ""),
                            item.get("author", ""),
                            item.get("isbn", ""),
                            item.get("status", "available")
                        )
                        self.books.append(book)
            logging.info("Catalog loaded")
        except Exception as e:
            logging.error(f"Error loading catalog: {e}")

    def save(self):
        try:
            data = [book.to_dict() for book in self.books]
            self.file_path.write_text(json.dumps(data, indent=4), encoding="utf-8")
            logging.info("Catalog saved")
        except Exception as e:
            logging.error(f"Error saving catalog: {e}")

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        self.save()
        logging.info(f"Book added: {title} ({isbn})")

    def search_by_title(self, title):
        result = []
        for book in self.books:
            if title.lower() in book.title.lower():
                result.append(book)
        return result

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        return self.books
