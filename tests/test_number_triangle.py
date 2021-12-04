from constant_inputs.q018_input import Q018_triangle_raw_input
from number_triangle import NumberTriangle
from constant_inputs.q018_input import Q018_triangle_raw_input


def test_get_number():
    tri = NumberTriangle(Q018_triangle_raw_input)
    assert tri.get(0, 0) == 75
    assert tri.get(1, 0) == 95
    assert tri.get(1, 1) == 64
    assert tri.get(14, 14) == 23


def test_next_cells():
    tri = NumberTriangle(Q018_triangle_raw_input)
    assert list(tri.next_cells(0, 0)) == [(1, 0), (1, 1)]
    assert list(tri.next_cells(1, 1)) == [(2, 1), (2, 2)]
    assert list(tri.next_cells(13, 5)) == [(14, 5), (14, 6)]
    assert list(tri.next_cells(14, 14)) == []  # no next cells in the last row


def test_max_value():
    tri = NumberTriangle(Q018_triangle_raw_input)
    assert tri.max_value(14, 0) == 4
    assert tri.max_value(14, 1) == 62
    assert tri.max_value(13, 0) == 63 + 62
    assert tri.max_value(13, 1) == 66 + 98
    assert tri.max_value(12, 1) == 71 + 66 + 98
