from locust import User, task, between 

class MyUser(User):

    wait_time = between(1,2)

    @task(weight=2)
    def add_cart(self):
        print("I am add to cart")
    

    @task(weight=4)
    def view_product(self):
        print("I am view product")

# Task weightage is useful for creating realistic load test scenarios
# where different user behaviors have varying probabilities of occurrence
# For example, you might assign higher weights to critical user actions or
# frequently used features to ensure they are adequately stress-tested during the load test.