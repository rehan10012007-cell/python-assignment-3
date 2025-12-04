from inventory import LibraryInventory

def show_menu():
    print()
    print("Library Inventory Manager")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

def main():
    inventory = LibraryInventory()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter title: ").strip()
            author = input("Enter author: ").strip()
            isbn = input("Enter ISBN: ").strip()
            if title and author and isbn:
                inventory.add_book(title, author, isbn)
                print("Book added successfully.")
            else:
                print("All fields are required.")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ").strip()
            book = inventory.search_by_isbn(isbn)
            if book:
                if book.issue():
                    inventory.save()
                    print("Book issued.")
                else:
                    print("Book is already issued.")
            else:
                print("Book not found.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ").strip()
            book = inventory.search_by_isbn(isbn)
            if book:
                if book.return_book():
                    inventory.save()
                    print("Book returned.")
                else:
                    print("Book is not issued.")
            else:
                print("Book not found.")

        elif choice == "4":
            books = inventory.display_all()
            if books:
                for book in books:
                    print(book)
            else:
                print("No books in inventory.")

        elif choice == "5":
            mode = input("Search by (1) Title or (2) ISBN: ").strip()
            if mode == "1":
                query = input("Enter title or part of title: ").strip()
                result = inventory.search_by_title(query)
                if result:
                    for book in result:
                        print(book)
                else:
                    print("No books found.")
            elif mode == "2":
                isbn = input("Enter ISBN: ").strip()
                book = inventory.search_by_isbn(isbn)
                if book:
                    print(book)
                else:
                    print("No book found with that ISBN.")
            else:
                print("Invalid option.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose between 1 and 6.")

if __name__ == "__main__":
    main()
