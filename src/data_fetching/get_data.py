import json
from pathlib import Path
from src import db
import os

DATABASE_CLUBS_PATH = Path(__file__).resolve().parent.parent / "db/clubs.json"
DATABASE_COMPETITIONS_PATH = Path(
  __file__).resolve().parent.parent / "db/competitions.json"


def load_clubs():
  with open(DATABASE_CLUBS_PATH) as file:
    return json.load(file)['clubs']


def load_competitions():
  with open(DATABASE_COMPETITIONS_PATH) as file:
    return json.load(file)['competitions']


def load():
  CLUBS = load_clubs()
  COMPETITIONS = load_competitions()
  return CLUBS, COMPETITIONS
