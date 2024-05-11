from locust import User, task, between


# class MyWebUser(User):

#     wait_time=between(1, 2)

#     @task
#     def login_url(self):
#         print("I am logging into Web Url")


# class MyMobileUser(User):

#     wait_time=between(1, 2)

#     @task
#     def login_url(self):
#         print("I am logging into Mobile Url")


# Consider the number of user set is 2 so 1 user will be allocated to each one of them 
# [2024-05-11 12:41:06,845] syedjaferk/INFO/locust.runners: All users spawned: {"MyMobileUser": 1, "MyWebUser": 1} (2 total users)
# But if you want to give more users to a particular class then you can mention weightage.


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