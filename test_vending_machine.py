from vending_machine import VendingMachine
import unittest


class TestVendingMachine(unittest.TestCase):
    def setUp(self):
        self.machine = VendingMachine(10, 5)

    def test_status_after_purchase(self):
        self.machine.buy(1, 5)
        self.assertEqual(self.machine.status(),
                         '9 items left in the machine. Each costs 5.')

    def test_buy(self):
        self.assertEqual(self.machine.buy(2, 15), 5)

    def test_not_enough_items(self):
        with self.assertRaises(ValueError) as error:
            self.machine.buy(15, 200)
        self.assertEqual(str(error.exception),
                         'Not enough items in the machine.')

    def test_not_enough_money(self):
        with self.assertRaises(ValueError) as error:
            self.machine.buy(2, 1)
        self.assertEqual(str(error.exception), 'Not enough money.')

    def test_exact_money(self):
        self.assertEqual(self.machine.buy(2, 10), 0)


if __name__ == '__main__':
    unittest.main()
