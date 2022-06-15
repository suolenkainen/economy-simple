#!/usr/bin/env python

"""test-resource.py: Contains tests for resource.py file."""

__author__      = "Pekka 'Suolenkainen' Marjamäki"
__contact__     = "pmarjama@gmail.com"

import unittest
from src.resource import resource_object

class resource_tests(unittest.TestCase):
    def test_check_if_object(self):
        
        result = resource_object()

        # self.assertIs(type(result): object)

print(type(resource_object()))