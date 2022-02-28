from locust import HttpUser, task 

class ProjectPerfTest(HttpUser):
  @task
  def registration(self):
    response = self.client.get("/")