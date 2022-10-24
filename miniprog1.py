# create a library class
# methods = display books
#             lend books
#             donate(add book)
#             return book

class Library:
    def __init__(self,listofbooks,libraryname):
        self.listofbooks= listofbooks
        self.libraryname= libraryname

    def display_book(self):
        return f"{self.libraryname} have these books- {self.listofbooks}"

    def lend_book(self,lendbook):
        if lendbook in self.listofbooks:
            yourname= input("whats your name?")
            self.lending_dict= {lendbook:yourname}
            self.listofbooks.remove(lendbook)
            return self.lending_dict

        else:
            return f"sorry this book is not in library\n lended books are-{self.lending_dict}"


    def add_book(self,newbook):
        return self.listofbooks.append(newbook)

    def return_book(self,returnedbook):
        if  returnedbook in self.lending_dict.keys():
            del self.lending_dict[returnedbook]
            self.listofbooks.append(returnedbook)
            return self.listofbooks
        else:
            return "this book was never taken...\n to donate book please use add_book function"




vishal_library= Library(["harry potter","got","rings of power"], "vishal_lib")

# if __name__ == '__main__':
#
#     print(vishal_library.listofbooks)
#
#
#     vishal_library.add_book("HCV")
#     print(vishal_library.display_book())
#
#
#     print(vishal_library.lend_book("got"))
#     print(vishal_library.lend_book("got"))
#     print(vishal_library.return_book("got"))
#     vishal_library.add_book("time history")
#     print(vishal_library.display_book())
#     print(vishal_library.lend_book("got"))






