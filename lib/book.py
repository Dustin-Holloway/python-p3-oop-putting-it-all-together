#!/usr/bin/env python3
import ipdb

class Book:
    def __init__(self, page_count, title="And Then There Were None",  ):
        self.page_count = page_count
        self.title = title

    def turn_page(self):
        print ("Flipping the page...wow, you read fast!")


    def set_page_count(self, count):
        if isinstance(count, int):
            self._page_count = count
        else:
            print("page_count must be an integer")
            self._page_count = None

    def get_page_count(self):
        return self._page_count
    
    page_count = property(get_page_count, set_page_count)


# mystory = Book(25)
# mystory.turn_page()


