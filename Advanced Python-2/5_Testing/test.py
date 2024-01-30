import unittest
import script


class TestMain(unittest.TestCase):

    def setUp(self):  # This function basically runs before every test function
        print('About to test a function!')

    def test_calculation(self):
        test_param = 10
        result = script.calculation(test_param)
        self.assertEqual(result, 20)

    def test_calculation2(self):
        test_param = 'abc'
        result = script.calculation(test_param)
        self.assertIsInstance(result, TypeError)

    def test_calculation3(self):
        test_param = None
        result = script.calculation(test_param)
        self.assertEqual(result, 'Please enter number')

    def test_calculation4(self):
        test_param = ''
        result = script.calculation(test_param)
        self.assertEqual(result, 'Please enter number')

    def tearDown(self):  # This function basically runs after every test function
        print('Cleaning up!')


if __name__ == '__main__':
    unittest.main()

# There are two important functions provided by unittest package
# 1) setUp()
# 2) tearDown()
