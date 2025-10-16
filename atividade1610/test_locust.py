from locust import HttpUser, task, between

class UsuarioAPI(HttpUser):
    host = 'http://127.0.0.1:5000'
    wait_time = between(1, 3)
    
    @task(2)
    def acessar_index(self):
        self.client.get('/')

    @task(5)
    def buscar_personagens(self):
        self.client.get("/characters")