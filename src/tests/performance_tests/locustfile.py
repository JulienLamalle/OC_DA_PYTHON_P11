from random import randint
from locust import HttpUser, task 
import sys 
sys.path.insert(1, '../../data_fetching/get_data.py')
from data_fetching import get_data


get_data.load()
class ProjectPerfTest(HttpUser):
  @task
  def index(self):
    response = self.client.get("/")
    
  @task
  def show_summary(self):
    email = get_data.clubs[0]['email']
    self.client.post("/show-summary", {"email": email})

  @task
  def book(self):
    competition = get_data.competitions[0]["name"]
    club = get_data.clubs[0]["name"]
    self.client.get(f"/book/{competition}/{club}")

  @task
  def purchase_places(self):
    club = get_data.clubs[0]
    competition = get_data.competitions[0]
    required_places = 1
    self.client.post("/purchase-places", {"competition": competition, "club": club, "places": required_places})
    
  @task
  def clubs(self):
    self.client.get("/clubs")

  @task
  def logout(self):
    self.client.get("/logout")
  