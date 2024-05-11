from locust import User, task, constant
from datetime import datetime


class MyUser(User):

    wait_time=constant(0) # initial wait time
    constant_throughput = 100

    @task
    def login_url(self):
        # define your task here.
        print(datetime.now())