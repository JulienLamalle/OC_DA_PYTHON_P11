import json
from pathlib import Path

DATABASE_CLUBS_PATH = Path(__file__).resolve().parent.parent / "db/clubs.json"
DATABASE_COMPETITIONS_PATH = Path(
  __file__).resolve().parent.parent / "db/competitions.json"


def load_clubs():
  with open(DATABASE_CLUBS_PATH) as file:
    return json.load(file)['clubs']


def load_competitions():
  with open(DATABASE_COMPETITIONS_PATH) as file:
    return json.load(file)['competitions']


def get_club_by_email(email):
  try:
    if clubs:
      for club in clubs:
        if club['email'] == email:
          return club
  except (ValueError, KeyError, TypeError):
    return None


def load():
  global clubs
  global competitions
  clubs = load_clubs()
  competitions = load_competitions()
