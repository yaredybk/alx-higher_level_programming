#!/usr/bin/python3
"""
ORM python3
"""
import re
import MySQLdb
from sys import argv

# do not execute this at import
if __name__ == '__main__':
    db = MySQLdb.connect(
            user=argv[1], passwd=argv[2], db=argv[3]
    )
    c = db.cursor()
    if not re.search("^[a-zA-Z0-9_]*$", argv[4]):
        raise ValueError("invalid input")
    query = "SELECT c.`name` \
            FROM `cities` c \
            JOIN `states` s \
            on `c`.`state_id` = `s`.`id` \
            WHERE s.`name` = '{}' \
            ORDER BY `c`.`id`".format(argv[4])
    c.execute(query)
    print(', '.join([a[0] for a in c.fetchall()]))
