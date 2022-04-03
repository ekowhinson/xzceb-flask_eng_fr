import unittest
from machinetranslation.translator import english_to_french,french_to_english

class TestEnglishtoFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french(None),None)

class TestFrenchtoEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english(None),None)
        self.assertEqual(french_to_english('Bonjour'),'Hello')

unittest.main()