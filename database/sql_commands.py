import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_db(self):
        if self.connection:
            print("Database connected successfully")

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.commit()

    def sql_insert_users(self, telegram_id,
                         username, first_name, last_name):
        self.cursor.execute(sql_queries.START_INSERT_USER_QUERY,
                            (None, telegram_id, username, first_name, last_name)
                            )
        self.connection.commit()

    def sql_admin_select_username_users_table(self):
        self.cursor.row_factory = lambda cursor, row: {
            "telegram_id": row[0],
            "username": row[1],
            "first_name": row[2],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_QUERY
        ).fetchall()
