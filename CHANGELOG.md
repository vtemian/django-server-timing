# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-07-02

### Added
- Comprehensive changelog documentation
- Modern CI/CD pipeline with GitHub Actions
- Matrix testing across Python 3.10-3.12 and Django 4.2-5.1
- Automated PyPI publishing on version tags
- Security scanning with pip-audit
- Code quality checks with Ruff (linting and formatting)
- Package build validation in CI
- Digital attestations for package security

### Changed
- **BREAKING**: Minimum Python version increased to 3.10 (from 3.8)
- **BREAKING**: Minimum Django version increased to 4.2 (from 3.2)
- Modernized project structure with `pyproject.toml` and `uv` for dependency management
- Migrated from Travis CI to GitHub Actions
- Updated django-silk dependency from git+https://github.com/jazzband/django-silk.git to PyPI version (>=5.4.0)
- Improved development workflow with better dependency resolution
- Enhanced release process with automated version bumping

### Fixed
- Resolved CI/CD pipeline failures due to dependency conflicts
- Fixed PyPI upload restrictions by removing direct git dependencies
- Corrected GitHub Actions artifact upload/download actions (v3 → v4)
- Improved version generation for clean releases without dev suffixes
- Enhanced compatibility with modern Django versions

### Removed
- Support for Python 3.8 and 3.9
- Support for Django 3.2, 4.0, and 4.1
- Travis CI configuration
- Direct git dependencies that caused PyPI upload failures

## [0.0.3] - Previous Release

### Features
- Django middleware for Server-Timing header support
- Thread-local storage for request isolation
- Timing services and context managers
- Django-silk integration for SQL query timing
- Compatible with Django 3.2+ and Python 3.8+

---

**Note**: This changelog was introduced in version 0.2.0. Previous versions may not have detailed change documentation.

For more information about Server-Timing header support, see the [README](README.md).