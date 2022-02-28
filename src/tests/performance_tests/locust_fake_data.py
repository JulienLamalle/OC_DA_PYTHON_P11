import tempfile
import json

COMPETITIONS_TEMPORARY_FILE_PATH = tempfile.NamedTemporaryFile()
CLUBS_TEMPORARY_FILE_PATH = tempfile.NamedTemporaryFile()

def create_fake_clubs_data():
  clubs = {
    "clubs": [
      {"name": "Fake Club 1", "email": "fake_club_1@fake.com", "points": "0"},
      {"name": "Fake Club 2", "email": "fake_club_2@fake.com", "points": "50"},
      {"name": "Fake Club 3", "email": "fake_club_3@fake.com", "points": "100"},
      {"name": "Fake Club 4", "email": "fake_club_4@fake.com", "points": "150"},
    ]
  }
  
  with open(CLUBS_TEMPORARY_FILE_PATH.name, "w") as f:
    json.dump(clubs, f)
    
  return CLUBS_TEMPORARY_FILE_PATH.name


def create_fake_competions_data():
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
  
  with open(COMPETITIONS_TEMPORARY_FILE_PATH.name, "w") as f:
    json.dump(competitions, f)
    
  return COMPETITIONS_TEMPORARY_FILE_PATH.name


def load_fake_data():
  #TODO => add_method_to_create_fake_data_files_and_read_data_from_them
  return 
