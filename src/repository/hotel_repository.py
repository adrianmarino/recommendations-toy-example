from .repository import Repository

class HotelRepository(Repository):
    def _upset_query_fn(self, session, entity):
        session.run("MERGE (c:Hotel {_id: $id}) ON CREATE SET c.name = $name", 
                    id=entity.id, name=entity.name)