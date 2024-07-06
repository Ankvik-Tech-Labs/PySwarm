"""Honey Swarm is a Swarm light client implemented in Python 🐍"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pyswarm")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
