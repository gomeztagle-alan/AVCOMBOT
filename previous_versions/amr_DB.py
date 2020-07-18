import sqlite3


try:
    connection = sqlite3.connect("AMR_text.db")
    cursor = connection.cursor()
    print("Successfully connected to SQLite3")

    create_pilot_table = """CREATE TABLE pilot (
                        id INTEGER PRIMARY KEY,
                        discord TEXT NOT NULL,
                        information TEXT NOT NULL,
                        join_date datetime,
                        callsign TEXT NOT NULL,
                        flight_hours INTEGER NOT NULL);"""

    create_amr_table = """CREATE TABLE amr (
                        id INTEGER PRIMARY KEY,
                        pilot_id INTEGER NOT NULL,
                        discord TEXT NOT NULL,
                        information TEXT NOT NULL,
                        date datetime,
                        callsign TEXT NOT NULL,
                        operation TEXT NOT NULL,
                        estimated TEXT NOT NULL,
                        duration INTEGER NOT NULL,
                        base TEXT NOT NULL,
                        FOREIGN KEY(pilot_id) REFERENCES pilot(id)
                        );"""
    cursor.execute(create_amr_table)
    connection.commit()
    print("Table created")

except sqlite3.Error as error:
    print("Error while creating table", error)
finally:
    if (connection):
        connection.close()
        print("sqlite connection is closed")