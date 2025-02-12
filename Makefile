.PHONY: help
help:
	@echo "Available targets:"
	@echo "  make clean           - Remove the database and migration files (WARNING: deletes your current DB and migrations)"
	@echo "  make run_migrations  - Create and apply migrations for safety_app"
	@echo "  make load_genes      - Load gene data from data/genes.jsonl"
	@echo "  make setup           - Clean the project, run migrations, and load gene data"
	@echo "  make test            - Run the tests"
	@echo "  make run_server      - Start the Django development server on port 8080"
	@echo "  make run_end_to_end  - Run migrations, load gene data, run tests, then start the server (without cleaning first)"

.PHONY: clean
clean:
	@echo "Cleaning up database and migration files..."
	@rm -f db.sqlite3
	@rm -rf safety_app/migrations/*
	@echo "Clean complete."

.PHONY: run_migrations
run_migrations:
	@echo "Creating migrations for safety_app..."
	poetry run python manage.py makemigrations safety_app
	@echo "Applying migrations..."
	poetry run python manage.py migrate
	@echo "Migrations complete."

.PHONY: load_genes
load_genes:
	@echo "Loading gene data from data/genes.jsonl..."
	poetry run python manage.py load_genes data/genes.jsonl
	@echo "Gene data loading complete."

.PHONY: setup
setup: clean run_migrations load_genes
	@echo "Project setup complete."

.PHONY: test
test:
	@echo "Running tests..."
	poetry run pytest

.PHONY: run_server
run_server:
	@echo "Starting Django development server on port 8080..."
	poetry run python manage.py runserver 8080

.PHONY: run_end_to_end
run_end_to_end: run_migrations load_genes test run_server
	@echo "End-to-end run complete."
