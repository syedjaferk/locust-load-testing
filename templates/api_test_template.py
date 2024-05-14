from locust import HttpUser, TaskSet, task, between, constant_pacing, constant_throughput, events

def get_headers():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer <your_token>"
    }
    return headers

def get_payload():
    payload = {
        "key": "value"
    }
    return payload

def get_proxies():
    proxies = {

    }
    return proxies


# If you need to run when a test is start executing.
@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new test is starting")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("A new test is ending")


class MyTaskSet(TaskSet):
    # weight = 1 If you have many taskset and to give weightage for each.

    # Note: Method names can be different. It need not be get_request. 

    @task(weight=1)
    def get_request(self):
        with self.client.get("/get", catch_response=True, name="get api name") as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("GET request failed")

    @task(weight=1)
    def post_request(self):
        with self.client.post("/post", json={"key": "value"}, catch_response=True, name="post api name") as response:
            if response.status_code == 201:
                response.success()
            else:
                response.failure("POST request failed")

    @task(weight=1)
    def put_request(self):
        with self.client.put("/put", json={"key": "value"}, catch_response=True, name="put api name") as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("PUT request failed")

    @task(weight=1)
    def delete_request(self):
        with self.client.delete("/delete", catch_response=True, name="delete api name") as response:
            if response.status_code == 204:
                response.success()
            else:
                response.failure("DELETE request failed")

    @task(weight=1)
    def patch_request(self):
        with self.client.patch("/patch", json={"key": "value"}, catch_response=True, name="patch api name") as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("PATCH request failed")

class MyUser(HttpUser):

    def __init__(self, environment):
        """ Class constructor."""
        super().__init__(environment)

    wait_time = between(1, 3) # To wait between 1 to 3 seconds for each request for each user.
    # wait_time = constant_pacing(1) # To attain no of requests per second. If you want to have 100 requests per second, then have the users as 100.
    # wait_time = constant_throughput(0.1) # To attain no of tasks per second. 
    tasks = [MyTaskSet]

    def on_start(self):
        """ on_start is called when a user start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping for a user"""
        pass


# To run in headless mode, 
# ------------------------

# locust -f locustfile.py --headless -u 10 -r 10 --logfile <logfilee>
# for more options check https://docs.locust.io/en/stable/configuration.html#configuration