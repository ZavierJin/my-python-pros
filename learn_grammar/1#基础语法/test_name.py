
import unittest
from learn001 import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('john')
        key = 'john'
        self.assertEqual(formatted_name, key)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
