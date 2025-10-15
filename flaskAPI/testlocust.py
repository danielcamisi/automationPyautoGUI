from locust import HttpUser, task, between
import random

class baseUser(HttpUser):
    abstract = True

    wait_time = between(1, 3)

    host = "http://locahost:8000"
