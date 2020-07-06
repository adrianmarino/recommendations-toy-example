from .repository import Repository

class CountryRepository(Repository):
    def _upset_query_fn(self, session, entity):
        session.run("MERGE (c:Country {_id: $id}) ON CREATE SET c.code = $code, c.name = $name", 
                    id=entity.id, code=entity.code, name=entity.name)