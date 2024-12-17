from locust import HttpUser, TaskSet, task, between

class ApiService(TaskSet):
    @task(1)
    def test_endpoint(self):
        """Simulates GET requests to /test"""
        response = self.client.get("/test")
        if response.status_code != 200:
            response.failure(f"Failed: {response.text}")

    @task(1)
    def hola_endpoint(self):
        """Simulates GET requests to /hola/{name}"""
        name = "world"
        response = self.client.get(f"/hola/{name}")
        if response.status_code != 200:
            response.failure(f"Failed: {response.text}")

class HelloService(TaskSet):
    @task(1)
    def hello_endpoint(self):
        """Simulates GET requests to /hello"""
        response = self.client.get("/hello")
        if response.status_code != 200:
            response.failure(f"Failed: {response.text}")

class ApiUser(HttpUser):
    host = "http://api.local"

    """Simulates a user interacting with the API"""
    tasks = [ApiService]
    wait_time = between(1, 2)

class HelloUser(HttpUser):
    host = "http://hello-service.local"
    
    """Simulates a user interacting with the Hello Service"""
    tasks = [HelloService]
    wait_time = between(1, 2)
