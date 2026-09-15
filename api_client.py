import requests
import os
from dotenv import load_dotenv

load_dotenv()

def request(method, url, **kwargs):
    try:
        response = requests.request(method, url, timeout=5, **kwargs
        )

        response.raise_for_status()

        if response.content:
            data = response.json()

        else:
            data =  None

        return{"status_code": response.status_code,
               "data": data

}

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None

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

    result = request("GET", url, params=params,  headers=headers)
    if result is not None:
        return result["data"]
    
    return None

def create_post(title, body, userId):
    url = "https://jsonplaceholder.typicode.com/posts"

    post = {"title" : title,
    "body" : body,
    "userId" : userId

}

    headers = {
        "Authorization": f"Bearer {os.getenv('MY_API_KEY')}"
    }

    result =  request("POST", url, json=post, headers=headers)
    if result is not None:
        return result["data"]
    
    return None
    
def update_post(post_id, title=None, body=None):
    url = "https://jsonplaceholder.typicode.com/posts/post_id"
    post_update = {}

    headers = {
        "Authorization": f"Bearer {os.getenv('MY_API_KEY')}"}

    if title is not None:
        post_update["title"]=title

    if body is not None:
        post_update["body"]=body

    result = request( "PATCH", url, json=post_update, headers=headers)
    if result is not None:
        return result["data"]
    
    return None
    
def delete_post(post_id):
    url = "https://jsonplaceholder.typicode.com/posts/post_id"

    headers = {
        "Authorization": f"Bearer {os.getenv('MY_API_KEY')}"}


    result =  request( "DELETE", url, headers=headers)

    if result is None:
        return False

    return 200 <= result["status_code"] < 300
