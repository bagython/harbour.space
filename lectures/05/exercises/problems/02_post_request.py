"""Problem 02: POST request to JSONPlaceholder.

Task:
1. Send POST to https://jsonplaceholder.typicode.com/posts
2. Send JSON payload with fields: title, body, userId
3. Print:
   - status code
   - raw body
   - parsed JSON
4. Confirm response includes your data + id

Note: JSONPlaceholder simulates writes; data is not truly persisted.
"""

import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def main() -> None:

    payload = {"title": "totl", "body": "bad", "userId": 67}

    print(payload)

    response = requests.post(URL, json=payload)

    print(
        response.status_code,
        response.text,
        response.json(),
        f"my data in response? {all(response.json().get(k, None) == v for k, v in payload.items())}",
        f"id: {response.json()['id']}",
        sep="\n",
    )

    print()


if __name__ == "__main__":
    main()
