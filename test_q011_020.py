from q011_020 import q011, Q011_grid_raw, q012, Q013_input_string, q013


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


def test_q012():
    assert q012(1) == 3
    assert q012(2) == 6
    assert q012(3) == 6
    assert q012(4) == 28
    assert q012(5) == 28
    assert q012(6) == 36
    assert q012(500) == 76576500


def test_q013():
    assert q013(Q013_input_string, 10) == '5537376230'
