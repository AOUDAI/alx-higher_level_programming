#!/usr/bin/python3
""" prints the State object with the name passed as argument
from the database hbtn_0e_6_usa"""


if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    id = session.query(State.id).filter(State.name.like(sys.argv[4])).scalar()
    if (id):
        print(id)
    else:
        print("Not found")

    session.close()
