class UserData:
    def __init__(self, database) -> None:
        self.database = database

    def get_users(self):
        return self.database.execute_query("SELECT * FROM users;")