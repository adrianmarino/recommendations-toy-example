from collections import namedtuple

City = namedtuple('City', 'code name')
Country = namedtuple('Country', 'code name')
Region = namedtuple('Region', 'code name')
Airline = namedtuple('Airline', 'code name')
Hotel = namedtuple('Hotel', 'id name')
User = namedtuple('User', 'id email realm')
