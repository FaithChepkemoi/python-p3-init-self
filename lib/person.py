#!/usr/bin/env python3


# lib/person.py

class Person:
    def __init__(self, name):
        """
        Initializes a Person object with a name.

        Args:
            name (str): The person's name.
        """
        self.name = name

    # Other methods (e.g., talk, walk) can be added here
    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")
