import pytest
from src.data_fetching import get_data
from src.tests.conftest import client, clubs, competitions, tests_database


def test_can_load_clubs(tests_database, clubs):
  assert tests_database.clubs == clubs[0]["clubs"]


def test_can_load_competitions(tests_database, competitions):
  assert tests_database.competitions == competitions[0]["competitions"]


def test_get_club_by_email(tests_database):
  assert get_data.get_club_by_email(
    tests_database.clubs[0]["email"]) == tests_database.clubs[0]


def test_get_club_by_email_returns_none_if_club_not_found_with_email(tests_database):
  assert get_data.get_club_by_email("test") is None
  assert get_data.get_club_by_email("") is None
  assert get_data.get_club_by_email({}) is None
  assert get_data.get_club_by_email(None) is None


def test_can_get_club_by_name(tests_database):
  assert get_data.get_club_by_name(
    tests_database.clubs[0]["name"]) == tests_database.clubs[0]


def test_get_club_by_name_returns_none_if_club_not_found_with_name(tests_database):
  assert get_data.get_club_by_name("test") is None
  assert get_data.get_club_by_name("") is None
  assert get_data.get_club_by_name({}) is None
  assert get_data.get_club_by_name(None) is None
  
  
def test_can_load_competitions(tests_database, competitions):
  assert tests_database.competitions == competitions[0]["competitions"]
  
  
def test_get_competition_by_name(tests_database):
  assert get_data.get_competition_by_name(
    tests_database.competitions[0]["name"]) == tests_database.competitions[0]
  
def test_get_competition_by_name_returns_none_if_competition_not_found_with_name(tests_database):
  assert get_data.get_competition_by_name("test") is None
  assert get_data.get_competition_by_name("") is None
  assert get_data.get_competition_by_name({}) is None
  assert get_data.get_competition_by_name(None) is None
  
  
def test_load_method(tests_database, clubs, competitions):
  assert tests_database.clubs == clubs[0]["clubs"]
  assert tests_database.competitions == competitions[0]["competitions"]