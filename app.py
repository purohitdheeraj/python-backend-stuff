import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import String, create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

load_dotenv()


def _build_db_url() -> str:
    db_user = os.getenv("DB_USER", "root")
    db_password = os.getenv("DB_PASSWORD") or os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "3306")
    db_name = os.getenv("DB_NAME", "flask_api_db")

    if not db_password:
        raise ValueError(
            "Missing DB password. Set DB_PASSWORD (or MY_SQL_PASSWORD) in your .env file."
        )

    safe_password = quote_plus(db_password)
    return (
        f"mysql+mysqlconnector://{db_user}:{safe_password}@"
        f"{db_host}:{db_port}/{db_name}"
    )


engine = create_engine(_build_db_url(), pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users" #change to the table name you want to use
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

def create_tables() -> None:
    Base.metadata.create_all(engine)


def check_db_connection() -> None:
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("DB connected successfully")
    except SQLAlchemyError as exc:
        raise RuntimeError(f"DB connection failed: {exc}") from exc
