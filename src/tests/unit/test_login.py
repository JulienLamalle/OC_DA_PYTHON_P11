from urllib import response
from src.tests.conftest import client, first_club, tests_database


def test_existing_user_can_login(client, first_club):
  data = {"email": first_club.get("email")}
  response = client.post('/show-summary', data=data, follow_redirects=True)
  assert response.status_code == 200