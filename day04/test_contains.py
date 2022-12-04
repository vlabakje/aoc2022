from one import fully_contains
from two import overlap

def test_fully_contains_basic():
    assert fully_contains((6, 6), (6, 6))
    assert fully_contains((6, 6), (6, 7))
    assert fully_contains((2, 8), (3, 7))
    assert fully_contains((6, 6), (4, 6))
    ## neg
    assert not fully_contains((6, 6), (7, 7))
    assert not fully_contains((7, 7), (6, 6))

def test_overlap():
    assert overlap((6, 6), (6, 6))
    assert overlap((6, 6), (6, 7))
    assert overlap((2, 8), (3, 7))
    assert overlap((6, 6), (4, 6))
