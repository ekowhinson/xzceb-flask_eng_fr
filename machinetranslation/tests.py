import unittest
from translator import englishToFrench,frenchToEnglish

class TestEnglishtoFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertNotEqual(englishToFrench('Bonjour'),'Hello')