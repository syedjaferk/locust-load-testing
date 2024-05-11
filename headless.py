from locust import HttpUser, between, task

class MyUser(HttpUser):

    wait_time = between(1,2)
    host = "http://localhost:1234"

    @task
    def login_url(self):
        print("I am logging in to an URL")

# locust -f headless.py -u 5 -r 1 -t 10s --headless --logfile .logfile --loglevel DEBUG
