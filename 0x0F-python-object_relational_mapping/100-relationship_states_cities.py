#!/usr/bin/python3
"""
    #!/usr/bin/python3

"""
import sys
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    args = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        args[1], args[2], args[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State(name="California")
    newCity = City(name="San Francisco", state=newState)
    newState.cities.append(newCity)
    session.add(newState)

    session.commit()
    session.close()