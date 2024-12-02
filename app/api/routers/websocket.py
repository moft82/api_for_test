from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException
from fastapi import Depends, Request
from typing import Dict
from app.module.connection_manager import manager
from app.utils.time_util import get_KST
import json

router = APIRouter(
    prefix="/ws",
    tags=["Websocket"],
    responses={404: {"description": "Not Found"}}
)

@router.websocket("")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()  # Handle incoming messages from the client if needed
            await manager.broadcast(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@router.post("/update")
async def update_data(request: Request):
    # Parse the incoming JSON payload dynamically
    try:
        update_request = await request.json()
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid JSON payload") from e

    # Construct the message with the provided JSON data
    message = {
        "type": "update",
        "timestamp": str(get_KST()),
        "data": update_request  # Include the entire dynamic payload
    }
    message_json = json.dumps(message)
    print(message_json)
    await manager.broadcast(message_json)
    return {
        "message": "Data update broadcasted to all clients",
        "data": message
    }
