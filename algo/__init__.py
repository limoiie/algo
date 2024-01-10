from typing import *

import collections
import dataclasses
import heapq
import math

import pytest

from algo.datatypes import *


@dataclasses.dataclass
class TestCase:
    args: Tuple[any, ...]
    expected: any
