from math import *


def compute_len(x_1, x_2, y_1, y_2):
    len_line = sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    return len_line


def compute_perimetr(a, b, c):
    p = a+b+c
    return p


def compute_area(p, a, b, c):
    p_half = p/2
    s = sqrt(p_half * (p_half-a)*(p_half-b)*(p_half-c))
    return s


def compute_angle(a, b, c):
    angle = acos((c**2 + b**2 - a**2) / (2*c*b))
    return degrees(angle)


def compute_circumcircle(s, a, b, c):
    out_r = a*b*c/4/s
    return out_r


def compute_incircle(p, a, b, c):
    p_half = p * 0.5
    inc_r = sqrt((p_half-a)*(p_half-b)*(p_half-c) / p_half)
    return inc_r


def median_len(a, b, c):
    med = 0.5 * sqrt(2 * (a**2 + b**2) - a**2)
    return med


a_x = float(input("Input x value for point A: "))
a_y = float(input("Input y value for point A: "))
b_x = float(input("Input x value for point B: "))
b_y = float(input("Input y value for point B: "))
c_x = float(input("Input x value for point C: "))
c_y = float(input("Input y value for point C: "))


a_len = compute_len(b_x, c_x, b_y, c_y)
b_len = compute_len(a_x, c_x, a_y, c_y)
c_len = compute_len(b_x, a_x, b_y, a_y)


if a_len + b_len <= c_len or b_len + b_len <= a_len or a_len + c_len <= b_len:
    print("This is not a triangle!")
else:

    per = compute_perimetr(a_len, b_len, c_len)

    square = compute_area(per, a_len, b_len, c_len)

    a_angle = compute_angle(a_len, b_len, c_len)
    b_angle = compute_angle(b_len, c_len, a_len)
    c_angle = compute_angle(c_len, a_len, b_len)

    print("Lenghts of triangle`s sides = ", round(
        a_len, 3), round(b_len, 3), round(c_len, 3))
    print("Square of triangle = ", round(square, 3))
    print("Perimetr of triangle = ", round(per, 3))
    print("Angles are : {}, {}, {}".format(
        round(a_angle, 3), round(b_angle, 3), round(c_angle, 3)))
