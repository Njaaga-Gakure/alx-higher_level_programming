#!/usr/bin/python3
"""Join tables module."""
import MySQLdb
import sys


if __name__ == "__main__":
    connect = MySQLdb.connect(
                                host="localhost",
                                port=3306,
                                user=sys.argv[1],
                                passwd=sys.argv[2],
                                db=sys.argv[3],
                                charset="utf8"
                             )
    cursor = connect.cursor()
    query = "SELECT cities.id, cities.name, states.name\
             FROM cities INNER JOIN states\
             ON cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(query)
    response = cursor.fetchall()
    for row in response:
        print(row)
    cursor.close()
    connect.close()
