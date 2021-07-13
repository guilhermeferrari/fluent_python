from types import MappingProxyType


# Example 3-9 (MappingProxyType)
import pytest


def test_basic_usage_mapping_proxy_type():
    d = {1: "A"}
    d_proxy = MappingProxyType(d)
    assert d_proxy[1] == d[1]

    with pytest.raises(TypeError):
        d_proxy[2] = "_"

    d[2] = "new_value_at_origin"
    assert d_proxy[2] == d[2]