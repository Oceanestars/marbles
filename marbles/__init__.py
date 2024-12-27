# type: ignore[attr-defined]
"""`Marbles` is a python packages that uses the Twilio API to send myself important reminder which won't quit upon dismissal like an old boring reminder"""

import sys
from importlib import metadata as importlib_metadata


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()
