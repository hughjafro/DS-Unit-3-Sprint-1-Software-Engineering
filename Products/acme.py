#!/usr/bin/env python
'''
Python module to organize and manage products
'''
import numpy
from numpy import randint


class Product:
    '''
    Class to manage product features
    '''
    def __init__(self, name, price=10, weight=20,
                 flammability=0.5,
                 identifier=randint(1000000, 10000000)):
        self.name = str(name)
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability)
        self.identifier = identifier

    def stealability(self):
        '''
        This function will divide the price by the weight
        and determine if it is too heavy > 50%, then it
        is not very stealable.
        '''
        s = self.price / self.weight

        if s < 0.5:
            return "Not so stealable..."
        elif s >= 0.5 and < 1:
            return "Kinda stealable..."
        else:
            return "Very stealable!"

    def explode(self):
        '''
        calculates the flammability times the weight, and
         then returns a message: if the product is less than
          10 return "...fizzle.", if it is greater or equal
         to 10 but less than 50 return "...boom!", and
         otherwise return "...BABOOM!!
        '''
        x = (self.flammability * self.weight)

        if x < 10:
            return "...fizzle."
        elif x >= 10 and x < 50:
            return "...boom"
        else:
            return "...BABOOM"

    class BoxingGlove(Product):
        '''
        Make a subclass of `Product` named `BoxingGlove` that
         does the following:

        - Change the default `weight` to 10 (but leave other
         defaults unchanged)
        - Override the `explode` method to always
         return "...it's a glove."
        - Add a `punch` method that returns "That tickles."
         if the weight is below 5,
        "Hey that hurt!" if the weight is greater or equal to 5
         but less than 15, and
        "OUCH!" otherwise
        '''

        def __init__(self, name, price=10,
                     weight=10, flammability=0.5,
                     identifier=randint(1000000, 10000000)):
                        super().__init__(name, price, weight,
                                         flammability, identifier)

        def explode(self):
            return "...it's a glove."

        def punch(self):
            if self.weight < 5:
                return "That tickles."
            elif self.weight >= 5 and self.weight < 15:
                return "Hey that hurt!"
            else:
                return "OUCH!"
