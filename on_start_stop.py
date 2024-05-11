from locust import HttpUser, between, task

class MyUser(HttpUser):

    wait_time = between(1,2)
    host = "http://localhost:1234"

    
    def on_start(self):
        print("I am logging in")

    @task
    def doing_work(self):
        print("I am logging in to an URL")

    
    def on_stop(self):
        print("i am logging out")
# locust -f on_start_stop.py -u 5 -r 1 -t 10s --headless --logfile .logfile --loglevel DEBUG
