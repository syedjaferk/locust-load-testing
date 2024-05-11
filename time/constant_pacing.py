from locust import HttpUser, task, between, constant_pacing

class MyUser(HttpUser):
    @task
    def my_task(self):
        # Perform some HTTP request here
        self.client.get("/")

    wait_time = constant_pacing(2)  # Perform 2 tasks per second
