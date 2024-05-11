1. How to send x no. of requests per second ?

you want to simulate a constant throughput of 100 requests per second (RPS). Here's how you can achieve that using the **constant_throughput** feature

```
from locust import User, task, constant
from datetime import datetime


class MyUser(User):

    wait_time=constant(0) # initial wait time
    constant_throughput = 100

    @task
    def login_url(self):
        # define your task here.
        print(datetime.now())
```

