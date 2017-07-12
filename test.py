import unittest
import sys
import os

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

    def test_address_eq(self):
        from address import Address
        first = Address("Jan Kowalski", "Kraków", "ul. Daszyńskiego", "15", "31")
        second = Address("Jan Kowalski", "Kraków", "ul. Daszyńskiego", "15", "31")
        self.assertEqual(first, second)

    def test_address_not_eq(self):
        from address import Address
        first = Address("Jan Kowalski", "Kraków", "ul. Daszyńskiego", "15", "31")
        second = Address("Jan Kowalski", "Kraków", "ul. Daszyńskiego", "16", "31")
        self.assertNotEqual(first, second)

    def test_work_address_eq(self):
        from work_address import WorkAddress
        first = WorkAddress("Adam Adamski", "Warszawa", "ul. Domaniewska", "6", "66", "Mordor sp. z o.o.")
        second = WorkAddress("Adam Adamski", "Warszawa", "ul. Domaniewska", "6", "66", "Mordor sp. z o.o.")
        self.assertEqual(first, second)

    def test_work_address_not_eq(self):
        from work_address import WorkAddress
        first = WorkAddress("Adam Adamski", "Warszawa", "ul. Domaniewska", "6", "66", "Mordor sp. z o.o.")
        second = WorkAddress("Adam Adamski", "Warszawa", "ul. Domaniewska", "6", "66", "Hobbit sp. z o.o.")
        self.assertNotEqual(first, second)

    def test_work_and_address_not_eq(self):
        from address import Address
        from work_address import WorkAddress
        first = Address("Adam Adamski", "Warszawa", "ul. Domaniewska", "6", "66")
        second = WorkAddress("Adam Adamski", "Warszawa", "ul. Domaniewska", "6", "66", "Hobbit sp. z o.o.")
        self.assertNotEqual(first, second)

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

    def test_create_from_csv_length(self):
        from address_book import AddressBook
        book = AddressBook.create_from_csv("book_name", "addresses.csv")
        self.assertIsInstance(book, AddressBook)
        self.assertEqual(5, len(book.addresses))

    def test_create_from_csv_name(self):
        from address_book import AddressBook
        book_name = "book_name"
        book = AddressBook.create_from_csv("book_name", "addresses.csv")
        self.assertEqual("book_name", book.name)

    def test_create_from_csv_addresses(self):
        from address_book import AddressBook
        expected = self.create_address_list()
        book = AddressBook.create_from_csv("book_name", "addresses.csv")
        actual = book.addresses
        self.assertListEqual(expected, actual)

    def test_save_to_csv(self):
        from address_book import AddressBook
        book_name = "book_name"
        book = AddressBook.create_from_csv("book_name", "addresses.csv")

        # remove old file so that we have a guarantee that a file is generated
        try:
            os.remove(book.name + ".csv")
        except:
            pass

        book.save_to_csv()

        with open("addresses.csv") as original, open(book.name + ".csv") as copy:
            are_equal = original.readlines() == copy.readlines()

        self.assertTrue(are_equal, msg="Loaded and saved files are not equal")

    # helper methods
    def add_addresses_to_book(self):
        from address_book import AddressBook
        self.my_book = AddressBook("friends")
        self.my_book.add_address(self.address1)
        self.my_book.add_address(self.work1)

    def create_address_list(self):
        from address_book import AddressBook
        from address import Address
        from work_address import WorkAddress

        expected = []
        expected.append(Address("Jane Weaver", "Tugusirna", "Rowland", "1877", "2"))
        expected.append(Address("Rebecca Cunningham", "Murzuq", "Heffernan", "2", "3"))
        expected.append(Address("Steven Pierce", "Matsena", "Mariners Cove", "153", "4"))
        expected.append(WorkAddress("Jerzy Mardaus", "Kraków", "Ślusarska", "9", "1", "Codecool Poland Sp. z o.o."))
        expected.append(Address("Betty Jenkins", "Tirmiz", "Hollow Ridge", "011", "5"))

        return expected

if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=False)
