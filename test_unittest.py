import unittest   # The test framework

#test 1
class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(4, 4)

#test 2
class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
            
if __name__ == '__main__':
    unittest.main()