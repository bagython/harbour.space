"""Problem 01 (merged): setup + first GET request.

Install dependencies (once):
    pip install requests fastapi uvicorn

Task:
1. Send a GET request to https://jsonplaceholder.typicode.com/todos/1
2. Print:
   - status code
   - Content-Type header
   - raw body (response.text)
   - parsed JSON (response.json())
3. Read and print: id, title, completed
4. Add error handling with raise_for_status()

Expected result:
- You can explain the difference between raw text and parsed JSON.
"""

import requests

URL = "https://jsonplaceholder.typicode.com/todos/1"


def main() -> None:
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print(response.status_code)
    print(response.headers["Content-Type"])
    print(response.text)
    print(response.json())


if __name__ == "__main__":
    main()
