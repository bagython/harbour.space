"""Problem 03: GET request for HTML content.

Task:
1. Send GET to https://example.com
2. Print:
   - status code
   - Content-Type header
   - HTML body (response.text)
3. Verify content type contains text/html
4. Add raise_for_status()
"""

import requests

URL = "https://example.com"


def main() -> None:
    response = requests.get(URL, verify=False)

    response.raise_for_status()

    print(
        response.status_code,
        response.headers["Content-Type"],
        response.text,
        f"dost content type contain text/html? {'text/html' in response.headers['Content-Type']}",
        sep="\n",
    )


if __name__ == "__main__":
    main()
