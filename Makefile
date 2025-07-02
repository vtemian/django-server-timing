full-test: test

test:
	uv run pytest

run:
	cd example && \
		uv run python manage.py runserver

build:
	uv build

install:
	uv sync --dev

install-prod:
	uv sync

lint:
	uv run ruff check .

format:
	uv run ruff format .

format-check:
	uv run ruff format --check .

lint-fix:
	uv run ruff check --fix .

version-patch:
	python scripts/bump_version.py patch

version-minor:
	python scripts/bump_version.py minor

version-major:
	python scripts/bump_version.py major

release-check:
	@echo "Running pre-release checks..."
	make lint
	make format-check
	make test
	uv build
	@echo "✅ All checks passed - ready for release!"

.PHONY: test full-test build lint format format-check lint-fix run install install-prod version-patch version-minor version-major release-check
