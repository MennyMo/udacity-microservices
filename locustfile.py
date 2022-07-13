from locust import HttpUser, between, task

# def testHome(l):
#     l.client.get("/")

# class UserBehaviour(TaskSet):
#     task = testHome

# class WebsiteUser(HttpUser):
#     task_set = [UserBehaviour]
#     wait_time = between(5.0, 9.0)

class QuickStart(HttpUser):
    wait_time = between(1.0, 5.0)

    @task
    def home(self):
        self.client.get('/')