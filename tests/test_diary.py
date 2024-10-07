from lib.diary import *

new_diary = Diary("Diary entry")

# NEED TO TEST FOR ERRORS

def test_creates_instance_of_diary():
    assert isinstance(new_diary, Diary)
    assert new_diary.contents == "Diary entry"

def test_read_returns_diary_contents():
    assert new_diary.read() == "Diary entry"