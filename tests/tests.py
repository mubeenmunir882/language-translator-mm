import unittest

from translator import englishtofrench, englishtogerman

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtofrench("hello"),"bonjour")
        self.assertEqual(englishtofrench("welcome"),"bienvenue")
        self.assertEqual(englishtofrench("love"),"Amour")

class TestEnglishToGerman(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtogerman("hello"),"Hallo")
        self.assertEqual(englishtogerman("welcome"),"Begrüßung")
        self.assertEqual(englishtogerman("love"),"Liebe")

unittest.main()