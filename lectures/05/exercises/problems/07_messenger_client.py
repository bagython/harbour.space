"""Problem 07 (part B): messenger sender client.

Task:
1. Split into pairs
2. Write an infinite loop reading message text from terminal
3. Send each message to partner API endpoint /messages
4. Show send status in terminal


Partner setup:
- Partner gives you ngrok public URL
- You set TARGET_BASE_URL to that URL
"""

import datetime
from uuid import UUID, uuid4

import requests
from pydantic import BaseModel

# TARGET_BASE_URL = "https://replace-with-partner-ngrok-url"
SENDER_NAME = "beebs"

TARGET_BASE_URL = "http://localhost:8000"


class MessageIn(BaseModel):
    sender_name: str = "Anonymous"
    sent_timestamp: datetime.datetime
    id: UUID
    contents: str
    # attachments: list[HttpUrl]
    attachments: list[str]


def main() -> None:
    while True:
        body = input("Message contents: ")
        attachments = input("Media attachments: ").split()

        payload = MessageIn(
            # sender_name=SENDER_NAME,
            sent_timestamp=datetime.datetime.now(),
            id=uuid4(),
            contents=body,
            attachments=attachments,
        )

        result = requests.post(
            f"{TARGET_BASE_URL}/messages", json=payload.model_dump(mode="json")
        )

        print(result.text)


if __name__ == "__main__":
    main()
