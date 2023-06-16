#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" select states from database """

import sys
import MySQLdb

if __name__ == "__main__":

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    connection = MySQLdb.connect(host="localhost",
                                 user=username,
                                 password=password,
                                 db=database,
                                 port=3306)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()

    connection.close()
