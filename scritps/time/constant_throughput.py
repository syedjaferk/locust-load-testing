from locust import User, task, constant_pacing
from datetime import datetime


class MyUser(User):

    wait_time=constant_pacing(1) # initial wait time
    # constant_throughput = 100

    @task
    def login_url(self):
        # define your task here.
        print(datetime.now(),"hi")