import argparse

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from connection import SessionLocal, User, create_tables


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Seed a user into the database.")
    parser.add_argument("--name", default="Alice", help="User name to insert")
    parser.add_argument(
        "--email", default="alice@example.com", help="User email (must be unique)"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Insert a new row even if the email already exists",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    create_tables()

    session = SessionLocal()
    try:
        existing = session.execute(
            select(User).where(User.email == args.email)
        ).scalars().first()

        if existing and not args.force:
            print(
                f"User with email '{args.email}' already exists (id={existing.id}). "
                "Use --force to bypass this check."
            )
            return

        new_user = User(name=args.name, email=args.email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        print(f"Inserted user: id={new_user.id}, name={new_user.name}, email={new_user.email}")
    except SQLAlchemyError as exc:
        session.rollback()
        print(f"Database error while seeding user: {exc}")
        raise
    finally:
        session.close()


if __name__ == "__main__":
    main()