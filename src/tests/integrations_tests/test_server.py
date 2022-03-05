from src.tests.conftest import client, tests_database


def test_client(client):
  response = client.get("/")
  assert response.status_code == 200
  assert b"Welcome" in response.data


def test_login(client, tests_database):
  response = client.post(
    "/show-summary", data={"email": tests_database.clubs[0]["email"]}, follow_redirects=True)
  assert response.status_code == 200
  assert b"Welcome" in response.data


def test_login_fail(client):
  response = client.post(
    "/show-summary", data={"email": "notanuser@gmail.com"}, follow_redirects=True)
  assert response.status_code == 200
  assert b"Sorry, that email wasn&#39;t found." in response.data


def test_booking_client(client, tests_database):
  response = client.get(
    f"/book/{tests_database.competitions[0]['name']}/{tests_database.clubs[0]['name']}")
  assert response.status_code == 200


def test_booking_fail(client):
  response = client.get("/book/notacompetition/notaclub")
  assert response.status_code == 200
  assert b"Something went wrong-please try again" in response.data


def test_to_purchase_places(client, tests_database):
  available_places_in_competition = int(
    tests_database.competitions[0]["numberOfPlaces"])
  available_club_points = int(tests_database.clubs[2]["points"])

  response = client.post("/purchase-places", data={
                         "competition": tests_database.competitions[0]["name"], "club": tests_database.clubs[2]["name"], "places": 1}, follow_redirects=True)
  assert response.status_code == 200
  assert b'Great-booking complete!' in response.data
  assert int(tests_database.competitions[0]
             ["numberOfPlaces"]) == available_places_in_competition - 1
  assert int(tests_database.clubs[2]["points"]) == available_club_points - 1


def test_booking_more_than_available_places(client, tests_database):
  available_places_in_competition = int(
    tests_database.competitions[0]["numberOfPlaces"])
  available_club_points = int(tests_database.clubs[2]["points"])

  response = client.post("/purchase-places", data={
                         "competition": tests_database.competitions[0]["name"], "club": tests_database.clubs[2]["name"], "places": available_places_in_competition + 1}, follow_redirects=True)
  assert response.status_code == 200
  assert int(tests_database.competitions[0]
             ["numberOfPlaces"]) == available_places_in_competition
  assert int(tests_database.clubs[2]["points"]) == available_club_points


def test_booking_more_than_twelve_places(client, tests_database):
  available_places_in_competition = int(
    tests_database.competitions[0]["numberOfPlaces"])
  available_club_points = int(tests_database.clubs[2]["points"])

  response = client.post("/purchase-places", data={
                         "competition": tests_database.competitions[0]["name"], "club": tests_database.clubs[2]["name"], "places": 13}, follow_redirects=True)
  assert response.status_code == 200
  assert b'Sorry, that wasn&#39;t a valid purchase, maybe you don&#39;t have enough points or competition is full, you&#39;re also not allowed to book negative or zero places' in response.data
  assert int(tests_database.competitions[0]
             ["numberOfPlaces"]) == available_places_in_competition
  assert int(tests_database.clubs[2]["points"]) == available_club_points


def test_booking_place_in_past_competition(client, tests_database):
  available_places_in_competition = int(
    tests_database.competitions[2]["numberOfPlaces"])
  available_club_points = int(tests_database.clubs[2]["points"])

  response = client.post("/purchase-places", data={
                         "competition": tests_database.competitions[2]["name"], "club": tests_database.clubs[2]["name"], "places": 1}, follow_redirects=True)
  assert response.status_code == 200
  assert b'Welcome' in response.data
  assert int(tests_database.competitions[2]
             ["numberOfPlaces"]) == available_places_in_competition
  assert int(tests_database.clubs[2]["points"]) == available_club_points


def test_logout(client):
  response = client.get("/logout", follow_redirects=True)

  assert response.status_code == 200
  assert b'Welcome to the GUDLFT' in response.data
