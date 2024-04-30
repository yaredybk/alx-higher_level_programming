#!/usr/bin/python3
#./100-relationship_states_cities.py
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
    c.execute("SELECT `id`, `name` FROM `states` ORDER BY `state`.`id`")
    [print(f"({id}, '{state}'") for state in c.fetchall() if state[1][0] == "N"]
