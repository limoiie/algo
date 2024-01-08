from typing import *
import dataclasses

# noinspection PyUnresolvedReferences
import pytest

from .datatypes import *


@dataclasses.dataclass
class TestCase:
    args: Tuple[any, ...]
    expected: any
