#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Filter states by user input"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Open database connection
    state_searched = sys.argv[4]
    connection = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=sys.argv[1],
                                 password=sys.argv[2],
                                 db=sys.argv[3],)

    # prepare a cursor object using cursor() method
    cursor = connection.cursor()

    # execute SQL query using execute() method.
    cursor.execute(
        "SELECT * FROM states WHERE name=%s ORDER BY id ASC",
        (state_searched,))

    # Fetch a single row using fetchone() method.
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # disconnect from server
    cursor.close()
    connection.close()
