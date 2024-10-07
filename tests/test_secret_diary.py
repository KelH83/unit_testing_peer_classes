from lib.secret_diary import *
from unittest.mock import Mock
import pytest

def test_creates_instance_of_a_diary():
    fake_diary = Mock()
    new_diary = SecretDiary(fake_diary)
    assert isinstance(new_diary, SecretDiary)
    assert new_diary.diary == fake_diary

def test_instance_creation_throws_error_for_wrong_datatype():
    with pytest.raises(Exception) as e:
        fake_diary = 123
        new_diary = SecretDiary(fake_diary)
    error_message = str(e.value)
    assert error_message == "Only class instances are allowed!"

def test_calling_lock_locks_diary():
    fake_diary = Mock()
    new_diary = SecretDiary(fake_diary)
    new_diary.lock()
    assert new_diary.locked == True

def test_calling_unlock_unlocks_diary():
    fake_diary = Mock()
    new_diary = SecretDiary(fake_diary)
    new_diary.unlock()
    assert new_diary.locked == False

def test_read_raises_error_go_away_if_locked():
    fake_diary = Mock()
    new_diary = SecretDiary(fake_diary)
    with pytest.raises(Exception) as e:
        new_diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"

def test_read_returns_diary_if_unlocked():
    fake_diary = Mock()
    new_diary = SecretDiary(fake_diary)
    new_diary.unlock()
    assert new_diary.read() == fake_diary