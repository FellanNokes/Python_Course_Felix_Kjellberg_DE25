from pytest import raises
from vector import Vector

def test_valid_init():
    v = Vector(1,2)
    assert v.numbers == (1,2)

# test negative values in init 
def test_negative_values_init():
    v = Vector(-1,-2)
    assert v.numbers == (-1,-2)
# test string in the init 
def test_string_init_fail():
    with raises(TypeError):
        Vector("1",2)
# test len() function
def test_len_function():
    v = Vector(1,2,3)
    assert len(v) == 3
# test abs() function 
def test_abs_function():
    v = Vector (3,4)

    assert abs(v) == 5
def test_empty_vector_fail():
    with raises(ValueError):
        Vector()