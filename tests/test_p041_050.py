from p041_050.p041 import find_largest_pandigital_prime


def test_p041_find_largest_pandigital_prime():
    assert find_largest_pandigital_prime(1) == None
    assert find_largest_pandigital_prime(2) == None
    assert find_largest_pandigital_prime(3) == None
    assert find_largest_pandigital_prime(4) == 4231
    assert find_largest_pandigital_prime(5) == None
    assert find_largest_pandigital_prime(6) == None
    assert find_largest_pandigital_prime(7) == 7652413
