import unittest

class TestStringUtils(unittest.TestCase):
    
    def setUp(self):
        self.utils = StringUtils()

    def test_capitalize(self):
        self.assertEqual(self.utils.capitalize("skypro"), "Skypro")
        self.assertEqual(self.utils.capitalize("hello world"), "Hello world")
        self.assertEqual(self.utils.capitalize(""), "")  # Пустая строка

    def test_trim(self):
        self.assertEqual(self.utils.trim("   skypro"), "skypro")
        self.assertEqual(self.utils.trim("hello"), "hello")  # Без пробелов
        self.assertEqual(self.utils.trim("   "), "")  # Только пробелы
        self.assertEqual(self.utils.trim("  hello  "), "hello  ")  # Пробелы только в начале

    def test_contains(self):
        self.assertTrue(self.utils.contains("SkyPro", "S"))
        self.assertTrue(self.utils.contains("SkyPro", "k"))
        self.assertFalse(self.utils.contains("SkyPro", "U"))
        self.assertFalse(self.utils.contains("", "A"))  # Пустая строка

    def test_delete_symbol(self):
        self.assertEqual(self.utils.delete_symbol("SkyPro", "k"), "SyPro")
        self.assertEqual(self.utils.delete_symbol("SkyPro", "Pro"), "Sky")
        self.assertEqual(self.utils.delete_symbol("SkyPro", "x"), "SkyPro")  # Символ не найден
        self.assertEqual(self.utils.delete_symbol("", "A"), "")  # Пустая строка

if __name__ == "__main__":
    unittest.main()

print ("все")
