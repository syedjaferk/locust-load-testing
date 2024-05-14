from locust import HttpUser, task, between, SequentialTaskSet

# class MyUser(HttpUser):

#     wait_time = between(1, 2)
#     host = "https://httpbin.org"

#     @task
#     def launch_url(self):
#         self.client.get("/get")
    

#     @task
#     def post_ex(self):
#         self.client.post("/post", name="post test", data={"action": "abcd"})


class TestWebsite(SequentialTaskSet):

    @task
    def get_request(self):
        self.client.get("/get")
    
    @task
    def post_request(self):
        self.client.post("/post")

class MyUser(HttpUser):

    wait_time = between(1, 2)
    host = "https://httpbin.org"

    tasks = [TestWebsite]