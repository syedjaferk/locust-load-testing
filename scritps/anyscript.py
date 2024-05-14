from locust import HttpUser, task, between, User, constant
from datetime import datetime

class QuickstartUser(HttpUser):
    wait_time = constant(3)
    host="https://api.openbrewerydb.org"

    @task
    def index_page(self):
        # self.client.get("/breweries")
        print(datetime.now())
