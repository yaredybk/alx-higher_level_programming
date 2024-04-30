#!/usr/bin/python3
"""
ORM python3
"""
import MySQLdb
from sys import argv

# do not execute this at import
if __name__ == '__main__':
    db = MySQLdb.connect(
            user=argv[1], passwd=argv[2], db=argv[3]
    )
    c = db.cursor()
    query = "SELECT `id`, `name` FROM `states` \
            WHERE `states`.`name` REGEXP '{}' \
            ORDER BY `states`.`id` DESC".format(argv[4])
    c.execute(query)
    for s in c.fetchall():
        print(s)
