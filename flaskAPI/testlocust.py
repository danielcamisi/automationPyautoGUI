from locust import HttpUser, task, between
import random

class baseUser(HttpUser):
    abstract = True

    wait_time = between(1, 3)

    host = "http://locahost:8000"

class userWeight(baseUser):
    weight = 1

    @task(3)
    def pageAcess(self):
        self.client.get("/")

    @task(2)
    def search_ComplexData(self):
        self.client.get("/data/search/complex?filter=1,2,3")

    @task(1)
    def search_Data(self):
        self.client.get("/data/search")
    
        