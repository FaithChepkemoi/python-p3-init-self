#!/usr/bin/env python3

    # lib/dog.py

class Dog:
    def __init__(self, name, breed="Mutt"):
        """
        Initializes a Dog object with a name and optional breed.

        Args:
            name (str): The dog's name.
            breed (str, optional): The dog's breed. Defaults to "Mutt".
        """
        self.name = name
        self.breed = breed

    # Other methods (e.g., bark, sit) can be added here
    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")
