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
    def __init__(self, number_of_pages: int): #Creates constructor method that initializes the number of pages of the book
        self.__number_of_pages = number_of_pages #Private attribute for number of pages
        super().__init__(title, author) #Calls the constructor method of the parent class Publication to initialize the title and author attributes

    def 
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.") 
print(pub1.display_info)