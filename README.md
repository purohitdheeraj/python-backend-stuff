# Python Backend Starter Template

Lightweight starter template for learning and building Python backends with:
- SQLAlchemy ORM
- MySQL connector
- Environment-based configuration
- Makefile task runner

## Quick Start

1. Create your env file:
   - `cp .env.example .env`
2. Update DB credentials in `.env`
3. Create virtual environment:
   - `make venv`
4. Install dependencies:
   - `make install`
5. Start MySQL (macOS/Homebrew):
   - `make mysql-start`
6. Create tables:
   - `make db-init`
7. Seed demo data:
   - `make db-seed`

## Available Commands

- `make help` - list all commands
- `make install` - install Python dependencies
- `make run` - run HTTP example script
- `make db-init` - create tables
- `make db-seed` - insert default user safely
- `make db-query` - query and update user
- `make db-flush` - delete all rows in `village` table
- `make mysql-start` - start MySQL via Homebrew
- `make mysql-stop` - stop MySQL via Homebrew
- `make mysql-status` - view MySQL service status

## Notes

- `db-seed` is idempotent by email unless `--force` is used.
- `db-query` handles "user not found" safely.
- `db-flush` asks confirmation by default; Makefile uses `--yes`.
