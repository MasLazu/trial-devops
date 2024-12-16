from locust import HttpUser, TaskSet, task, between

class MyTaskSet(TaskSet):
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

class MyLocustUser(HttpUser):
    """Simulates a user interacting with the API"""
    tasks = [MyTaskSet]
    wait_time = between(1, 2)
