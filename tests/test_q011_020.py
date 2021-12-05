from q011_020 import collatz_next, collatz_chain, q011, Q011_grid_raw, q012, Q013_input_string, q013, q014, q015, q016, q017, q018, Q018_triangle_raw_input, q019


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


def test_collatz_next():
    assert collatz_next(2) == 1
    assert collatz_next(3) == 10
    assert collatz_next(4) == 2
    assert collatz_next(5) == 16
    assert collatz_next(6) == 3
    assert collatz_next(7) == 22
    assert collatz_next(8) == 4
    assert collatz_next(9) == 28
    assert collatz_next(10) == 5
    assert collatz_next(11) == 34
    assert collatz_next(16) == 8
    assert collatz_next(20) == 10
    assert collatz_next(22) == 11
    assert collatz_next(40) == 20
    assert collatz_next(13) == 40
    assert collatz_next(34) == 17
    assert collatz_next(17) == 52
    assert collatz_next(52) == 26
    assert collatz_next(26) == 13
    assert collatz_next(13) == 40
    assert collatz_next(28) == 14
    assert collatz_next(14) == 7


def test_collatz_chain():
    assert collatz_chain(1) == 1
    assert collatz_chain(2) == 2
    assert collatz_chain(3) == 8
    assert collatz_chain(4) == 3
    assert collatz_chain(5) == 6
    assert collatz_chain(6) == 9
    assert collatz_chain(7) == 17
    assert collatz_chain(8) == 4
    assert collatz_chain(9) == 20
    assert collatz_chain(10) == 7
    assert collatz_chain(11) == 15
    assert collatz_chain(12) == 10
    assert collatz_chain(13) == 10
    assert collatz_chain(16) == 5
    assert collatz_chain(20) == 8
    assert collatz_chain(40) == 9


def test_q014():
    assert q014(2) == 1
    assert q014(3) == 2
    assert q014(4) == 3
    assert q014(5) == 3
    assert q014(7) == 6
    assert q014(8) == 7
    assert q014(9) == 7
    assert q014(10) == 9
    assert q014(14) == 9
    assert q014(1_000_000) == 837799


def test_q015():
    assert q015(1, 1) == 2
    assert q015(1, 2) == 3
    assert q015(2, 2) == 6
    assert q015(20, 20) == 137846528820


def test_q016():
    assert q016(0) == 1
    assert q016(1) == 2
    assert q016(2) == 4
    assert q016(3) == 8
    assert q016(4) == 1 + 6
    assert q016(5) == 3 + 2
    assert q016(6) == 6 + 4
    assert q016(15) == 26
    assert q016(1000) == 1366


def test_q017():
    assert q017(1) == len('one')
    assert q017(2) == len('one') + len('two')
    assert q017(3) == len('one') + len('two') + len('three')
    assert q017(4) == len('one') + len('two') + len('three') + len('four')
    assert q017(5) == len('one') + len('two') + \
        len('three') + len('four') + len('five')
    assert q017(1000) == 21124


def test_q018():
    test_triangle = "3\n7 4\n2 4 6\n8 5 9 3"
    assert q018(test_triangle) == 23
    assert q018(Q018_triangle_raw_input) == 1074


def test_q019():
    assert q019() == 171
