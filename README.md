# Python Backend Starter Template

Lightweight starter template for learning and building Python backends with:
- SQLAlchemy ORM
- MySQL connector
- Environment-based configuration
- Makefile task runner

## Quick Start

1. Create env file: `cp .env.example .env`
2. Update DB credentials in `.env`
3. Create virtual environment: `make venv`
4. Install dependencies: `make install`
5. Start MySQL (macOS/Homebrew): `make mysql-start`


## Available Commands

- `make help` - list all commands
- `make venv` - create local virtual environment
- `make activate` - print activation command
- `make install` - install Python dependencies
- `make db-check` - verify database connection
- `make db-init` - create DB tables from models
- `make freeze` - update `requirements.txt` from installed deps
- `make mysql-start` - start MySQL via Homebrew
- `make mysql-stop` - stop MySQL via Homebrew
- `make mysql-status` - view MySQL service status

## Typical Flow

```bash
make venv
source venv/bin/activate
make install
make mysql-start
make db-check
make db-init
```
