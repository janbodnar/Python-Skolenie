#!/usr/bin/env python3

import algo
import pytest

@pytest.mark.parametrize("data, expected", [((2, 3, 1, 4, 6), 1), 
    ((5, -2, 0, 9, 12), -2), ((200, 100, 0, 300, 400), 0)])
def test_min(data, expected):

    val = algo.min(data)
    assert val == expected

@pytest.mark.parametrize("data, expected", [((2, 3, 1, 4, 6), 6), 
    ((5, -2, 0, 9, 12), 12), ((200, 100, 0, 300, 400), 400)])
def test_max(data, expected):

    val = algo.max(data)
    assert val == expected
