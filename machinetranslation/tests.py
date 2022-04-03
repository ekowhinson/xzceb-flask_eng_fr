import unittest
from translator import englishToFrench,frenchToEnglish

class TestEnglishtoFrench(unittest.TestCase):
    def test(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertNotEqual(englishToFrench(''),'')

class TestFrenchtoEnglish(unittest.TestCase):
    def test(self):
        self.assertEqual(englishToFrench('Bonjour'),'Hello')
        self.assertNotEqual(englishToFrench(''),'')