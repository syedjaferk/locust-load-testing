1. How to send x no. of requests per second ? 

> Constant Throughput is about maintaining a consistent rate of requests sent to the target system.

you want to simulate a constant throughput of 100 requests per second (RPS). Here's how you can achieve that using the **constant_throughput** feature

Example 1: 

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

Example 2: 

```
from locust import HttpUser, task, constant

class MyUser(HttpUser):
    @task
    def my_task(self):
        # Perform some HTTP request here
        self.client.get("/")

    wait_time = constant(0)  # Set initial wait time to 0
    constant_throughput = 100  # Desired throughput of 100 requests per second

```

2. How to execute x no. of tasks per second ?

> Constant Pacing is about simulating a consistent workload or a specific level of activity on the system under test, regardless of variations in task execution times or system load.

```
from locust import HttpUser, task, between, constant_pacing

class MyUser(HttpUser):
    @task
    def my_task(self):
        # Perform some HTTP request here
        self.client.get("/")

    wait_time = constant_pacing(2)  # Perform 2 tasks per second

```

3. What is the difference between constant pacing and constant throughput ?

constant_pacing and constant_throughput are both features in Locust that regulate the rate at which tasks are executed, but they serve different purposes and operate in different ways:

    Purpose:
        Constant Pacing: With constant_pacing, the focus is on maintaining a steady pace of task execution, typically measured in tasks per unit of time (e.g., tasks per second).
        Constant Throughput: On the other hand, constant_throughput aims to maintain a constant rate of requests sent to the target system, usually measured in requests per unit of time (e.g., requests per second).

    Adjustment Mechanism:
        Constant Pacing: Locust adjusts the wait time between task executions to achieve the specified task rate, irrespective of how long each task takes to execute.
        Constant Throughput: Here, Locust adjusts the wait time between tasks based on the time taken to execute each task and maintain the desired rate of requests to the target system.

    Use Cases:
        Constant Pacing: Useful when you want to simulate a consistent workload or a specific level of activity on the system under test, regardless of variations in task execution times or system load.
        Constant Throughput: Ideal for simulating a consistent load on the system by controlling the rate at which requests are sent to it, ensuring a stable number of requests per second.

4. If there are 2 classes, how will you give the priority for one class to have more users ?

You can mention the `weight` attribute. Which will seggregate the users. 

```

from locust import User, task, between

class MyWebUser(User):

    wait_time=between(1, 2)
    weight = 3

    @task
    def login_url(self):
        print("I am logging into Web Url")


class MyMobileUser(User):

    wait_time=between(1, 2)
    weight = 1

    @task
    def login_url(self):
        print("I am logging into Mobile Url")
```

5. Can i do all the configuration using cli ?

```
locust -f headless.py -u 5 -r 1 -t 10s --headless --logfile .logfile --loglevel DEBUG

```

