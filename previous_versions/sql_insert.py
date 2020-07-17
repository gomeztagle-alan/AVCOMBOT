import sqlite3

try:
    sqliteConnection = sqlite3.connect("SQLite_Python.db")
    cursor = sqliteConnection.cursor()
    print("Succesfully connected to SQLite")

    sqlite_insert_query = """INSERT INTO SQLiteDb_developers 
                            (id, name, email, joining_date, salary)
                            VALUES
                            (2, 'Alan', 'agomeztagle7@gmail.com', '2019-07-10', 0)"""

    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record succesfully inserted into the SQLiteDb_developers table ", cursor)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into SqliteDb_developers table", error)
finally:
    if(sqliteConnection):
        sqliteConnection.close()
        print("The SQL connection is closed")