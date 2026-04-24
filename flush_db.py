from sqlalchemy import delete
from sqlalchemy.orm import Session

from connection import engine, User


session = Session(engine)

try:
    result = session.execute(delete(User))
    session.commit()
    print(f"Deleted {result.rowcount or 0} rows from '{User.__tablename__}' table.")
finally:
    session.close()
