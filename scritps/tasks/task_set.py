from locust import User, task, between, TaskSet

class UserBehaviour(TaskSet):

    @task()
    def add_cart(self):
        print("I am add to cart")

    @task()
    def view_product(self):
        print("I am view product")

class MyUser(User):

    wait_time = between(1,2)
    tasks = [UserBehaviour]

    

# We can define the task_set class inside the Userclass



# class MyUser(User):

#     wait_time = between(1,2)
    
#     @task()
#     class UserBehaviour(TaskSet):

#         @task # method is optional
#         def add_cart(self):
#             print("I am add to cart")

#         @task()
#         def view_product(self):
#             print("I am view product")

