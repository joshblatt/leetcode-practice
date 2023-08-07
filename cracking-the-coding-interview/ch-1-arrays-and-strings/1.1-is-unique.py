import unittest

# Implement an algorithm to determine if a string has all unique characters
def is_characters_unique(string: str):
    characters = dict()
    for c in string:
        if not characters.get(c):
            characters[c] = True
        else:
            return False
    return True

# What if you cannot use additional data structures?
def is_characters_unique_no_data_structure(string: str):
    characters = [False for _ in range(128)] #128 ascii characters
    for c in string:
        val = ord(c)
        if characters[val]:
            return False
        else:
            characters[val] = True
    return True

class Test(unittest.TestCase):
    data_true = ['yes', 'no', '', 'qwertyuiop']
    data_false = ['hello', 'yessir']

    def test_is_characters_unique(self):
        for test_string in self.data_true:
            result = is_characters_unique(test_string)
            self.assertTrue(result)
        for test_string in self.data_false:
            result = is_characters_unique(test_string)
            self.assertFalse(result)
    
    def test_is_characters_unique_no_data_structure(self):
        for test_string in self.data_true:
            result = is_characters_unique_no_data_structure(test_string)
            self.assertTrue(result)
        for test_string in self.data_false:
            result = is_characters_unique_no_data_structure(test_string)
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()