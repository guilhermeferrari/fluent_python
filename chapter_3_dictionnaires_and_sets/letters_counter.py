from collections import Counter


def test_simple_counter():
    word_to_count = "abracadabra"
    letters_count = Counter(word_to_count)

    assert letters_count == {
        "a": 5,
        "b": 2,
        "r": 2,
        "c": 1,
        "d": 1
    }
