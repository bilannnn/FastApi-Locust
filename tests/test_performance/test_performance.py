from locust import HttpUser, task, between
import json

from src.constants import IMAGE_URL
from src.schema import Img


class PerformanceTests(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def test_fastapi(self):
        response = self.client.get("/")

    @task(2)
    def test_torch_predict(self):
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        self.client.post(
            "/predict/torch_model/", json={"img_url": IMAGE_URL}, headers=headers
        )

    @task(3)
    def test_tf_predict(self):
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        self.client.post("/predict/tf/", json={"img_url": IMAGE_URL}, headers=headers)
