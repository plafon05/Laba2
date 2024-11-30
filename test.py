import unittest
from file_job import *

class test(unittest.TestCase):
    def test_true(self):
        self.assertTrue(check_tandem_repetition("mama"))
        self.assertTrue(check_tandem_repetition("oo"))
        self.assertTrue(check_tandem_repetition("oo oo oo oop"))

    def test_false(self):
        self.assertFalse(check_tandem_repetition("Danila"))

    def test_probel_false(self):
        self.assertFalse(check_tandem_repetition("  "))
        self.assertFalse(check_tandem_repetition("ma oop"))
        self.assertFalse(check_tandem_repetition(""))