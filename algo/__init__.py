from typing import *
import collections
import dataclasses
import math

# noinspection PyUnresolvedReferences
import pytest

from .datatypes import *


@dataclasses.dataclass
class TestCase:
    args: Tuple[any, ...]
    expected: any
