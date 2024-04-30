#!/usr/bin/python3
"""
ORM python3
"""


# do not execute this at import
if __name__ == '__main__':
    db = MySQLdb.connect(
            user=argv[1], passwd=argv[2], db=argv[3]
    )
    c = db.cursor()
    query = "SELECT `id`, `name` FROM `states` WHERE `states`.`name` = '{}' \
              ORDER BY `states`.`id`".format(argv[4])
    c.execute(query)
    [print(state) for state in c.fetchall()]
