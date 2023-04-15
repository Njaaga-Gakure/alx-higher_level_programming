#!/usr/bin/python3
"""Select cities from a state entered as an input by a user."""
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
    query = "SELECT cities.name\
             FROM cities INNER JOIN states\
             ON cities.state_id = states.id\
             WHERE states.name=%s ORDER BY cities.id ASC"
    cursor.execute(query, (sys.argv[4], ))
    response = cursor.fetchall()

    x = 0
    for row in response:
        if (x > 0):
            print(", ", end="")
        x += 1
        print(row[0], end="")
    print("")
    cursor.close()
    connect.close()
