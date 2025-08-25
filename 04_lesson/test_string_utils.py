import pytest
from string_utils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


def test_capitalize(string_utils):
    # Позитивные тесты
    assert string_utils.capitalize("skypro") == "Skypro"
    assert string_utils.capitalize("hello world") == "Hello world"

    # Негативные тесты
    assert string_utils.capitalize("") == ""
    assert string_utils.capitalize("123abc") == "123abc"


def test_trim(string_utils):
    # Позитивные тесты
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("   hello world   ") == "hello world   "

    # Негативные тесты
    assert string_utils.trim("") == ""
    assert string_utils.trim("no spaces") == "no spaces"


def test_contains(string_utils):
    # Позитивные тесты
    assert string_utils.contains("SkyPro", "S") is True
    assert string_utils.contains("SkyPro", "o") is True

    # Негативные тесты
    assert string_utils.contains("SkyPro", "U") is False
    assert string_utils.contains("SkyPro", "z") is False


def test_delete_symbol(string_utils):
    # Позитивные тесты
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"

    # Негативные тесты
    assert string_utils.delete_symbol("SkyPro", "x") == "SkyPro"  # Символа нет
    assert string_utils.delete_symbol("", "a") == ""  # Пустая строка
