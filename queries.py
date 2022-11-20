import json
import pandas as pd
import sqlite3

# Connecting to the database
connection = sqlite3.connect("fortune.db")

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

def parse_to_json(df):
    result = df.to_json(orient="records")
    parsed = json.loads(result)
    return json.dumps(parsed, indent=4)  

def searchAll():
    # get all the data from database
    sql = """
    SELECT * FROM fortune;
    """

    # executing the SQL query
    cursor.execute(sql)

    # storing the data in a variable using fetchall() method
    alldata = cursor.fetchall()  # a list of tuples
    df = pd.DataFrame(alldata)
    result = parse_to_json(df)
    return result


def searchTop100ChineseCompanies():
    # get all the data from database
    sql = """
    SELECT Rank, Name, Country, Sales, Profit, Assets, MarketValue 
    FROM fortune
    WHERE Rank <= 100 AND Country = 'China' AND Name NOT LIKE "%China%"
    LIMIT 10
    ;
    """

    # executing the SQL query
    cursor.execute(sql)

    # storing the data in a variable using fetchall() method
    alldata = cursor.fetchall()  # a list of tuples
    df = pd.DataFrame(alldata)
    result = parse_to_json(df)
    return result


def searchCountriesByNumberOfTop100Companies():
    # get all the data from database
    sql = """
    SELECT Country, Count(*)
    FROM Fortune
    WHERE Rank <= 100
    GROUP BY Country
    ORDER BY Count(*) DESC;
    ;
    """

    # executing the SQL query
    cursor.execute(sql)

    # storing the data in a variable using fetchall() method
    alldata = cursor.fetchall()  # a list of tuples
    df = pd.DataFrame(alldata)
    result = parse_to_json(df) 
    return result


def searchCountriesRankedByMarketValue():
    # get all the data from database
    sql = """
    SELECT Country, MAX(MarketValue) as MaxMarketValue
    FROM Fortune
    GROUP BY Country
    ;
    """

    # executing the SQL query
    cursor.execute(sql)

    # storing the data in a variable using fetchall() method
    alldata = cursor.fetchall()  # a list of tuples
    df = pd.DataFrame(alldata)
    result = parse_to_json(df)
    return result
