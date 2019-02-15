#!/usr/bin/env python

'''
Test methods for testing reports and products
'''


import unittest
from acme import Product
from acme_report import generate_products, adjectives, nouns


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_product_methods(self):
        prod = Product('Test Product', 10,10,)
        self.assertEqual(prod.stealability(), 'Very Stealable!' )
        self.assertEqual(prod.explode, '...BABOOM',)

if __name__ == '__main__':
    unittest.main()