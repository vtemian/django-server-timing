try:
    from importlib.metadata import version

    __version__ = version("django-server-timing")
except Exception:
    # Fallback version if package not installed or metadata unavailable
    __version__ = "0.0.3"
