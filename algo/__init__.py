from typing import *

import bisect
import collections
import dataclasses
import functools
import itertools
import heapq
import math

import pytest

from algo.datatypes import *


@dataclasses.dataclass
class TestCase:
    args: Tuple[any, ...]
    expected: any
