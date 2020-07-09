from .repository import Repository

class CityRepository(Repository):
    def _upset_query_fn(self, session, entity):
        session.run("MERGE (c:City {code: $code}) ON CREATE SET c.name = $name", 
            code=entity.code, name=entity.name)
