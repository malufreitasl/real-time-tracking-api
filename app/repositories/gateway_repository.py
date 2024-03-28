import requests
import os

class GatewayRepository:
    def  __init__(self) -> None:
        self.api_key = os.getenv("API_KEY")

    def fetch_shift(self, url, gateway_id, start_timestamp, end_timestamp):
        try:
            url = f"{url}/{gateway_id}/{start_timestamp}"
            params = {
                'timestamp_end': end_timestamp
            }
            response = requests.get(url, params=params, headers={"X-Api-Key": self.api_key})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching data: {e}")
            return []