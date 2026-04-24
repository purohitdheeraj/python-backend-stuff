from sqlalchemy import select
from connection import engine, User
from sqlalchemy.orm import Session

# Create a new session
session = Session(engine)


# Query the user
query = select(User).where(User.name == 'Alice')
user = session.execute(query).scalars().first()

# Update the user's name
user.name = 'Alicia'

# Commit the changes
session.commit()
# print the updated user
print(user.name, user.email)
