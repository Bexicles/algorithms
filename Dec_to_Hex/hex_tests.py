import unittest
import dec_to_hex as dec


class Hex_Tests(unittest.TestCase):
    def hex_testers(self):
        self.assertEqual('CB9', dec.convert_dec_to_hex(3257))
        self.assertEqual('816E3D', dec.convert_dec_to_hex(8482365))
        self.assertEqual('10', dec.convert_dec_to_hex(16))
        self.assertEqual('0', dec.convert_dec_to_hex(0))
        self.assertEqual('100', dec.convert_dec_to_hex(256))
        self.assertEqual('AAA', dec.convert_dec_to_hex(2730))
