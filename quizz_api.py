import requests
import os
from dotenv import load_dotenv
class api_req:
    load_dotenv()
    def __init__(self):
        parameters = {
            "amount":10,
            "category":9,
            "difficulty":"medium",
            "type":"boolean"
        }
        self.connection = requests.get(url=os.getenv("URL"),params=parameters)
        self.connection.raise_for_status()
        self.data = self.connection.json()

