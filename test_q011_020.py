from q011_020 import q011, Q011_grid_raw


test_grid = """3 3 0 1 1
0 1 10 1 1
4 2 1 2 5"""


def test_q011():
    assert q011(Q011_grid_raw, 1) == 99
    assert q011(Q011_grid_raw, 2) == 99 * 97
    assert q011(Q011_grid_raw, 3) == 89 * 94 * 97
    assert q011(Q011_grid_raw, 4) == 70600674

    # test that it can work with other grids
    assert q011(test_grid, 1) == 10
    assert q011(test_grid, 2) == 3 * 10
    assert q011(test_grid, 3) == 3 * 10 * 2
    assert q011(test_grid, 4) == 2 * 1 * 2 * 5
    assert q011(test_grid, 5) == 4 * 2 * 1 * 2 * 5
