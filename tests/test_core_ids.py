import pytest

from synthops.core.ids import generate_id, generate_ids


def test_generate_id_returns_expected_format():
    assert generate_id("RES", 1) == "RES0001"


def test_generate_id_uppercases_prefix():
    assert generate_id("res", 12) == "RES0012"


def test_generate_ids_returns_expected_count():
    ids = generate_ids("STAFF", 3)

    assert ids == ["STAFF0001", "STAFF0002", "STAFF0003"]


def test_generate_id_rejects_empty_prefix():
    with pytest.raises(ValueError):
        generate_id("", 1)


def test_generate_id_rejects_invalid_number():
    with pytest.raises(ValueError):
        generate_id("RES", 0)


def test_generate_ids_rejects_invalid_count():
    with pytest.raises(ValueError):
        generate_ids("RES", 0)


def test_generate_id_supports_custom_width():
    assert generate_id("HM", 1, width=3) == "HM001"


def test_generate_ids_supports_custom_width():
    ids = generate_ids("HM", 3, width=3)

    assert ids == ["HM001", "HM002", "HM003"]


def test_generate_id_strips_spaces_from_prefix():
    assert generate_id(" hm ", 1, width=3) == "HM001"


def test_generate_id_rejects_blank_prefix():
    with pytest.raises(ValueError):
        generate_id("   ", 1)


def test_generate_id_rejects_invalid_width():
    with pytest.raises(ValueError):
        generate_id("HM", 1, width=0)