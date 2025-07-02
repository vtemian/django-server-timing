#!/usr/bin/env python3
"""
Version bumping script for django-server-timing using git tags.

Usage:
    python scripts/bump_version.py patch  # 0.0.3 -> 0.0.4
    python scripts/bump_version.py minor  # 0.0.3 -> 0.1.0
    python scripts/bump_version.py major  # 0.0.3 -> 1.0.0
"""

import argparse
import subprocess
import sys


def get_current_version():
    """Get current version from git tags"""
    try:
        # Get the latest tag
        result = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            capture_output=True,
            text=True,
            check=True,
        )
        tag = result.stdout.strip()
        # Remove 'v' prefix if present
        if tag.startswith("v"):
            return tag[1:]
        return tag
    except subprocess.CalledProcessError:
        # No tags found, start from 0.0.0
        return "0.0.0"


def bump_version(current_version, bump_type):
    """Bump version according to bump_type"""
    major, minor, patch = map(int, current_version.split("."))

    if bump_type == "major":
        return f"{major + 1}.0.0"
    elif bump_type == "minor":
        return f"{major}.{minor + 1}.0"
    elif bump_type == "patch":
        return f"{major}.{minor}.{patch + 1}"
    else:
        raise ValueError(f"Invalid bump type: {bump_type}")


def create_version_tag(new_version):
    """Create git tag for new version"""
    tag = f"v{new_version}"
    try:
        # Check if tag already exists
        subprocess.run(
            ["git", "tag", "-l", tag], capture_output=True, text=True, check=True
        )
        result = subprocess.run(
            ["git", "tag", "-l", tag], capture_output=True, text=True, check=True
        )
        if result.stdout.strip():
            raise ValueError(f"Tag {tag} already exists")

        # Create the tag
        subprocess.run(["git", "tag", tag], check=True)
        print(f"Created git tag: {tag}")
        return tag
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Failed to create tag: {e}") from e


def main():
    parser = argparse.ArgumentParser(
        description="Bump version for django-server-timing"
    )
    parser.add_argument(
        "bump_type", choices=["major", "minor", "patch"], help="Type of version bump"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )

    args = parser.parse_args()

    try:
        current_version = get_current_version()
        new_version = bump_version(current_version, args.bump_type)

        print(f"Current version: {current_version}")
        print(f"New version: {new_version}")

        if args.dry_run:
            print("Dry run - no changes made")
            return

        tag = create_version_tag(new_version)

        print(f"\nCreated tag: {tag}")
        print("Next steps:")
        print(f"1. Push tag: git push origin {tag}")
        print("2. GitHub Actions will automatically publish to PyPI")
        print(
            "3. Monitor progress: https://github.com/vtemian/django-server-timing/actions"
        )

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
