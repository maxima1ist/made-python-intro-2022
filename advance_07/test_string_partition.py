import pytest


def test_string_partition():
    with pytest.raises(ValueError, match="empty separator"):
        "".partition("")

    with pytest.raises(ValueError, match="empty separator"):
        "some".partition("")

    assert "".partition(".") == ("", "", "")
    assert "12".partition(".") == ("12", "", "")
    assert ".1.2".partition(".") == ("", ".", "1.2")
    assert ".1.2".partition(".") == ("", ".", "1.2")
    assert "I could eat bananas all day".partition("bananas") == \
        ("I could eat ", "bananas", " all day")
    assert "I could eat bananas all day".partition("apples") == \
        ("I could eat bananas all day", "", "")
