from locust import HttpUser, between, task, events

# Test Start and Stop runs before the entire test class. It should be defined outside. 


@events.test_start.add_listener
def script_start(**kwargs):
    print(" I am connecting to DB")

@events.test_stop.add_listener
def script_stop(**kwargs):
    print("I am disconnecting to DB")


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
