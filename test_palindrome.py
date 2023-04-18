import unittest
from palindrome import palindrome
from palindrome_recursivo import palindromer

class TestPalindrome(unittest.TestCase):
    def test_palindrome1(self):
        result = palindrome('neuquen')
        self.assertEqual(result, True)

    def test_palindrome2(self):
        result = palindrome('mendoza')
        self.assertEqual(result, False)

    def test_palindrome3(self):
        result = palindrome('radar')
        self.assertEqual(result, True)

    def test_palindrome4(self):
        result = palindrome('no es palindromo')
        self.assertEqual(result, False)

    def test_palindrome5(self):
        result = palindrome('agita falsos usos la fatiga')
        self.assertEqual(result, True)
        
    def test_palindrome6(self):
        result = palindrome('ana')
        self.assertEqual(result, True)

    def test_palindrome7(self):
        result = palindrome('oso')
        self.assertEqual(result, True)
        
    def test_palindrome8(self):
        result = palindrome('somos o no somos')
        self.assertEqual(result, True)

    def test_palindrome9(self):
        result = palindrome('amo la paloma')
       
    def  test_rpalindrome_1(self):
        result = palindromer('neuquen')
        self.assertEqual(result, True)

    def test_rpalindrome_2(self):
        result = palindromer('mendoza')
        self.assertEqual(result, False)

    def test_rpalindrome_3(self):
        result = palindromer('radar')
        self.assertEqual(result, True)

    def test_rpalindrome_4(self):
        result = palindromer('no es palindromo')
        self.assertEqual(result, False)

    def test_rpalindrome_5(self):
        result = palindromer('agita falsos usos la fatiga')
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()

    