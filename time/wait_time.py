from locust import User, task, between
from datetime import datetime


class MyUser(User):

    wait_time=between(1, 3)

    @task
    def login_url(self):
        print(datetime.now())