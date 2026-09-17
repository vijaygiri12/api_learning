import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")


class APIClient:
    def __init__(self, base_url, **kwargs):
            self.headers = kwargs.pop("headers", {})
            self.api_key = os.getenv("MY_API_KEY")
            if self.api_key:
                self.headers["Authorization"] = f"Bearer {self.api_key}"
            base_url  = base_url.rstrip( "/")
            self.base_url = base_url
    def request(self, method, url,  **kwargs):
        request_headers = kwargs.pop("headers", {})
        final_headers = { **self.headers, **request_headers}
        full_url = self.base_url + url
        try:
            response = requests.request(method, full_url, headers=final_headers, timeout=5, **kwargs)
            response.raise_for_status()
        
            if response.content:
                data = response.json()
            else:
                data = None
            
            return {"error": False,
            "status_code": response.status_code,
            "data": data
                }
        
        except requests.exceptions.HTTPError as e:
                return {"error": True,
                "status_code": e.response.status_code,
                "message": str(e)}
                
        except requests.exceptions.RequestException as e:
                return {"error": True,
                "status_code": None,
                "message": str(e)}
    
    def get(self, url, **kwargs):
        return self.request("GET", url, **kwargs)

    def post(self, url, **kwargs):
        return self.request("POST", url, **kwargs)

    def patch(self, url, **kwargs):
        return self.request("PATCH", url, **kwargs)

    def delete(self, url, **kwargs):
        return self.request("DELETE", url, **kwargs)
        
client = APIClient("https://jsonplaceholder.typicode.com///")
headers = {"Authorization": "Vijay999"}
result = client.get( "/posts", headers=headers)
print(len(result["data"]))

