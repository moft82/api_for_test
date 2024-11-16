class DataWebSocketHandler {
    constructor(table, jsonFilename) {
        const WS_URL = "ws://127.0.0.1:8000/ws/websocket"; // Consistent WebSocket URL
        this.socket = new WebSocket(WS_URL);
        this.dataTemplateManager = new DataTemplateManager(jsonFilename);
        this.table = table;

        this.socket.onopen = this.onOpen.bind(this);
        this.socket.onmessage = this.onMessage.bind(this);
        this.socket.onclose = this.onClose.bind(this);
        this.socket.onerror = this.onError.bind(this);
    }

    onOpen(event) {
        console.log("WebSocket connection established.");
    }

    onMessage(event) {
        console.log("Received message from server:", event.data);
        if (this.table) {
            this.table.ajax.reload();
        }
        else{
            console.log("Table not exist");
        }
    }

    onClose(event) {
        console.log("WebSocket connection closed.");
    }

    onError(event) {
        console.error("WebSocket error:", event);
    }

    sendMessage(message) {
        this.socket.send(message);
    }
}