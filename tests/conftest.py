from os import getenv
from typing import AnyStr

import pytest


def str_to_bool(value: AnyStr) -> bool:
    """
    Convert a string representation of truth to True or False.

    True values are 'y', 'yes', 't', 'true', 'on', and '1';
    false values are 'n', 'no', 'f', 'false', 'off', and '0'.
    Raises ValueError if 'val' is anything else.
    """
    value = str(value).lower()
    if value in {"y", "yes", "t", "true", "on", "1"}:
        return True
    elif value in {"n", "no", "f", "false", "off", "0"}:
        return False
    else:
        raise ValueError(f"Invalid truth value {value}")


# Used to omit certain tests, based on the value of the `CI` env var.
skip_in_ci = pytest.mark.skipif(
    str_to_bool(getenv("CI", "false")),
    reason="Test marked as not suitable to run in Continuous Integration environment.",
)
