import collections


def words_position(words: list[str]):
    dd = collections.defaultdict(list)
    for position, word in enumerate(words):
        dd[word].append(position)

    return dd


def test_words_position():
    test_words = "test phrase for counting repeated words for test for".split()
    repeat_positions = words_position(test_words)

    assert repeat_positions == {
        "test": [0, 7],
        "phrase": [1],
        "for": [2, 6, 8],
        "counting": [3],
        "repeated": [4],
        "words": [5],
    }


def test_default_dict_get():
    dd = collections.defaultdict(list)
    assert dd.get("random_key") is None
    assert dd["random_key"] == []

