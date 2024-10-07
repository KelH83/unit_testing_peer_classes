from lib.diary import *
import pytest

new_diary = Diary("Diary entry")

def test_creates_instance_of_diary():
    assert isinstance(new_diary, Diary)
    assert new_diary.contents == "Diary entry"

def test_instance_creation_throws_error_for_wrong_datatype():
    with pytest.raises(Exception) as e:
        new_diary = Diary(123)
    error_message = str(e.value)
    assert error_message == "Only strings are allowed!"
    
def test_read_returns_diary_contents():
    assert new_diary.read() == "Diary entry"
