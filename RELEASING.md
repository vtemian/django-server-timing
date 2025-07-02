# Release Process

This document describes how to create and publish releases for django-server-timing.

## Prerequisites

### PyPI Trusted Publishing Setup

1. **Create/access PyPI project**: https://pypi.org/project/django-server-timing/
2. **Configure Trusted Publishers** in PyPI project settings:
   - Go to project settings → Publishing → Add a new pending publisher
   - Repository owner: `vtemian`
   - Repository name: `django-server-timing`
   - Workflow name: `ci.yml`
   - Environment name: `pypi`

This allows GitHub Actions to publish to PyPI without storing API tokens.

## Release Steps

### 1. Prepare Release

Run pre-release checks to ensure everything is ready:

```bash
make release-check
```

This will:
- Run linting checks
- Verify code formatting
- Execute all tests
- Build the package
- Confirm all checks pass

### 2. Version Bump & Tag Creation

**Important**: This project uses **VCS-based versioning**. The version is determined by git tags, not by files.

Choose the appropriate version bump:

```bash
# For bug fixes (0.0.3 -> 0.0.4)
make version-patch

# For new features (0.0.3 -> 0.1.0)
make version-minor

# For breaking changes (0.0.3 -> 1.0.0)
make version-major
```

Or use the script directly:
```bash
python scripts/bump_version.py patch
python scripts/bump_version.py minor
python scripts/bump_version.py major
```

This will:
1. **Read current version** from latest git tag
2. **Calculate new version** based on bump type
3. **Create git tag** immediately (e.g., `v1.0.4`)

### 3. Push Tag

```bash
# Push the tag to trigger release
git push origin vX.Y.Z
```

**No commit is needed** - the version is determined entirely by the git tag!

### 4. Automatic Publication

When you push a tag starting with `v`, GitHub Actions will:

1. **Run all CI checks** (tests, linting, security)
2. **Build the package** (wheel and source distribution)
3. **Publish to PyPI** automatically via trusted publishing

Monitor the progress at: https://github.com/vtemian/django-server-timing/actions

### 5. Verify Release

After successful publication:

1. **Check PyPI**: https://pypi.org/project/django-server-timing/
2. **Test installation**:
   ```bash
   pip install django-server-timing==X.Y.Z
   ```
3. **Create GitHub Release** (optional):
   - Go to https://github.com/vtemian/django-server-timing/releases
   - Click "Create a new release"
   - Select the tag you just created
   - Add release notes describing changes

## Troubleshooting

### PyPI Publication Fails

1. **Check trusted publishing setup** in PyPI project settings
2. **Verify workflow environment name** matches "pypi"
3. **Ensure tag follows pattern** `v*` (e.g., `v1.0.0`)
4. **Check GitHub Actions logs** for detailed error messages

### Version Conflicts

If PyPI rejects due to existing version:
```bash
# Bump to next patch version
make version-patch
git add .
git commit -m "Bump to next version"
git tag vX.Y.Z+1
git push origin master && git push origin vX.Y.Z+1
```

### CI Failures

Before creating releases, always run:
```bash
make release-check
```

Fix any issues before proceeding with the release.

## Development Releases

For testing purposes, you can create development releases:

1. Use development version numbers: `X.Y.Z.devN`
2. Manually upload to TestPyPI first
3. Test installation from TestPyPI before production release

## Security

- **Never commit API tokens** - use trusted publishing
- **All releases go through CI** - no manual uploads
- **Security scanning** runs on every release
- **Code quality checks** enforced before publication