#!/usr/bin/python3
"""
test `"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                   (argv[4],))

    for states in cur.fetchall():
        print(states)

    cur.close()
    db.close()
