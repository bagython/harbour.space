"""Problem 07 (part A): messenger API server.

Task:
1. Create POST /messages endpoint, agree on the request schema with your partner
2. Print received message to server console
3. Return JSON confirmation (for example: {"status": "received"})
4. Share API with partner via ngrok (install it first: https://ngrok.com/)

Run:
    uvicorn 07_messenger_server:app --reload
    ngrok http 8000
"""

import datetime
from uuid import UUID

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class MessageIn(BaseModel):
    sender_name: str = "Anonymous"
    sent_timestamp: datetime.datetime
    id: UUID
    contents: str
    attachments: list[HttpUrl]


class MessageOut(BaseModel):
    status: str
    received_timestamp: datetime.datetime
    received_id: UUID
    attachments_count: int


@app.post("/messages")
def receive_message(payload: MessageIn) -> MessageOut:
    # so if i understand correctly i can assume fastapi already
    # validated the model so i don't need to
    # check the actual status type shiiiit

    print(payload.model_dump_json(indent=4))

    return MessageOut(
        status="received",
        received_timestamp=datetime.datetime.now(),
        received_id=payload.id,
        attachments_count=len(payload.attachments),
    )
