import csv
import os

def display_menu():
    print("\nMenu:")
    print("1. Add a New Book")
    print("2. Update a Book")
    print("3. Delete a Book")
    print("4. Search for Books")
    print("5. Display All Books")
    print("6. Exit")

def display_books_from_csv():
    with open('BookRegistry.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\tBook ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Number of Pages: {row[3]}, Publishing Date: {row[4]}, Series: {row[5]}, Genre: {row[6]}')
                line_count += 1
        print(f'Processed {line_count - 1} books.')

def add_new_book():
    book_id = input("Enter book ID to update: ")
    field_to_update = input("Enter field to update (Title/Author/Number of pages/Publishing Date/Series/Genre): ").capitalize()
    new_value = input(f"Enter new {field_to_update}: ")
    pass

def update_book():
    book_id = input("Enter book ID to update: ")

    with open('BookRegistry.csv', 'r', newline='') as file:
        csv_reader = csv.reader(file)
        books = list(csv_reader)
        updated = False

        for book in books:
            if book[0] == book_id:
                field_to_update = input("Enter field to update (Title/Author/Number of pages/Publishing Date/Series/Genre): ").capitalize()
                new_value = input(f"Enter new {field_to_update}: ")

                field_indices = {"Title": 1, "Author": 2, "Number of pages": 3, "Publishing Date": 4, "Series": 5, "Genre": 6}

                if field_to_update in field_indices:
                    book[field_indices[field_to_update]] = new_value
                    updated = True

        if updated:
            with open('BookRegistry.csv', 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(books)
                print(f"Book ID {book_id} updated successfully.")
        else:
            print(f"Book ID {book_id} not found.")

def delete_book():
    book_id = input("Enter book ID to delete: ")

    with open('BookRegistry.csv', 'r', newline='') as file:
        csv_reader = csv.reader(file)
        books = list(csv_reader)
        new_books = [book for book in books if book[0] != book_id]

    with open('BookRegistry.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(new_books)
        print(f"Book ID {book_id} deleted successfully.")
    pass

def search_books():
    valid_criteria = ["ID", "Title", "Author", "Number of pages", "Publishing Date", "Series", "Genre"]
    search_criteria = input("Enter search criteria (ID/Title/Author/Number of pages/Publishing Date/Series/Genre): ").capitalize()

    if search_criteria not in valid_criteria:
        print("Invalid criteria. Please enter a valid option.")
        return

    search_value = input(f"Enter {search_criteria} to search for: ")

    with open('BookRegistry.csv', 'r', newline='') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        matched_books = [book for book in csv_reader if search_value.lower() in book[valid_criteria.index(search_criteria)].lower()]

        if matched_books:
            print(f"Matching books based on {search_criteria} ({search_value}):")
            for book in matched_books:
                print(f"Book ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Number of Pages: {book[3]}, Publishing Date: {book[4]}, Series: {book[5]}, Genre: {book[6]}")
        else:
            print(f"No books found based on {search_criteria} ({search_value}).")

if not os.path.isfile('BookRegistry.csv'):
    with open('BookRegistry.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Author", "Number of pages", "Publishing Date", "Series", "Genre"])
        writer.writerow(["1", "Red Queen", "Victoria Aveyard", "469", "2015-02-10", "Red Queen Series", "Fantasy"])
        writer.writerow(["2", "Glass Sword", "Victoria Aveyard", "544", "2016-02-04", "Red Queen Series", "Fantasy"])
        writer.writerow(["3", "King's Cage", "Victoria Aveyard", "594", "2017-02-07", "Red Queen Series", "Fantasy"])
        writer.writerow(["4", "War Storm", "Victoria Aveyard", "772", "2018-05-15", "Red Queen Series", "Fantasy"])
        writer.writerow(["5", "The Knife of Never Letting Go", "Patrick Ness", "479", "2008-05-05", "Chaos Walking", "Sci-Fi"])
        writer.writerow(["6", "The Ask and The Answer", "Patrick Ness", "506", "2009-05-04", "Chaos Walking", "Sci-Fi"])

    pass

while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_new_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        search_books()
    elif choice == "5":
        display_books_from_csv()
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")


