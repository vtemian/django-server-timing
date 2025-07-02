# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Django Server Timing is a middleware library that exposes performance metrics via the HTTP Server-Timing header. The header allows browsers to display timing information in the Network tab's Timing section (Chrome 65+).

## Key Commands

### Testing
```bash
# Run all tests with coverage using uv
uv run pytest

# Alternative using Makefile
make test
```

### Development
```bash
# Install development dependencies with uv
uv sync --dev

# Install with silk integration for SQL timing
uv sync --dev --extra silk

# Install production dependencies only
uv sync

# Run the example Django app
make run
# or manually:
cd example && uv run python manage.py runserver

# Build the package
uv build
```

### Code Quality
```bash
# Run linting with Ruff
make lint

# Check code formatting
make format-check

# Auto-format code
make format

# Fix auto-fixable lint issues
make lint-fix
```

### Release Management
```bash
# Check if ready for release (lint, format, test, build)
make release-check

# Bump version
make version-patch  # 0.0.3 -> 0.0.4
make version-minor  # 0.0.3 -> 0.1.0
make version-major  # 0.0.3 -> 1.0.0

# Or use the script directly
python scripts/bump_version.py patch
python scripts/bump_version.py --dry-run minor
```

## Architecture

### Core Components

1. **`server_timing/middleware.py`** - Main middleware implementation
   - `ServerTiming` class - Django middleware that adds Server-Timing headers
   - `TimedService` class - For timing individual operations
   - `timed` context manager - For timing code blocks
   - `timed_wrapper` decorator - For timing functions
   - Uses thread-local storage for request isolation

2. **`server_timing/silk.py`** - Optional django-silk integration
   - `ServerTimingSilkMiddleware` - Adds SQL query timing
   - `ServerTimingSilkViewOnlyMiddleware` - Times only view execution

### How It Works

1. Middleware intercepts Django requests/responses
2. Timing services collect metrics during request processing
3. On response, all collected timings are formatted into Server-Timing header
4. Browser displays timings in DevTools Network tab

Example header output:
```
Server-Timing: index;desc="Index View";dur=800,first;desc="First service";dur=300,second;desc="Second service";dur=500
```

### Django Compatibility

- Supports Django 4.2+ through 5.1+
- Uses Django's modern header API (`response.headers`)
- Python 3.10+ required

### Package Management

- Uses `uv` for fast dependency management and virtual environments
- `pyproject.toml` defines project configuration and dependencies
- `uv.lock` provides reproducible dependency resolution
- Development dependencies include Django 4.2+, pytest 8.2+, and Ruff
- django-silk is available as optional dependency for SQL timing features
- Ruff configuration in `pyproject.toml` enforces code style and quality

## Testing Guidelines

- Tests use pytest with mocked `time.sleep()` for timing verification
- Unit tests in `tests/test_unit.py` cover timing services, decorators, context managers
- Integration tests in `tests/test_integration.py` verify header generation
- Always run tests before committing changes

## CI/CD

- Uses GitHub Actions for continuous integration (`.github/workflows/ci.yml`)
- Matrix testing across Python 3.10-3.12 and Django 4.2-5.1 
- Automated security scanning with pip-audit
- Code coverage reporting to Codecov
- Package build validation on every commit
- Automated code quality checks with Ruff (linting + formatting)
- **Automated PyPI publishing** on version tags via trusted publishing

### Release Process

1. **Prepare**: `make release-check` - runs all quality checks
2. **Version bump**: `make version-patch/minor/major` - updates version
3. **Commit & tag**: Commit changes and create `v*` tag
4. **Automatic publish**: GitHub Actions publishes to PyPI on tag push

See `RELEASING.md` for detailed release instructions.

## Important Notes

- License discrepancy: setup.py mentions Apache, but LICENSE file is GPL v3
- Uses modern Python packaging with `pyproject.toml` and `uv`
- Build process uses `uv build` to create wheel distributions
- Code formatting and linting enforced with Ruff
- Minimum Python version increased to 3.10 due to Django 4.2+ requirements
- Migrated from Travis CI to GitHub Actions for modern CI/CD
- Automated release management with version bumping scripts and PyPI publishing
- Release documentation in `RELEASING.md` with detailed instructions