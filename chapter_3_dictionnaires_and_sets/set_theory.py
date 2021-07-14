# Set basic operations

def test_basic_operations():
    a = {"a", "b", "c"}
    b = {"c", "d"}

    union = a | b
    assert union == {"a", "b", "c", "d"}

    intersection = a & b
    assert intersection == {"c"}

    difference = a - b
    assert difference == {"a", "b"}
