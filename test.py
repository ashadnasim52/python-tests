import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print('About to run a function')

    def test_do_stuff(self):
        test_param = 10
        result = main.funcname(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'hello'
        result = main.funcname(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.funcname(test_param)
        self.assertEqual(result, 'Please enter any number')

    def test_do_stuff3(self):
        test_param = ''
        result = main.funcname(test_param)
        self.assertEqual(result, 'Please enter any number')

    def tearDown(self):
        print('Cleaingin up')


if __name__ == '__main__':
    unittest.main()
