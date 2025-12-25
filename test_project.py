from project import (
    select_language,
    translate,
    add_word,
    list_words,
    save_dict,
)

TEST_FILE = "test_dictionary.json"

def set_function():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    save_dict({}, TEST_FILE)

def test_select_language():
    lang = select_language("Hindi", TEST_FILE)
    data = add_word("apple", "सेब", "hindi", TEST_FILE)
    save_dict(data, TEST_FILE)
    data = add_word("apple", "pomme", "french", TEST_FILE)
    save_dict(data, TEST_FILE)
    assert lang == "hindi"

def test_add_word_multi_language():
    assert translate("apple", "hindi", TEST_FILE) == "सेब"
    assert translate("apple", "french", TEST_FILE) == "pomme"


def test_list_words_language():

    assert list_words("hindi", TEST_FILE) ==["apple"]
    assert list_words("french", TEST_FILE) ==["apple"]

def test_translate_not_found():

    assert translate("test", "hindi", TEST_FILE) == "Word not found"

def test_translate_unknown_language():

    assert translate("hello", "german", TEST_FILE) == "Language not found"




