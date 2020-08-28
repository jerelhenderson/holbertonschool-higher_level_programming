#!/usr/bin/python3
"""
lists all states from database with name starting with 'N'
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for states in cur.fetchall():
        if states[1][0] == 'N':
            print(states)

    cur.close()
    db.close()
