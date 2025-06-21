
class VendingMachine:
    """
    A simple vending machine simulator.

    Attributes:
        num_items (int): Number of items in the machine.
        item_price (int): Price of a single item.
    """

    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price

    def status(self):
        return f'{self.num_items} items left in the machine. Each costs {self.item_price}.'

    def buy(self, req_items, money):
        """
        Attempts to buy a number of items with the given amount of money.

        Args:
            req_items (int): Number of items the user wants to buy.
            money (int): Amount of money the user has.

        Returns:
            int: The change to be returned to the user.

        Raises:
            ValueError: If there are not enough items or not enough money.
        """
        total_cost = req_items * self.item_price

        if req_items > self.num_items:
            raise ValueError('Not enough items in the machine.')

        if money < total_cost:
            raise ValueError('Not enough money.')

        self.num_items -= req_items
        return money - total_cost


if __name__ == '__main__':
    num_items, item_coins = map(int, input(
        'Enter initial number of items and its price\n').split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input('How many attempts would you like to have?\n'))
    for _ in range(n):
        num_items, num_coins = map(int, input(
            'How many items would you like to buy and how much money do you have?\n').split())
        try:
            change = machine.buy(num_items, num_coins)
            if change:
                print(f'Payment successful! Change is {change}')
                print(machine.status())
            else:
                print('Payment successful! No change received.')
                print(machine.status())
        except ValueError as e:
            print(f'Error: {e}')
