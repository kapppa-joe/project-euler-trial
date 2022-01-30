from random import randint
from p071_080.p071 import p071
from p071_080.p072 import p072
from p071_080.p073 import p073
from p071_080.p074 import chain_length, fac_of_digits, p074
from p071_080.p075 import calc_L, p075, upper_limit_for_m, generate_m_n_pairs, search_unique_L, brute_force_func_for_testing

from p031_040.p039 import count_right_angle_triangles, is_right_angle_triangle

from farey_seq import farey_sequence


def test_p071():
    assert p071(target_d=8) == (2, 5)
    assert p071(2, 3, 8) == (5, 8)
    assert p071(5, 6, 7) == (4, 5)
    assert p071(123, 4567, 10000) == (269, 9988)
    assert p071(target_d=10000) == (4283, 9994)
    assert p071(target_d=1_000_000) == (428570, 999997)


def test_p072():
    assert p072(8) == 21


def test_p073():
    assert p073(1, 3, 1, 2, 8) == 3

    # random test
    for _ in range(5):
        n = randint(10, 100)
        seq = list(farey_sequence(n))
        for _ in range(10):
            (start, stop) = sorted(
                (randint(0, len(seq) - 1), randint(0, len(seq) - 1)))
            a, b = seq[start]
            c, d = seq[stop]
            assert p073(a, b, c, d, n) == stop - start - 1


def test_p074_fac_of_digits():
    assert fac_of_digits(1) == 1
    assert fac_of_digits(101) == 3
    assert fac_of_digits(91) == 362881

    assert fac_of_digits(145) == 145

    assert fac_of_digits(169) == 363601
    assert fac_of_digits(363601) == 1454
    assert fac_of_digits(1454) == 169

    assert fac_of_digits(871) == 45361
    assert fac_of_digits(45361) == 871

    assert fac_of_digits(872) == 45362
    assert fac_of_digits(45362) == 872


def test_p074_chain_length():
    assert chain_length(69) == 5
    assert chain_length(540) == 2
    assert chain_length(78) == 4
    assert chain_length(169) == 3


def test_p074():
    assert p074(upper_limit=10, req_terms=1) == 2
    assert p074() == 402


def test_p075_brute_force_func_for_testing():
    upper_limit = 200
    actual_output = brute_force_func_for_testing(upper_limit)
    for L in range(upper_limit):
        if L in actual_output:
            assert actual_output[L] == count_right_angle_triangles(L)
        else:
            assert count_right_angle_triangles(L) == 0


def test_p075_upper_limit_for_m():
    for _ in range(20):
        L_limit = randint(10, 1000)
        m = upper_limit_for_m(L_limit)
        assert calc_L(m, 1) >= L_limit
        assert calc_L(m-1, 1) < L_limit


def test_p075_generate_m_n_pairs():
    pairs_list = list(generate_m_n_pairs(100))
    assert len(pairs_list) == len(set(pairs_list))  # check no duplicates

    for m, n in generate_m_n_pairs(100):
        # check every pairs can form a right angle triangle
        a = m * n
        b = (m * m - n * n) // 2
        c = (m * m + n * n) // 2
        assert is_right_angle_triangle(a, b, c)


def test_p075_search_unique_L():
    test_limit = 500
    table_for_checking = brute_force_func_for_testing(limit_of_L=test_limit)

    expected_output = {
        L for L in table_for_checking if table_for_checking[L] == 1}
    actual_output = search_unique_L(limit_of_L=test_limit)

    assert set(actual_output) == expected_output


def test_p075():
    assert p075() == 161667
