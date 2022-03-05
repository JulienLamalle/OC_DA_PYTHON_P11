import pytest
import json
from src import server
from src.data_fetching import get_data

@pytest.fixture()
def client():
  with server.app.test_client() as client:
    yield client


@pytest.fixture
def webdriver():
  from selenium import webdriver
  from selenium.webdriver.firefox.service import Service
  from webdriver_manager.firefox import GeckoDriverManager

  service = Service(GeckoDriverManager().install())
  yield webdriver.Firefox(service=service)

@pytest.fixture()
def clubs(tmp_path_factory):
  clubs = {
    "clubs": [
      {"name": "Fake Club 1", "email": "fake_club_1@fake.com", "points": "0"},
      {"name": "Fake Club 2", "email": "fake_club_2@fake.com", "points": "12"},
      {"name": "Fake Club 3", "email": "fake_club_3@fake.com", "points": "100"},
      {"name": "Fake Club 4", "email": "fake_club_4@fake.com", "points": "150"},
    ]
  }

  tests_clubs_database_path = tmp_path_factory.getbasetemp() / "clubs.json"

  with open(tests_clubs_database_path, 'w') as outfile:
    json.dump(clubs, outfile)

  return clubs, tests_clubs_database_path


@pytest.fixture()
def competitions(tmp_path_factory):
  competitions = {
    "competitions": [
      {
        "name": "Fake Competition 1",
        "date": "2075-02-28 10:00:00",
        "numberOfPlaces": 25,
      },
      {
        "name": "Fake Competition 2",
        "date": "2050-03-27 10:00:00",
        "numberOfPlaces": 12,
      },
      {
        "name": "Fake Competition 3",
        "date": "2020-02-28 10:00:00",
        "numberOfPlaces": 5,
      },
    ]
  }

  tests_competitions_database_path = tmp_path_factory.getbasetemp() / \
      "competitions.json"

  with open(tests_competitions_database_path, 'w') as outfile:
    json.dump(competitions, outfile)

  return competitions, tests_competitions_database_path


@pytest.fixture()
def tests_database(clubs, competitions):
  get_data.DATABASE_CLUBS_PATH = clubs[1]
  get_data.DATABASE_COMPETITIONS_PATH = competitions[1]
  get_data.load()
  return get_data


@pytest.fixture()
def first_club(tests_database):
  return tests_database.clubs[0]
