#!/usr/bin/env python

from acme import products
import random


'''
This module will generate random products and
print a summary of them.
'''

adjectives = ['Awesome', 'Shiny', 'Impressive',
              'Portable', 'Improved']
nouns = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def generate_products(N=30):
    '''
    Generate a list of products from random
    '''
    products = []

    for i in range(N):
        product = Product(
            name=random.choice(adjectives) +
            " " + random.choice(nouns)
            price=random.randint(5, 100)
            weight=random.randint(5, 100)
            flammability=random.uniform(0.0, 2.5)
            )
        products.append(product)
    return products


def inventory_reports():
    '''
    This will take a list of products and print a summary
    '''
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT\N")

    total_products = len(products)

    for i in products:
        total_price = += i.price
        total_weight = += i.weight
        total_flamm = += i.flammability

    print("Average price: " + int(total_price/total_products))
    print('\nAverage weight:' + int(total_weight/total_products))
    print('\nAverage flammability:' + float(total_flamm/total_products))

    return

if __name__ == '__main__':
    print(inventory_report(generate_products()))
