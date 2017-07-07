# Address Book in OOP way

## Final result expectation

When your program is done you should be able to do following in Python console.

```python
>>> from address_book import AddressBook
>>> from address import Address
>>> from work_address import WorkAddress

>>> address1 = Address("Jan Kowalski", "Kraków", "ul. Daszyńskiego", "15", "31")
>>> address1.get_full_address()
'Jan Kowalski, Kraków, ul. Daszyńskiego 15/31'

>>> work1 = WorkAddress("Adam Adamski", "Warszawa", "ul. Domaniewska", "6", "66", "Mordor sp. z o.o.")

>>> work1.get_full_address()
'Adam Adamski, Warszawa, ul. Domaniewska 6/66, Mordor sp. z o.o.'

>>> my_book = AddressBook("friends")
>>> my_book.add_address(address1)
>>> my_book.add_address(work1)
>>> my_book.print_addresses()
1. Jan Kowalski, Kraków, ul. Daszyńskiego 15/31
2. Adam Adamski, Warszawa, ul. Domaniewska 6/66, Mordor sp. z o.o.
```

## 1st part

### `Address` class

#### Attributes:

* `person` - string, full name of address owner
* `city` - string, city name
* `street` - string, street name
* `house_no` - string, house number
* `flat_no` - string, flat number

#### Methods

##### `__init__`

Parameters:
* `person` - string, full name of address owner
* `city` - string, city name
* `street` - string, street name
* `house_no` - string, house number
* `flat_no` - string, flat number

##### `get_full_address`

This function should __return__ full address as a string in the following form:
`{owner}, {city}, {street} {house_no}/{flat_no}`

### `WorkAddress` class

#### Attributes:

* `person` - string, full name of address owner
* `city` - string, city name
* `street` - string, street name
* `house_no` - string, house number
* `flat_no` - string, flat number
* `company` - string, name of the company

#### Methods

##### `__init__`

Parameters:
* `person` - string, full name of address owner
* `city` - string, city name
* `street` - string, street name
* `house_no` - string, house number
* `flat_no` - string, flat number
* `company` - string, name of the company

##### `get_full_address`

This function should __return__ full address as a string in the following form:
`{owner}, {city}, {street} {house_no}/{flat_no}, {company}`

### `AddressBook` class

#### Attributes:

* `name` - name of the address book
* `addresses` - list containing addresses (`Address` or `WorkAddress` objects)

#### Methods

##### `__init__`

Parameters:
* `name` - name of the address book

##### `add_address`
Adds given `Address` or `WorkAddress` to the list of addresses

Parameters:
* `address` - `Address` or `WorkAddress` object

##### `print_addresses`

Function should print out all addresses in the address book. Output should look like this:
```
1. Jan Kowalski, Kraków, ul. Daszyńskiego 15/31
2. Adam Adamski, Warszawa, ul. Domaniewska 6/66, Mordor sp. z o.o.
```

##### `find`
Searches through address book for a given phrase and returns a list of matching objects.

Parameters:
* `search_phrase` - string, that we're looking for


# 2nd part
### `create_from_csv`

Create `create_from_csv` static method in `AddressBook` class. It should take
2 parameters:

* `list_name` - name of todo list
* `csv_path` - path to CSV file

This method should return `AddressBook` instance with list of items from
CSV file.

First row in CSV file contains column headers

Have in mind that CSV file could contain both home and work addresses.
