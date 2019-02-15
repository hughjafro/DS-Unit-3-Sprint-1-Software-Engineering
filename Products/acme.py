#!/usr/bin/env python
'''
Python module to organize and manage products
'''


class Product:
    '''
    Class to manage product features
    '''
    def __init__(self, name, price:int, weight:int, flammability:float,
                 identifier:int):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier


    