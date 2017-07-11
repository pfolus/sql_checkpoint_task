import unittest
import sys


class TestCheckpointExcersise(unittest.TestCase):
    def setUp(self):
        from address import Address
        from work_address import WorkAddress
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
        from address_book import AddressBook
        self.my_book = AddressBook("friends")
        self.assertEqual("friends", self.my_book.name)

    def test_address_book_add_address(self):
        self.add_addresses_to_book()
        self.assertEqual(2, len(self.my_book.addresses))

    def test_address_book_type_error(self):
        from address_book import AddressBook
        book = AddressBook("Test")
        with self.assertRaises(TypeError, msg="Test dupy się nie powiódł ;("):
            book.add_address("dupa")

    def test_address_book_find_returns_empty(self):
        self.add_addresses_to_book()
        self.assertListEqual([], self.my_book.find("XXX"),  msg="Should return empty list")

    def test_address_book_find_returns_one(self):
        self.add_addresses_to_book()
        expected = []
        expected.append(self.my_book.addresses[0])
        actual = self.my_book.find("Kraków")
        self.assertListEqual(expected, actual)

    def test_address_book_find_returns_many(self):
        self.add_addresses_to_book()
        expected = self.my_book.addresses
        actual = self.my_book.find("ski")
        self.assertListEqual(expected, actual)

    # 2nd part tests

    def test_create_from_csv(self):
        from address_book import AddressBook
        book = AddressBook.create_from_csv("List name", "addresses.csv")
        self.assertIsInstance(book, AddressBook)
        self.assertEqual(4, len(book.addresses))

    # helper methods
    def add_addresses_to_book(self):
        from address_book import AddressBook
        self.my_book = AddressBook("friends")
        self.my_book.add_address(self.address1)
        self.my_book.add_address(self.work1)

if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=False)
