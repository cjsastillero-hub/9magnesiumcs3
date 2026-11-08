# SG 9: Inheritance
## Name: Christine Joyce S. Astillero
## Section: 9 - Magnesium
## Date : 11/8/2026
## School Year: 2026-2027

class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def set_title(self, title):
        self.__title = title
    def set_author(self, author):
        self.__author = author
    def display_info(self):
        print(f"Publication: {self.title}")
        print(f"Author: {self.author}")

class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = number_of_pages

    @property
    def number_of_pages(self):
        return self.__number_of_pages

    def get_number_of_pages(self):
        print(f"Number of Pages: {self.number_of_pages}")
    def set_number_of_pages(self, number_of_pages):
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("Im sorry! The number of pages must be greater than 0!")

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = issue_number

    @property
    def issue_number(self):
        return self.__issue_number

    def get_issue_number(self):
        print(f"Issue Number: {self.issue_number}")
    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("Im sorry! The issue number must be a positive integer!")

pub1 = Publication("The Greatest Showman", "Hugh Jackman")
pub2 = Publication("Epic The Musical", "Jorge Rivera-Herrans")
book1 = Book("Caraval", "Stephani Garber", 448)
book2 = Book("Legendborn", "Tracy Deonn", 512)
mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Vogue", "Various Authors", 203)

print("Publication Information 1:")
pub1.display_info()
print("\nPublication Information 2:")
pub2.display_info()

print("\nBook Information 1:")
book1.set_number_of_pages(-448)
book1.display_info()
print(book1.get_number_of_pages())
print("\nBook Information 2:")
book2.set_number_of_pages(-512)
book2.display_info()
print(book2.get_number_of_pages())

print("\nMagazine Information 1:")
mag1.display_info()
print(mag1.get_issue_number())
print("\nMagazine Information 2:")
mag2.display_info()
print(mag2.get_issue_number())
