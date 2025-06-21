# Vending Machine Simulator

A simple vending machine simulator written in Python.  
Allows setting the initial number of items and item price, then simulates purchasing items from the machine.

---

## Features

- Set initial number of items and price per item  
- Purchase a specified number of items with given money  
- Check machine status (items left and price)  
- Handles errors for:  
  - Not enough items in the machine  
  - Insufficient money  

---

## How to run

1. Make sure you have Python 3.6+ installed.  
2. Clone the repository:  
   
   bash
   git clone https://github.com/YourUsername/your-repo.git
   cd your-repo
   
3. Run the program:
   python vending_machine.py

4. Follow the on-screen prompts to set the machine and make purchases.

Unit Tests

This project includes unit tests using Python’s built-in unittest module.
To run tests, execute:
  python -m unittest test_vending_machine.py

Project Structure:
  vending_machine.py — main file containing the VendingMachine class and program logic
  test_vending_machine.py — unit tests

Example usage:

Enter initial number of items and its price
10 5
How many attempts would you like to have?
2
How many items would you like to buy and how much money do you have?
3 20
Payment successful! Change is 5
7 items left in the machine. Each costs 5.
How many items would you like to buy and how much money do you have?
8 50
Error: Not enough items in the machine.

Author

NoobCoder12  
https://github.com/NoobCoder12

License

This project is licensed under the MIT License — feel free to use and modify it.
