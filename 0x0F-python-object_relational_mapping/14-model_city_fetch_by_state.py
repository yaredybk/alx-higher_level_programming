#!/usr/bin/python3
"""
ORM python3
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

# do not execute this at import
if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    cc = session.query(City.id, City.name, State.name) \
        .join(State) \
        .filter(State.name.like('%a%')) \
        .order_by(City.id) \
        .all()
    for i, c, s in cc:
        print(f"{s}: ({i}) {c}")
