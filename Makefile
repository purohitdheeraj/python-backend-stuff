PYTHON ?= python3
PIP ?= $(PYTHON) -m pip
VENV ?= venv
VENV_PYTHON = $(VENV)/bin/python
VENV_PIP = $(VENV_PYTHON) -m pip

.PHONY: help venv activate install db-check db-init freeze clean mysql-start mysql-stop mysql-status

help:
	@echo "Available tasks:"
	@echo "  make venv         - Create local virtual environment"
	@echo "  make activate     - Print command to activate virtual environment"
	@echo "  make install      - Install dependencies from requirements.txt"
	@echo "  make db-check     - Verify database connection"
	@echo "  make db-init      - Create database tables"
	@echo "  make freeze       - Freeze current deps into requirements.txt"
	@echo "  make clean        - Remove local caches"
	@echo "  make mysql-start  - Start MySQL (Homebrew service)"
	@echo "  make mysql-stop   - Stop MySQL (Homebrew service)"
	@echo "  make mysql-status - Check MySQL status (Homebrew service)"

venv:
	$(PYTHON) -m venv $(VENV)

activate:
	@echo "Run this in your shell:"
	@echo "source $(VENV)/bin/activate"

install:
	$(VENV_PIP) install -r requirements.txt

db-init:
	$(VENV_PYTHON) -c "from app import create_tables; create_tables(); print('Tables ensured')"

db-check:
	$(VENV_PYTHON) -c "from app import check_db_connection; check_db_connection()"

freeze:
	$(VENV_PIP) freeze > requirements.txt

clean:
	rm -rf __pycache__ .pytest_cache

mysql-start:
	brew services start mysql

mysql-stop:
	brew services stop mysql

mysql-status:
	brew services info mysql
