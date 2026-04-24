from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import os
from dotenv import load_dotenv
load_dotenv()

engine = create_engine(
    f"mysql+mysqlconnector://root:{os.getenv('MY_SQL_PASSWORD')}@localhost/village_app"
)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "village"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(100))

# THIS LINE CREATES TABLE
Base.metadata.create_all(engine)