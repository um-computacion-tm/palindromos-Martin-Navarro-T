import unittest

# Detector de Palindromo recursivo
def palindromer(word):
    word = word.replace(' ','').lower()
    if len(word) < 2:
        return True
    if word[0] == word[-1]:
        return palindromer(word[1:-1])
    else:
        return False

if __name__ == '__main__':
    unittest.main()
