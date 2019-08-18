#!/usr/bin/env python3

import algo
import pytest

@pytest.fixture
def data():

    return [3, 2, 1, 5, -3, 2, 0, -2, 11, 9]

def test_sel_sort(data):

    sorted_vals = algo.sel_sort(data)
    assert sorted_vals == sorted(data)
