import argparse

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from connection import SessionLocal, User


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Find a user and optionally update the user's name."
    )
    parser.add_argument("--email", default="alice@example.com", help="User email to query")
    parser.add_argument(
        "--new-name",
        default="Alicia",
        help="If provided, update the user's name to this value",
    )
    parser.add_argument(
        "--no-update",
        action="store_true",
        help="Only query the user without updating",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    session = SessionLocal()

    try:
        user = session.execute(select(User).where(User.email == args.email)).scalars().first()
        if not user:
            print(f"No user found with email '{args.email}'.")
            return

        print(f"Found user: id={user.id}, name={user.name}, email={user.email}")
        if args.no_update:
            return

        previous_name = user.name
        user.name = args.new_name
        session.commit()
        print(f"Updated user name: '{previous_name}' -> '{user.name}'")
    except SQLAlchemyError as exc:
        session.rollback()
        print(f"Database error while querying/updating user: {exc}")
        raise
    finally:
        session.close()


if __name__ == "__main__":
    main()
