import sqlite3


try:
    connection = sqlite3.connect("AMR_text.db")
    cursor = connection.cursor()
    print("Successfully connected to SQLite3")

    create_pilot_table = """CREATE TABLE pilot (
                        id INTEGER PRIMARY KEY,
                        pilot TEXT NOT NULL,
                        information TEXT NOT NULL,
                        join_date datetime,
                        callsign TEXT NOT NULL,
                        flight_hours INTEGER NOT NULL);"""

except sqlite3.Error as error:
    print("Error while creating ")