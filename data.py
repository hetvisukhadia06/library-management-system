import json


class Data:

    def __init__(self):
        try:
            self.message = "Hello, Welcome to the library."

      

        # Get JSON data from Data class
            self.books = {}
            self.member = {}
            self.book_borrow = {}
            self.pre_register = {}

            self.load_books()
            self.load_members()
            self.load_borrow_books()
            self.load_pre_register_book()
            

        except Exception as e:
            print("Error while starting library:", e)

    def load_books(self):
        try:
            with open("books.json", "r") as file:
                self.books = json.load(file)

        except Exception as e:
            print("Error while loading books:", e)
            self.books = {}


    def load_members(self):
        try:
            with open("member.json", "r") as file:
                self.member = json.load(file)

        except Exception as e:
            print("Error while loading members:", e)
            self.member = {}

    def load_borrow_books(self):
            try:
                with open("borrow_book.json", "r") as file:
                    self.book_borrow = json.load(file)
            except Exception as e:
                print("Error while loading members:", e)
                self.book_borrow = {}

    def load_pre_register_book(self):
                try:
                    with open("pre_register_book.json", "r") as file:
                        self.pre_register = json.load(file)
    
        
                except Exception as e:
                    print("Error while loading members:", e)
                    self.pre_register = {}

#save methods

    def save_books(self):
        try:
            with open("books.json", "w") as file:
                json.dump(self.books, file, indent=4)

        except Exception as e:
            print("Error while saving books:", e)


    def save_members(self):
        try:
            with open("member.json", "w") as file:
                json.dump(self.member, file, indent=4)

        except Exception as e:
            print("Error while saving members:", e)


    def save_borrow_books(self):
        try:
            with open("borrow_book.json", "w") as file:
                json.dump(self.book_borrow, file, indent=4)

        except Exception as e:
            print("Error while saving borrowed books:", e)


    def save_pre_register(self):
        try:
            with open("pre_register_book.json", "w") as file:
                json.dump(self.pre_register, file, indent=4)

        except Exception as e:
            print("Error while saving pre-register data:", e)
