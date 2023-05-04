#!/usr/bin/env python3
import ipdb

class Shoe:
    def __init__(self, brand):
        self.brand = brand



    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")     

    def get_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")
            self._size = None

    def set_size(self):
        return self._size
        
    size = property(set_size, get_size)