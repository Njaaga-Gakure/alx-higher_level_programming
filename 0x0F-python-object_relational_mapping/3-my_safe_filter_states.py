#!/usr/bin/python3
"""Safe from SQl injection module."""
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
    query = "SELECT * FROM states\
             WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))
    response = cursor.fetchall()
    for row in response:
        if row[1] == sys.argv[4]:
            print(row)
    cursor.close()
    connect.close()
