import pandas as pd
from neo4j import GraphDatabase
from tqdm.notebook import tqdm


def to_table(result, columns):
    df = pd.DataFrame([[row[c] for c in columns] for row in result], columns=columns)
    df.columns = map(str.upper, df.columns)
    return df


def to_object_list(result, columns):
    rows = []
    for item in result:
        row = {}
        for col in columns:
            row[col] = item[col]
        rows.append(row)
    return rows


class DatabaseClient:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def session(self):
        return self.driver.session()

    def bulk_update(self, records, query_fn, batch_size=1000):
        with tqdm(total=len(records), unit=' Records') as pbar:
            session = self.session()
            for record_index, record in enumerate(records):
                query_fn(session, record)
                pbar.update(1)
                if record_index % batch_size == 0:
                    session.close()
                    session = self.session()

    def run(self, query):
        with self.session() as session:
            session.read_transaction(lambda tx: tx.run(query))

    def query(self, query_fn):
        with self.session() as session:
            return session.read_transaction(query_fn)
