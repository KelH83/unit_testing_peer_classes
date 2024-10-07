from lib.diary import *
from lib.secret_diary import *
import pytest

diary_entry = Diary("A diary entry")
new_secret_diary = SecretDiary(diary_entry)

def test_creates_an_instance():
    assert isinstance(new_secret_diary, SecretDiary)

def test_read_returns_error_if_diary_locked():
    with pytest.raises(Exception) as e:
        new_secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"

def test_read_returns_diary_entry():
    new_secret_diary.unlock()
    assert new_secret_diary.read() == diary_entry