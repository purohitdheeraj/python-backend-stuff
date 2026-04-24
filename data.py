from sqlalchemy.orm import Session
from connection import engine, Base, User

# Create a new session
session = Session(engine)

# Create a new user
new_user = User(name='Alice', email='alice@example.com')

# Add and commit the user to the database
session.add(new_user)
session.commit()