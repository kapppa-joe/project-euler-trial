from number_triangle import NumberTriangle


def p067():
    triangle_str_raw = open("constant_inputs/p067_triangle.txt").read()
    triangle = NumberTriangle(triangle_str_raw)
    return triangle.max_value()
