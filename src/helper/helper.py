import datetime


def is_valid_purchase(competition, club, required_places):
  if not competition or not club:
    return False
  if required_places <= 0 or required_places > int(competition['numberOfPlaces']):
    return False
  if int(required_places) > int(club["points"]):
    return False
  if int(required_places) > 12:
    return False
  return True

def is_not_a_past_competition(competition):
  return competition['date'] >= datetime.datetime.now().strftime('%Y-%m-%d')