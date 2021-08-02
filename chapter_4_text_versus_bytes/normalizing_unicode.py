from unicodedata import normalize

# To be safe, it may be good to sanitize user input with normalize('NFC', user_text) before saving.
#
# Ramalho, Luciano. Fluent Python (p. 122). O'Reilly Media. Kindle Edition.
def test_basic_normalization():
    s1 = "café"
    s2 = "cafe\u0301"
    assert len(s1) == 4
    assert len(s2) == 5

    s1_normalized_nfc = normalize("NFC", s1)
    s2_normalized_nfc = normalize("NFC", s2)
    assert len(s1_normalized_nfc) == 4
    assert len(s2_normalized_nfc) == 4

    s1_normalized_nfd = normalize("NFD", s1)
    s2_normalized_nfd = normalize("NFD", s2)
    assert len(s1_normalized_nfd) == 5
    assert len(s2_normalized_nfd) == 5


def test_special_chars():
    half = "½"
    half_normalized = normalize("NFKC", half)
    print(half_normalized)
    half_copied_from_print = "1⁄2"
    half_typed = "1/2"

    assert half_normalized == half_copied_from_print
    assert half_normalized != half_typed
    # Aqui para funcionar precisei copiar a saida do print.
    # Visualmente digitando 1/2 está igual mas tem algum problema de codificaçao