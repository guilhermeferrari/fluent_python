def test_error_handling():
    city = "São Paulo"
    encoded_city = city.encode("cp437", errors="ignore")
    assert encoded_city.decode("cp437") == "So Paulo"

    encoded_city = city.encode("cp437", errors="replace")
    assert encoded_city.decode("cp437") == "S?o Paulo"