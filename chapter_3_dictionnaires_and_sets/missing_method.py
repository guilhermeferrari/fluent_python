import collections
import pytest


class StrDictKey(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]

        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


def test_access_dict_with_str_or_int():
    str_dict = StrDictKey({
        "2": "two",
        "4": "four"
    })
    assert str_dict[2] == str_dict["2"]
    assert str_dict[4] == str_dict["4"]

    with pytest.raises(KeyError):
        _ = str_dict[1]

    assert str_dict.get(2) == str_dict[2]
    assert str_dict.get(1) is None

