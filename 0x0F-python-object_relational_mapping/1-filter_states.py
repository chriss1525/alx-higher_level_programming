#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""list all states with a name starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    connection = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=username,
                                 password=password,
                                 db=database)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name REGEXP '^N' ORDER BY id ASC;")

    for row in cursor.fetchall():
                   print(row)

    cursor.close()
    connection.close()
