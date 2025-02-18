#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed=None):
        self._name = None
        self._breed = None
        if name is not None:
            self.name = name
        if breed is not None:
            self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is None:
            return
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        if breed is None:
            return
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
