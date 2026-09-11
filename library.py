from datetime import date,datetime,timedelta
import traceback
from data import Data


class library:

    def __init__(self):
        try:
            self.message = "Hello, Welcome to the library."

            self.data = Data() 
            self.books = self.data.books
            self.member = self.data.member
            self.borrow = self.data.book_borrow
            self.pre_register = self.data.pre_register

        except Exception as e:
            print("Error while starting library:", e)

            self.books = {}
            self.member = {}
            self.borrow = {}
            self.pre_register = {}


    def welcome_message(self):
        try:
            print(self.message)

        except Exception as e:
            print("Error:", e)


    def add_books(self, book_id, name, book_author, book_location):
        try:
            #ensure that the old data will come first
            self.data.load_books()
            self.books=self.data.books

            self.books[str(book_id)] = {
                "name": name,
                "book_author": book_author,
                "book_location": book_location
            }

            #save the data
            self.data.books = self.books
            self.data.save_books()

            print("Book added successfully.")

        except Exception as e:
            print("Error while adding book:", e)


    def display_data(self):
        try:
            for book_id, book in self.books.items():

                print("Book ID:", book_id)
                print("Book Name:", book["name"])
                print("Author:", book["book_author"])
                print("Location:", book["book_location"])
                print("----------------------")

        except KeyError as e:
            print("Book data is missing:", e)

        except Exception as e:
            print("Error while displaying books:", e)


    def add_members(self, member_id, member_name, member_course):
        try:
            self.data.load_members()
            self.member=self.data.member

            self.member[str(member_id)] = {
                "member_name": member_name,
                "member_course": member_course
            }

            self.data.member=self.member
            self.data.save_members()

            print("Member added successfully.")

        except Exception as e:
            print("Error while adding member:", e)

    def display_member_data(self):
        try:
            for member_id, mem in self.member.items():

                print("Member ID:", member_id)
                print("Member Name:", mem["member_name"])
                print("Member Course:", mem["member_course"])
                print("----------------------")

        except KeyError as e:
            print("Member data is missing:", e)

        except Exception as e:
            print("Error while displaying members:", e)

    def add_pre_register_book(self,pre_register_id,book_id,member_id,prebook_date):
        try:
            self.data.load_books()              # reload latest books
            self.data.load_members()
            self.data.load_pre_register_book()
            self.books = self.data.books
            self.member = self.data.member
            self.pre_register=self.data.pre_register

            #convert the Book_id and member_id into the string and remove the extra space 
            book_id = str(book_id).strip()
            member_id = str(member_id).strip()


            #check that the book is available or not
            if book_id not in self.books:
                print("Book is not avilable.")
                return
            else:
                print("Book is available")

            #check that the member is authorized member or not
            if member_id  not in self.member:
                print("member is not  avilable.")
                return
            else:
                print("member is available")
                name=self.member[member_id]["member_name"]
                prebook_date = datetime.strptime(prebook_date, "%Y-%m-%d").date()

                if prebook_date < date.today():
                    print("Booking date cannot be in the past.")
                    return
                
                #add the data into pre_register_book.json
                self.pre_register[str(pre_register_id)] = {
                    "book_id":book_id,
                    "member_id":member_id,
                    "name":name,
                    "booking_date":str(prebook_date)
                    }

                #save the data in the pre_registration_book.json
                self.data.pre_register=self.pre_register
                self.data.save_pre_register()
                            

        except Exception:
                traceback.print_exc()

    def borrow_book(self,book_id,member_id):

        try:
            self.data.load_books()              # reload latest books
            self.data.load_members()
            self.data.load_borrow_books()

            self.books = self.data.books
            self.member = self.data.member
            self.borrow=self.data.book_borrow
            #convert the Book_id and member_id into the string and remove the extra space 
            book_id = str(book_id).strip()
            member_id = str(member_id).strip()


            #check that the book is available or not
            if book_id not in self.books:
                print("Book is not avilable.")
                return
            else:
                print("Book is available")

            #check that the member is authorized member or not
            if member_id  not in self.member:
                print("member is not  avilable.")
                return
            else:
                print("member is available")

            borrow_date=date.today() # Get today's date

            status="borrowed" # Default status of borrowed book

            #check that the book is pre Register or not
            self.data.load_pre_register_book()
            self.pre_register=self.data.pre_register

            if book_id in self.pre_register:
                print("\nbook is already pre booked")
                booking_date=self.pre_register[book_id]["booking_date"]
                booking_date=datetime.strptime(booking_date,"%Y-%m-%d").date()
                remaining_days=(booking_date-borrow_date).days
                if remaining_days <= 0:
                    print("Book is already reserved for another member.")
                    return
                else:
                    return_date=booking_date
                    print(f"Book is pre_booked after {remaining_days} days")
                    print(f"YOu can borrow the book {remaining_days} days")

            else:
                print("book is not pre booked")

                return_date=borrow_date + timedelta(days=7) #If book is not pre-booked, give it for normal 7 days
                   
            #borrow data
            self.borrow[book_id]={
                "book_id":book_id,
                "member_id":member_id,
                "borrow_date":str(borrow_date),
                "return_date":str(return_date),
                "status":status,
                "book_data":self.books[book_id]
            }

            self.books.pop(book_id)             # remove from available
            self.data.book_borrow = self.borrow
            self.data.save_borrow_books()
            self.data.books = self.books
            self.data.save_books()
            
            print("borrow book data added successfully.")
            print("Borrow Date:", borrow_date)
            print("Return Date:", return_date)


        except Exception as e:
            print("Error while borrowing books",e)


    def return_book(self,book_id,member_id):
        try:
                        #load the json data
                        self.data.load_books()
                        self.data.load_members()
                        self.data.load_borrow_books()
                        self.books=self.data.books
                        self.member=self.data.member
                        self.borrow=self.data.book_borrow

            #convert the Book_id and member_id into the string and remove the extra space 
                        book_id = str(book_id).strip()
                        member_id = str(member_id).strip()

            #firstly reload the json file and store data in variable

                        #check that the book is available or not
                        if book_id not in self.borrow:
                            print("Book is not avilable.")
                            return
                        else:
                            print("Book is available")

                        #check that the member is authorized member or not
                        if member_id  not in self.member:
                            print("member is not  avilable.")
                            return
                        else:
                            print("member is available")

                        if self.borrow[book_id]["member_id"] != member_id:
                            print("Book borrowed by this member.")
                            return

                        # Get return date from borrowed book data
                        return_date = self.borrow[book_id]["return_date"]

                        # Convert string return date into date object
                        return_date = datetime.strptime(return_date,"%Y-%m-%d").date()

                        #caluclate last days
                        last_day=(date.today()-return_date).days

                        #caluclate fine
                        if last_day > 0:
                            fine= last_day * 10
                            print("Late Days:", last_day)
                            print("Fine: ₹", fine)
                                
                        else:
                            fine=0
                            print("Fine:₹0")
                        
                        #for get book details
                        book_details=self.borrow[book_id]["book_data"]
                        self.books[book_id]=book_details
                        self.data.books=self.books
                        self.data.save_books()

                        #add data into the books.json
                        self.borrow.pop(book_id)
                        self.data.book_borrow=self.borrow
                        self.data.save_borrow_books()


                        print("Book returned sucessfully")

        except Exception as e:
            print("Error while borrowing books",e)
    