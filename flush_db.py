import argparse
import sys

from sqlalchemy import delete

from connection import SessionLocal, User


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Delete all rows from the user table.")
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Skip interactive confirmation prompt",
    )
    return parser.parse_args()


def confirm_or_abort() -> None:
    confirmation = input(
        "This will delete ALL rows from table 'village'. Type 'yes' to continue: "
    ).strip()
    if confirmation.lower() != "yes":
        print("Aborted.")
        sys.exit(0)


def main() -> None:
    args = parse_args()
    if not args.yes:
        confirm_or_abort()

    session = SessionLocal()
    try:
        result = session.execute(delete(User))
        session.commit()
        print(f"Deleted {result.rowcount or 0} rows from '{User.__tablename__}' table.")
    finally:
        session.close()


if __name__ == "__main__":
    main()
