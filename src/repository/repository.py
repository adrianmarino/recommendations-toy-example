from abc import ABC, abstractmethod
    
class Repository(ABC):
    def __init__(self, client):
        self.__client = client
    
    def __perform(self, records, query_fn): 
        self.__client.bulk_update(records, query_fn)
    
    def upsert(self, records): 
        self.__perform(records, self._upset_query_fn)

    @abstractmethod
    def _upset_query_fn(self, session, entity):
        pass
