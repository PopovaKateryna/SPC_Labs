import requests
import json
import csv
import re
import logging
from prettytable import PrettyTable

logging.basicConfig(filename='book_catalog.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

class BookAPIConnector:
    def __init__(self):
        self.base_url = 'https://jsonplaceholder.typicode.com/posts'

    def fetch_books(self):
        try:
            resp = requests.get(self.base_url)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as err:
            logging.error(f"API call error: {err}")
            return []

    def create_book(self, book_info):
        try:
            resp = requests.post(self.base_url, json=book_info)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as err:
            logging.error(f"API call error: {err}")
            return None

class BookCatalog:
    def __init__(self, api_connector):
        self.api_connector = api_connector

    def retrieve_books(self):
        return self.api_connector.fetch_books()

    def insert_book(self, name, writer):
        book_info = {'title': name, 'author': writer}
        return self.api_connector.create_book(book_info)

    def find_book_by_title(self, title):
        all_books = self.retrieve_books()
        return [book for book in all_books if title.lower() in book['title'].lower()]

class FileStorage:
    @staticmethod
    def store_data(data, file_format):
        if file_format == 'json':
            with open('saved_books.json', 'w') as file:
                json.dump(data, file, indent=4)
        elif file_format == 'csv':
            with open('saved_books.csv', 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data)
        elif file_format == 'txt':
            with open('saved_books.txt', 'w') as file:
                file.write(str(data))

class BookLibraryInterface:
    def __init__(self, catalog):
        self.catalog = catalog

    def operate(self):
        while True:
            print("\nChoose an action:")
            print("1. View all books")
            print("2. Add a new book")
            print("3. Look up a book by title")
            print("4. Quit")

            selection = input("Your choice (1-4): ")

            if selection == '1':
                books = self.catalog.retrieve_books()
                if books:
                    book_table = PrettyTable()
                    book_table.field_names = ["ID", "Title", "Author"]
                    for book in books:
                        book_table.add_row([book['id'], book['title'], book.get('author', 'N/A')])
                    print(book_table)

                    store_decision = input("Save these books? (yes/no): ")
                    if store_decision.lower() == 'yes':
                        FileStorage.store_data(book_table.get_string(), 'txt')
                        print("Books stored in saved_books.txt")
                else:
                    print("No books found.")

            elif selection == '2':
                book_title = input("Book title: ")
                book_author = input("Book author: ")
                if self.validate_entry(r'^[A-Za-z0-9\s]+$', book_title) and self.validate_entry(r'^[A-Za-z\s]+$', book_author):
                    new_book = self.catalog.insert_book(book_title, book_author)
                    if new_book:
                        print(f"New book added: {new_book}")
                    else:
                        print("Could not add the book.")
                else:
                    print("Invalid input. Please enter a valid title and author.")

            elif selection == '3':
                search_title = input("Book title to search: ")
                found_books = self.catalog.find_book_by_title(search_title)
                print("Books found:", found_books)

            elif selection == '4':
                print("Exiting the Book Library Interface.")
                break
            else:
                print("Invalid selection. Please choose a number between 1 and 4.")

    @staticmethod
    def validate_entry(pattern, text):
        return bool(re.match(pattern, text))

def start_application():
    api_connector = BookAPIConnector()
    catalog = BookCatalog(api_connector)
    interface = BookLibraryInterface(catalog)
    interface.operate()

if __name__ == '__main__':
    start_application()
