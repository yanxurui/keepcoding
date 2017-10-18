#!/usr/bin/env

"""
>>> in_the_forest(Duck())
Quaaaaaack!
>>> in_the_forest(Person())
The person imitates a duck.
"""

class Duck:
    def quack(self):
        print("Quaaaaaack!")

class Person:
    def quack(self):
        print("The person imitates a duck.")

def in_the_forest(mallard):
    mallard.quack()
