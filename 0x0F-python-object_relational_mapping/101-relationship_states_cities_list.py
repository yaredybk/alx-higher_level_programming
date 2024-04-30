#!/usr/bin/python3
"""
ORM python3
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

# do not execute this at import
if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    tmps = None
    for s, c in session.query(State, City).join(City).order_by(State.id, City.id):
        if (tmps != s):
            print(f"{s.id}: {s.name}")
        print(f"\t{c.id}: {c.name}")
        tmps = s
#        print("{}: {}".format(state.id, state.name))
#        for city in state.cities:
#            print("    {}: {}".format(city.id, city.name))
