import sqlite3
import csv

def init_db():
    # Connecting to the database
    connection = sqlite3.connect("fortune.db")

    # Creating a cursor object to execute
    # SQL queries on a database table
    cursor = connection.cursor()

    drop_table = """DROP TABLE IF EXISTS fortune"""
    cursor.execute(drop_table)

    # Table Definition
    create_table = """CREATE TABLE fortune(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Rank INTEGER NOT NULL,
                    Name TEXT NOT NULL,
                    Country TEXT NOT NULL,
                    Sales TEXT NOT NULL,
                    Profit TEXT NOT NULL,
                    Assets TEXT NOT NULL,
                    MarketValue TEXT NOT NULL);
                    """

    # Creating the table into our
    # database
    cursor.execute(create_table)

    # Opening the fortune.csv file
    file = open("fortune.csv")

    # Reading the contents of the
    # person-records.csv file
    contents = csv.reader(file)

    # SQL query to insert data into the
    # person table
    insert_records = "INSERT INTO fortune (Rank, Name, Country, Sales, Profit, Assets, MarketValue) VALUES(?, ?, ?, ?, ?, ?, ?)"

    # Importing the contents of the file
    # into our person table
    cursor.executemany(insert_records, contents)

    # Committing the changes
    connection.commit()

    # closing the database connection
    connection.close()
