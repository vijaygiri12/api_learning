import requests
import os
from dotenv import load_dotenv

load_dotenv()


def request(method, url, **kwargs):
    headers = kwargs.pop("headers", {})

    api_key = os.getenv("MY_API_KEY")

    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    try:
        response = requests.request(
            method,
            url,
            headers=headers,
            timeout=5,
            **kwargs
        )

        response.raise_for_status()

        if response.content:
            data = response.json()
        else:
            data = None

        return {
            "error": False,
            "status_code": response.status_code,
            "data": data
        }

    except requests.exceptions.HTTPError as e:
        return {
            "error": True,
            "status_code": e.response.status_code,
            "message": str(e)
        }

    except requests.exceptions.RequestException as e:
        return {
            "error": True,
            "status_code": None,
            "message": str(e)
        }