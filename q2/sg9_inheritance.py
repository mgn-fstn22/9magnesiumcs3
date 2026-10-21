class Publication: #Creates a class called Publication
    def __init__(self, title: str, author: str): #Creates constructor method that initializes the title and author of the publication
        self.__title = title #Private attribute for title
        self.__author = author #Private attribute for author

    @property #makes the function be treated as an attribute
    def get_title(self): #Function that returns the title of the publication
        return self.__title #returns the title of the publication/access the private attribute

    @property #makes the function be treated as an attribute
    def get_author(self): #Function that returns the author of the publication
        return self.__author #returns the author of the publication/access the private attribute

    def set_title(self, title): #creates the function that can access the private attribute title and set it to a new title
        self.__title = title #assigns the new value to the private attribute

    def set_author(self, author): #creates the function that can access the private attribute author and set it to a new author
        self.__author = author #assigns the new value to the private attribute

    @property #makes the function be treated as an attribute
    def display_info(self): #Function that displays the title and author of the publication
        return f"Title: {self.__title}, \nAuthor: {self.__author}" #returns the title and author of the publication

class Book(Publication): #Creates a child class called Book that inherits from the Publication class.
    def __init__(self, title: str, author: str, number_of_pages: int): #Creates constructor method that initializes the number of pages of the book
        self.__number_of_pages = number_of_pages #Private attribute for number of pages and attribute only for this child class Book
        super().__init__(title, author) #Calls the constructor method of the parent class Publication to initialize the title and author attributes

    @property #makes the function be treated as an attribute
    def get_number_of_pages(self): #Function that returns the number of pages of the book
        return self.__number_of_pages #returns/print the number of pages of the book

    def set_number_of_pages(self, number_of_pages): #creates the function that can access the private attribute number_of_pages and set it to a new number of pages
        if number_of_pages > 0: #Checks if the number of pages is greater than 0
            self.__number_of_pages = number_of_pages #assigns the new value to the private attribute

class Magazine(Publication): #Creates a child class called Magazine that inherits from the Publication class.
    def __init__(self, title: str, author: str, issue_number: int): #creates constructor method that initializes the issue number of the magazine and the attributes from parent class
        super().__init__(title, author) #Calls the constructor method of the parent class Publication to initialize the title and author attributes
        self.__issue_number = issue_number #Private attribute for issue number and attribute only for this child class Magazine

    @property #makes the function be treated as an attribute
    def get_issue_number(self): #Function that returns the issue number of the magazine
        return self.__issue_number #returns/print the issue number of the magazine

    def set_issue_number(self, issue_number): #creates a function that accesses the private attribute issue_number and assigns it a new value
        self.__issue_number = issue_number #assigns the new value to the private attribute

pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.") #object for parent class Publication
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310) #object for child class Book
mag1 = Magazine("National Geographic", "Various Authors", 202) #object for child class Magazine

print("----Publication Information----") #prints a string
print(pub1.display_info) #prints the information of the publication using the display_info method of the Publication class

print("\n----Book Information----") #prints a string
book1.set_number_of_pages(-310)  #modifies the number of pages of the book using the set_number_of_pages method of the Book class
print(book1.display_info) #prints the information of the book using the display_info method of the Publication class (inherited by the Book class)
print(f"Number of Pages: {book1.get_number_of_pages}") #prints the number of pages of the book

print("\n----Magazine Information----") #prints a string
print(mag1.display_info) #prints the information of the magazine using the display_info method of the Publication class (inherited by the Magazine class)
print(f"Issue Number: {mag1.get_issue_number}") #prints the issue number of the magazine
