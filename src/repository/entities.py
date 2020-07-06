from collections import namedtuple

City = namedtuple('City', 'id iata_code name')
Country = namedtuple('Country', 'id code name')
Region = namedtuple('Region', 'code name')
User = namedtuple('User', 'id email realm')
