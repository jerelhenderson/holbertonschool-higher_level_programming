#!/usr/bin/python3
"""
list all `cities` of a state
"""
import MySQLdb
from sys import argv

split = 0


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3],charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    ORDER BY cities.id ASC")

    for states in cur.fetchall():
        if 
            print(', ', end="")
        else:
            print(states[0], end="")

    cur.close()
    db.close()
