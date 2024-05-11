from locust import User, task, constant
from datetime import datetime


class MyUser(User):

    wait_time=constant(3)

    @task
    def login_url(self):
        print(datetime.now())