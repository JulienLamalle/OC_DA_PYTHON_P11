from locust import HttpUser, task 

class ProjectPerfTest(HttpUser):
  @task
  def index(self):
    response = self.client.get("/")
    
  @task
  def show_summary(self):
    self.client.post("/showSummary", {"email": 'fake@email.com'})

  @task
  def book(self):
    self.client.get("/book/fakecompetitions/fakeclub")

  @task
  def purchase_places(self):
    data = {"club": "Fake Club", "competition": "Fake Competition", "places": 1}
    self.client.post("/purchasePlaces", data=data)

  @task
  def logout(self):
    self.client.get("/logout")
  