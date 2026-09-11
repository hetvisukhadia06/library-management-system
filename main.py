from library import library


def main():

    try:
        l = library()
        l.welcome_message()

        while True:

            print("\n===== Library Management System =====")
            print("1. Add Book")
            print("2. Display Books")
            print("3. Add Member")
            print("4. Display Member Details")
            print("5. Add Your Pre Booking OF Books")
            print("6. Borrow Book")
            print("7. Return Book")
            print("8. Exit")

            choice = input("Enter your choice: ")

            print("----------------------")


            if choice == "1":
                #this choice is used to add the books details

                try:
                    book_id = input("Enter a book ID: ")
                    name = input("Enter a book name: ")
                    book_author = input("Enter an author name: ")
                    book_location = input("Enter a book location: ")

                    l.add_books(
                        book_id,
                        name,
                        book_author,
                        book_location
                    )

                except ValueError:
                    print("Book ID must be a number.")

                except Exception as e:
                    print("Error:", e)


            elif choice == "2":
                #this choice is used for the display the books data
                try:
                    l.display_data()

                except Exception as e:
                    print("Error:", e)


            elif choice == "3":
                #this choice is used for the add the member details
                try:
                    member_id = input("Enter your ER No: ")
                    member_name = input("Enter your name: ")
                    member_course = input("Enter your course: ")

                    l.add_members(
                        member_id,
                        member_name,
                        member_course
                    )

                except Exception as e:
                    print("Error:", e)


            elif choice == "4":
                #this choice is used for the display member data
                try:
                    l.display_member_data()

                except Exception as e:
                    print("Error:", e)

            elif choice == "5":
                #this choice is used for pre_register books
                try:
                    pre_register_id=input("ENter Your pre_registration id ID:")
                    book_id=input("ENter Your Book ID:")
                    member_id = input("Enter your ER No: ")
                    prebook_date=input("enter a date that you can pre book your book in (yyyy-MM-DD) formate:")
                    
                    l.add_pre_register_book(
                        pre_register_id,
                        book_id,
                        member_id,
                        prebook_date
                    )
                except Exception as e:
                    print("Error:", e)

            elif choice == "6":
                #this choice is used for the borrow_book
                try:
                    book_id=input("ENter Your Book ID:")
                    member_id = input("Enter your ER No: ")
                    
                    l.borrow_book(
                        book_id,
                        member_id
                    )
                except Exception as e:
                    print("Error:", e)

            elif choice == "7":
                #this choice is used for the borrow_book
                try:
                    book_id=input("ENter Your Book ID:")
                    member_id = input("Enter your ER No: ")
                    
                    l.return_book(
                        book_id,
                        member_id
                    )
                except Exception as e:
                    print("Error:", e)

            elif choice == "8":
                #this this used for print the statement
                print(
                    "Thank you for using the "
                    "Library Management System!"
                )
                break


            else:
                print("Invalid choice. Please try again.")


    except Exception as e:
        print("Program Error:", e)


main()