import unittest

from atomic_0x_hash import hash_order


class TestHash(unittest.TestCase):
    def test_list_int(self):
        """
        Test hash_order for correct order hash
        """
        result = hash_order(
            '0xf666d1ca49cc8dfd9b63d6476a898dfd5422f7e3',
            '0xcecf0a780419f621301910ea2f8e4fa051833055',
            '0x827606bda249d38aa69aa4aef60f2867289a0bb6',
            '0xf666d1ca49cc8dfd9b63d6476a898dfd5422f7e3',
            999,
            999,
            99,
            99,
            99,
            99,
            '0x231',
            '0x231'
        )
        expected = '0xb5a51eb876321b9abcace4a64c213978212a64bb2c6778c8658edb7087210c8a'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
