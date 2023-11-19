#!/usr/bin/python3
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_base_constructor_with_id(self):
        """
        Test the constructor of Base with an explicit ID.
        """
        obj1 = Base(1)
        self.assertEqual(obj1.id, 1)

    def test_base_constructor_without_id(self):
        """
        Test the constructor of Base without an explicit ID.
        """
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_base_id_attribute(self):
        """
        Test the ID attribute of the Base class.
        """
        obj = Base(5)
        self.assertEqual(obj.id, 5)
