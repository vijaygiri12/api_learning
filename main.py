import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("MY_API_KEY")

url = "https://jsonplaceholder.typicode.com/posts"

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print("Authorization:", response.request.headers["Authorization"])
