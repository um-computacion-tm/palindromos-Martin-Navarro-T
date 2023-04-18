import unittest

# Detector de Palindromo Común
def palindrome (word):
    descendiente = len(word) - 1
    ascendiente = 0
    palindromo = True
    for letra in word:
       if word[ascendiente].lower() != word[descendiente].lower():
           palindromo = False 
       descendiente -= 1
       ascendiente += 1
       return palindromo 

if __name__ == '__main__':
    unittest.main()
