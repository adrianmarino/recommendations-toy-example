from .repository import Repository

class CityRepository(Repository):
    def _upset_query_fn(self, session, entity):
        session.run(
            "MERGE (c:City {_id: $id}) ON CREATE SET c.iata_code = $iata_code, c.name = $name", 
            id=entity.id, iata_code=entity.iata_code, name=entity.name)
