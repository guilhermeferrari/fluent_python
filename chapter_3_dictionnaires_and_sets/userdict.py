import collections


# Example 3-8 (Subclassing UserDict)
class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)

        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item


def test_subclass_user_dict():
    dict_test = StrKeyDict()
    dict_test[1] = "test"

    assert dict_test == {"1": "test"}
    assert dict_test[1] == dict_test["1"]
