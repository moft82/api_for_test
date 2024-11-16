from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.utils.connection_manager import ConnectionManager
import json

router = APIRouter(
    prefix="/ws",
    tags=["websocket"],
)
manager : ConnectionManager = ConnectionManager()

@router.websocket("/websocket")
async def websocket_endpoint(websocket: WebSocket):
    # Accept the WebSocket connection
    await manager.connect(websocket)
    print(f"client connected : {websocket.client}")

    try:
        # Continuously listen for messages
        while True:
            # Receive message from the client
            data = await websocket.receive_text()
            message_data = json.load(data)
            # Handle the message
            await manager.broadcast({
                "type": "message",
                "message": message_data["message"]
            })
            
            print(f"Received message from client: {message_data} from :{websocket.client}")
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast({"disconnected"})