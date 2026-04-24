PYTHON ?= python3
PIP ?= $(PYTHON) -m pip
VENV ?= venv
VENV_PYTHON = $(VENV)/bin/python
VENV_PIP = $(VENV_PYTHON) -m pip

.PHONY: help venv activate install run db-seed db-query db-flush http-test freeze clean mysql-start mysql-stop mysql-status

help:
	@echo "Available tasks:"
	@echo "  make venv       - Create local virtual environment"
	@echo "  make activate   - Print command to activate virtual environment"
	@echo "  make install    - Install dependencies from requirements.txt"
	@echo "  make run        - Run default script (my_http_test.py)"
	@echo "  make db-seed    - Insert sample user (data.py)"
	@echo "  make db-query   - Run update/delete sample query (query.py)"
	@echo "  make db-flush   - Delete all rows from village table"
	@echo "  make http-test  - Run HTTP test script"
	@echo "  make freeze     - Freeze current deps into requirements.txt"
	@echo "  make clean      - Remove local caches"
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

run:
	$(VENV_PYTHON) my_http_test.py

db-seed:
	$(VENV_PYTHON) data.py

db-query:
	$(VENV_PYTHON) query.py

db-flush:
	$(VENV_PYTHON) flush_db.py

http-test:
	$(VENV_PYTHON) my_http_test.py

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
