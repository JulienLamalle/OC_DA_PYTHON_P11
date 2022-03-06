import datetime


def is_valid_purchase(competition, club, required_places):
  if required_places <= 0 or required_places > int(competition['numberOfPlaces']):
    return False
  if int(required_places) > int(club["points"]):
    return False
  if int(required_places) > 12:
    return False
  if int(required_places) > define_max_places_we_can_purchase(club) or define_max_places_we_can_purchase(club) <= 0:
    return False
  return True

def is_not_a_past_competition(competition):
  return competition['date'] >= datetime.datetime.now().strftime('%Y-%m-%d')


def define_max_places_we_can_purchase(club):
  return int(club["points"]) / 3