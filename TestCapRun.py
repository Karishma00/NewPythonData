#For capitalization Testing

import unittest
import TestCap

class TestCapRun(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = TestCap.caps(text)
        self.assertEqual(result,'Python')

    def test_multiple_word(self):
        text = 'python programming'
        result = TestCap.caps(text)
        self.assertEqual(result,'Python Programming')

if __name__=='__main__':
    unittest.main()



