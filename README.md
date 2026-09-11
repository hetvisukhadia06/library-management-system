# library-management-system
# Library Management System

## 1. Project Title

**Library Management System**

---

## 2. Project Objective

The Library Management System is a simple Python-based project used to manage books, members, book pre-booking, borrowing, and returning books.

The main purpose of this project is to make basic library operations easy and organized.

This project is developed using **Core Python** and stores all information in **JSON files**.

The project also demonstrates important Python concepts such as:

* Object-Oriented Programming (OOP)
* Classes and Objects
* Functions
* JSON File Handling
* Exception Handling
* Dictionaries
* Loops and Conditions
* Menu-Driven Programming

---

## 3. Technology Used

**Programming Language:** Python

**Data Storage:** JSON Files

**Concepts Used:**

* OOP
* Classes and Objects
* Functions
* JSON
* File Handling
* Exception Handling
* Conditional Statements
* Loops
* Dictionaries
* Menu System

No external Python libraries are required for this project.

---

## 4. Main Features

The Library Management System provides the following features:

### 1. Add Book

* Add a new book to the library.
* Store book name, author, and book location.
* Each book has a unique book ID.

### 2. Display Books

* Display all books available in the library.
* Show book details such as book ID, name, author, and location.

### 3. Add Member

* Add a new library member.
* Store member name and course.
* Each member has a unique member ID.

### 4. Display Member Details

* Display registered library members.
* Show member ID, name, and course.

### 5. Pre-Booking of Books

* Members can pre-book a book.
* Store member ID, member name, book ID, and booking date.
* This helps members reserve a book before borrowing it.

### 6. Borrow Book

* A member can borrow a book.
* Store borrowing information.
* Store borrow date and return date.
* Book status is maintained in the system.

### 7. Return Book

* Members can return borrowed books.
* The system updates the book borrowing information.

### 8. Exit

* Exit the Library Management System safely.

---

## 5. Menu System

The application uses a simple menu-driven system.

```text
===== Library Management System =====

1. Add Book
2. Display Books
3. Add Member
4. Display Member Details
5. Add Your Pre Booking OF Books
6. Borrow Book
7. Return Book
8. Exit
```

The user selects an option and the related function is called.

---

## 6. Project Structure

The project contains Python files and JSON files for storing data.

```text
Library Management System/
│
├── main.py
├── data.py
│
├── books.json
├── member.json
├── borrow_book.json
└── pre_register_book.json
```

---

## 7. JSON Data Files

The project uses JSON files to store data permanently.

### books.json

This file stores book information.

Example:

```json
{
    "102": {
        "name": "python",
        "book_author": "jignesh patel",
        "book_location": "row 16"
    }
}
```

It stores:

* Book ID
* Book Name
* Book Author
* Book Location

---

### member.json

This file stores library member information.

Example:

```json
{
    "1": {
        "member_name": "hetvi sukhadia",
        "member_course": "bca"
    }
}
```

It stores:

* Member ID
* Member Name
* Member Course

---

### borrow_book.json

This file stores borrowed book information.

Example:

```json
{
    "121": {
        "book_id": "121",
        "member_id": "23",
        "borrow_date": "2026-09-08",
        "return_date": "2026-09-15",
        "status": "borrowed",
        "book_data": {
            "name": "react development",
            "book_author": "yash shah",
            "book_location": "row 30"
        }
    }
}
```

It stores:

* Book ID
* Member ID
* Borrow Date
* Return Date
* Book Status
* Book Details

---

### pre_register_book.json

This file stores pre-booking information.

Example:

```json
{
    "101": {
        "book_id": "101",
        "member_id": "1",
        "member_name": "hetvi sukhadia",
        "booking_date": "2026-08-02"
    }
}
```

It stores:

* Book ID
* Member ID
* Member Name
* Booking Date

---

## 8. OOP Concepts Used

Object-Oriented Programming is used to organize the project.

The project uses **classes and objects** to manage library operations.

Different library functions are written inside classes, and objects are used to call these functions.

For example, the `Data` class is used to manage JSON data.

```python
class Data:

    def __init__(self):
        self.books = {}
        self.member = {}
        self.book_borrow = {}
        self.pre_register = {}
```

The class stores the library data in different dictionaries.

The application then uses objects to access the class functions.

This makes the code more organized and reusable.

---

## 9. Data Class

The `data.py` file contains the `Data` class.

The main responsibility of this class is to handle JSON data.

It contains functions for loading and saving different JSON files.

### Loading Functions

The following functions load data from JSON files:

```text
load_books()
load_members()
load_borrow_books()
load_pre_register_book()
```

These functions read JSON files and store the data in Python dictionaries.

### Saving Functions

The following functions save data into JSON files:

```text
save_books()
save_members()
save_borrow_books()
save_pre_register()
```

These functions use `json.dump()` to permanently save the data.

---

## 10. JSON File Handling

The project uses Python's built-in `json` module.

The `json.load()` function is used to read data from JSON files.

Example:

```python
with open("books.json", "r") as file:
    self.books = json.load(file)
```

The `json.dump()` function is used to save data into JSON files.

Example:

```python
with open("books.json", "w") as file:
    json.dump(self.books, file, indent=4)
```

This allows the application to keep data even after the program is closed.

---

## 11. Exception Handling

Exception handling is used to prevent the program from crashing when an error occurs.

The project uses `try-except` blocks while loading and saving JSON files.

Example:

```python
try:
    with open("books.json", "r") as file:
        self.books = json.load(file)

except Exception as e:
    print("Error while loading books:", e)
    self.books = {}
```

If the file is missing, empty, or contains an invalid format, the program handles the error and continues safely.

Exception handling is also used while saving data.

This makes the application more reliable.

---

## 12. Functions

The project uses separate functions for different operations.

Examples:

* Add Book
* Display Books
* Add Member
* Display Member Details
* Pre-Book Book
* Borrow Book
* Return Book
* Load JSON Data
* Save JSON Data

Using functions makes the code easier to understand, maintain, and reuse.

---

## 13. Program Flow

The basic working flow of the application is:

```text
Start
  |
  v
Display Main Menu
  |
  v
Select Option
  |
  +---- Add Book
  |
  +---- Display Books
  |
  +---- Add Member
  |
  +---- Display Member
  |
  +---- Pre-Book Book
  |
  +---- Borrow Book
  |
  +---- Return Book
  |
  +---- Exit
  |
  v
Save Data in JSON
  |
  v
Exit
```

---

## 14. Error Handling and Validation

The system handles common errors using exception handling.

Examples:

* File not found
* Invalid JSON data
* Error while reading a file
* Error while saving a file
* Invalid user input
* Invalid book or member information

Clear error messages are displayed to the user when an error occurs.

---

## 15. Benefits of the Project

* Simple and easy-to-use menu system
* Easy book management
* Easy member management
* Book pre-booking facility
* Borrow and return functionality
* Permanent data storage using JSON
* Uses OOP concepts
* Uses functions and modular programming
* Uses exception handling
* Easy to understand for Python beginners
* No external libraries required

---

## 16. How to Run the Project

### Step 1

Install Python on your computer.

### Step 2

Download or clone this project from GitHub.

### Step 3

Open the project folder in VS Code.

### Step 4

Open the terminal in the project folder.

### Step 5

Run the main Python file:

```bash
python main.py
```

The Library Management System menu will be displayed.

---

## 17. Core Python Concepts Demonstrated

This project demonstrates the following Core Python concepts:

* Variables
* Strings
* Integers
* Dictionaries
* Lists
* Functions
* Classes
* Objects
* OOP
* Constructors
* JSON
* File Handling
* `try-except`
* Loops
* Conditional Statements
* User Input
* Menu-Driven Programming
* Data Storage

---

## 18. Project Conclusion

The Library Management System is a simple and practical Python project that manages basic library operations.

It allows users to add and display books, manage members, pre-book books, borrow books, and return books.

The project demonstrates how **OOP, functions, JSON file handling, exception handling, and menu-driven programming** can be combined to create a useful real-world application.

The project is simple, organized, and can be extended in the future with features such as fine calculation, librarian login, book search, book availability checking, and more detailed reports.

---

## 19. Author

**Developed as a Core Python Project**

**Project:** Library Management System
