import unittest
import sys

from address_book import AddressBook
from address import Address
from work_address import WorkAddress

class TestCheckpointExcersise(unittest.TestCase):
    def setUp(self):
        self.address1 = Address("Jan Kowalski", "Kraków", "ul. Daszyńskiego", "15", "31")
        self.work1 = WorkAddress("Adam Adamski", "Warszawa", "ul. Domaniewska", "6", "66", "Mordor sp. z o.o.")

    # Addreses tests

    def test_address_person(self):
        self.assertEqual("Jan Kowalski", self.address1.person)

    def test_work_address_person(self):
        self.assertEqual("Adam Adamski", self.work1.person)

    def test_company(self):
        self.assertEqual("Mordor sp. z o.o.", self.work1.company)

    def test_get_full_address(self):
        self.assertEqual('Jan Kowalski, Kraków, ul. Daszyńskiego 15/31',
                         self.address1.get_full_address())

    def test_get_full_work_address(self):
        self.assertEqual('Adam Adamski, Warszawa, ul. Domaniewska 6/66, Mordor sp. z o.o.',
                         self.work1.get_full_address())

    # AddressBook

    def test_address_book_name(self):
        self.my_book = AddressBook("friends")
        self.assertEqual("friends", self.my_book.name)

    def test_address_book_add_address(self):
        self.add_addresses_to_book()
        self.assertEqual(2, len(self.my_book.addresses))

    def test_print_addresses(self):
        self.add_addresses_to_book()
        expected_string = "1. Jan Kowalski, Kraków, ul. Daszyńskiego 15/31\n" \
                          "2. Adam Adamski, Warszawa, ul. Domaniewska 6/66, Mordor sp. z o.o.\n"
        self.my_book.print_addresses()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, expected_string)

    # 2nd part tests

    def test_create_from_csv(self):
        book = AddressBook.create_from_csv("List name", "addresses.csv")
        self.assertIsInstance(book, AddressBook)
        self.assertEqual(4, len(book.addresses))

    # helper methods
    def add_addresses_to_book(self):
        self.my_book = AddressBook("friends")
        self.my_book.add_address(self.address1)
        self.my_book.add_address(self.work1)

if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=False)
