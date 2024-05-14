from locust import User, task, between 

def add_cart(userclass):
    print("I am add to cart")

def view_product(userclass):
    print("I am view product")

class MyUser(User):

    wait_time = between(1,2)
    tasks = [add_cart, view_product]

class MyUser(User):

    wait_time = between(1,2)
    tasks = {add_cart:1, view_product: 2} # {task_name: weightage}