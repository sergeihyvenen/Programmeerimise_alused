import pytest
from quadratic_equation import solve_quadratic_equation as solve

def test_integer_values():
    assert solve(a:1, -3, c:2) == (1,2)

def test_float_values():
    assert solve(a:1, -4, c:3,75) == (1.5, 2,5)

def test_one_solution():
    assert solve (a:1, -4, c:4) == (2,)

def test_zero_solution():
    assert solve(a:10, b:2, c:1) == tuple()

def test_zero_division():
    assert solve(a:0, b:1, c:2) == tuple()