from src.helper import helper
from src.tests.conftest import client, clubs, competitions, tests_database


def test_is_valid_purchase(tests_database):
  book_one_place_for_club_with_more_than_one_points = helper.is_valid_purchase(
    tests_database.competitions[0], tests_database.clubs[3], 1)
  assert book_one_place_for_club_with_more_than_one_points is True


def test_is_valid_purchase_returns_false_if_required_places_is_zero(tests_database):
  book_zero_places_for_club_with_more_than_one_points = helper.is_valid_purchase(
    tests_database.competitions[0], tests_database.clubs[3], 0)
  assert book_zero_places_for_club_with_more_than_one_points is False


def test_is_valid_purchase_returns_false_if_required_places_is_more_than_number_of_places(tests_database):
  book_more_places_than_availables_in_competition = helper.is_valid_purchase(
    tests_database.competitions[2], tests_database.clubs[3], 6)
  assert book_more_places_than_availables_in_competition is False


def test_is_valid_purchase_returns_false_if_required_places_is_more_than_12(tests_database):
  book_more_places_than_twelves_places = helper.is_valid_purchase(
    tests_database.competitions[0], tests_database.clubs[3], 13)
  assert book_more_places_than_twelves_places is False


def test_is_valid_purchase_returns_false_if_club_has_any_points(tests_database):
  book_places_with_any_points = helper.is_valid_purchase(
    tests_database.competitions[0], tests_database.clubs[0], 1)
  assert book_places_with_any_points is False


def test_is_not_a_past_competition(tests_database):
  assert helper.is_not_a_past_competition(
    tests_database.competitions[0]) is True


def test_is_not_a_past_competition_returns_false_if_competition_is_in_the_past(tests_database):
  assert helper.is_not_a_past_competition(
    tests_database.competitions[2]) is False


def test_define_max_places_we_can_purchase(tests_database):
  assert helper.define_max_places_we_can_purchase(
    tests_database.clubs[1]) == 4

def test_define_max_places_we_can_purchase_when_club_have_any_points(tests_database):
  assert helper.define_max_places_we_can_purchase(
    tests_database.clubs[0]) == 0
