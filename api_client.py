import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_posts(user_id=None, limit=None):
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {}

    if user_id is not None:
        params["userId"] = user_id

    if limit is not None:
        params["_limit"] = limit

    headers = {
        "Authorization": f"Bearer {os.getenv('MY_API_KEY')}"
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=5
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return []


def create_post(title, body, userId):
    url = "https://jsonplaceholder.typicode.com/posts"

    post = {"title" : title,
    "body" : body,
    "userId" : userId

}

    headers = {
        "Authorization": f"Bearer {os.getenv('MY_API_KEY')}"
    }
    try:
        response = requests.post(url, json=post, headers=headers, timeout=5)
        response.raise_for_status()

        return response.json()
        
    except requests.exceptions.RequestException as e:
        print("Request failed: ", e)
        
        return {}
        
def update_post(post_id, title=None, body=None):
    url = "https://jsonplaceholder.typicode.com/posts/post_id"
    post_update = {}
    
    headers = {
        "Authorization": f"Bearer {os.getenv('MY_API_KEY')}"}
     
    if title is not None:
        post_update["title"]=title
        
    if body is not None:
        post_update["body"]=body
    
    try:
        response = requests.patch(url, json=post_update, headers=headers, timeout=5)
        response.raise_for_status()
        
        return response.json()
        
    except requests.exceptions.RequestsException as e:
        print("Request failed", e)
        
        return {}

def delete_post(post_id):
    url = "https://jsonplaceholder.typicode.com/posts/post_id"
    
    headers = {
        "Authorization": f"Bearer {os.getenv('MY_API_KEY')}"}
        
    try:
        response = requests.delete(url, headers=headers, timeout=5)
        response.raise_for_status()
        return True
        
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return False
