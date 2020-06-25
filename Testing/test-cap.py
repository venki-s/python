import unittest
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEquals(result, 'Python')

    def test_two_words(self):
        text = 'james bond'
        result = cap.cap_text(text)
        self.assertEquals(result, 'James bond')

    def test_two_words_fail(self):
        text = ''
        result = cap.cap_text(text)
        self.assertRaises(result)



if __name__ == '__main__':
    unittest.main()


