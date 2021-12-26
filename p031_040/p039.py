import functools


def is_right_angle_triangle(a: int, b: int, c: int) -> bool:
    return a ** 2 + b ** 2 == c ** 2


@functools.cache
def count_right_angle_triangles(p: int) -> int:
    # count the number of right angle triangle with integral length sides that can be formed with perimeter p.
    c_limit = p // 2 + 1  # c > p/2 cannot form a triangle
    count_triangles = 0

    for c in range(1, c_limit):
        for b in range(1, c):
            a = p - c - b
            if a > b:
                continue  # set limit a <= b to filter out duplications
            if is_right_angle_triangle(a, b, c):
                count_triangles += 1
    return count_triangles


def p039(limit: int = 1000) -> int:
    """ If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
        {20,48,52}, {24,45,51}, {30,40,50}
        For which value of p ≤ 1000, is the number of solutions maximised? """
    return max((p for p in range(12, limit + 1)), key=count_right_angle_triangles, default=0)
