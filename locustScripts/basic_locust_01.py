
from locust import User,task,between

class MyUser(User):
    wait_time=between(1,2)

    @task
    def login_URL(self):
        print("Im loggin into URL")