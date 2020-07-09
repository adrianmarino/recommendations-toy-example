from .json_utils import load_json
from .repository import City, Country, Region, User, Airline, Hotel
from abc import ABC, abstractmethod
    
class Repository(ABC):
    def __init__(self, client): self.__client = client
    def __perform(records, query_fn): self.__client.bulk_update(records, query_fn)
    def upsert(records): self.__perform(records, self._upset_query_fn)
    @abstractmethod    
    def _upset_query_fn(self): pass

def have_fields(entity, fields): 
    return entity != None and all((field in entity) and (entity[field] != None) for field in fields)
    
class Filter(ABC):
    def perform(self, entity):
        try:
            return self._condition(entity)
        except Exception as e:
            raise Exception(f'Filter entity error!. Entity: {entity}. Error: {e}')

    @abstractmethod
    def _condition(self, entity):
        pass

class Mapper(ABC):
    def perform(self, entity):
        try:
            return self._mapping(entity)
        except Exception as e:
            raise Exception(f'Map entity error!. Entity: {entity}. Error: {e}')

    @abstractmethod
    def _mapping(self, entity):
        pass

class CityMapper(Mapper):
    def _mapping(self, entity):
        return City(code=entity['code'], name=entity['name'])

class RegionMapper(Mapper):
    def _mapping(self, entity):
        return Region(code=entity['code'], name=entity['name'])

class HotelMapper(Mapper):
    def _mapping(self, entity):
        return Hotel(id=entity['id'], name=entity['name'])

class AirlineMapper(Mapper):
    def _mapping(self, entity):
        return Airline(code=entity['code'], name=entity['name'])

class UserMapper(Mapper):
    def _mapping(self, entity):
        return User(
            email=entity['email'], 
            realm=entity['realm'], 
            id=entity['id'],
        )
    
class CountryMapper(Mapper):
    def _mapping(self, entity): 
        return Country(code=entity['code'], name=entity['name'])


class EntityLoader:
    @staticmethod
    def load_filter_map(path, entity_filter, entity_mapper): 
        return map(entity_mapper.perform, filter(entity_filter.perform,  load_json(path)))

    @staticmethod
    def load_map(path, entity_mapper): return map(entity_mapper.perform,  load_json(path))

    @staticmethod
    def load(path): return load_json(path)
