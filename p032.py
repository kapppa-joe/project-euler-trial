from util import pandigital_generator


def p032():
    # Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
    '''
    as 10^a * 10^b = 10^(a+b), so the number of digits in multiplicand/multiplier/product must be a combination of either 1/4/4 or 2/3/4
    here I traverse all pandigital nums made by 1-9 and check where spliting into 1/4/4 or 2/3/4 give a set of triplets satisfying the condition a * b = c.
    '''

    products = set()

    for num in pandigital_generator():
        num_str = str(num)
        for i, j in [(1, 4), (2, 3)]:
            (a, b, c) = num_str[:i], num_str[i:i+j], num_str[i+j:]
            if int(a) * int(b) == int(c):
                print(f'found triplets: {a} * {b} = {c}')
                products.add(int(c))

    return sum(products)
