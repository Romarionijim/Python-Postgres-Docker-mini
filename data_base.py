import psycopg2

class DataBase:
    def __init__(self, host:str, user:str, password:str, database:str) -> None:
        self.conn = psycopg2.connect (
            host=host,
            user=user,
            password=password,
            database=database,
        )
        self.cur = self.conn.cursor()

    def execute_query(self, query:str):
        self.cur.execute(query)
        return self.cur.fetchall()

    def commit_and_close(self):
        self.conn.commit()
        self.conn.close()


