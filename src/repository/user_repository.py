from .repository import Repository

class UserRepository(Repository):
    def _upset_query_fn(self, session, entity):
        session.run(
            "MERGE (c:User {id: $id}) ON CREATE SET c.email = $email, c.realm = $realm ", 
            id=entity.id, email=entity.email, realm=entity.realm)