CREATE_USER_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS telegram_users
        (ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        USERNAME CHAR(50),        
        FIRST_NAME CHAR(50),        
        LAST_NAME CHAR(50),
        UNIQUE (TELEGRAM_ID)
        )
"""

START_INSERT_USER_QUERY = """INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)"""

SELECT_USER_QUERY = """SELECT telegram_id, username, first_name FROM telegram_users"""
