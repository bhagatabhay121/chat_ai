from flask import Flask, request, send_from_directory
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

message_history = []

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

    
@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@socketio.on("message")
def handle_message(data):
    print(f"Message: {data}")
    emit("message", data, broadcast=True)

file_parts = {}

@socketio.on("edit_message")
def edit_message(data):
    """Broadcast the edited message to all clients."""
    message_id = data["message_id"]
    new_message = data["new_message"]
    user = data["user"]
    emit("edit_message", {"message_id": message_id, "new_message": new_message, "user": user}, broadcast=True)
    print(f"Message: {data}")


@socketio.on("delete_message")
def delete_message(data):
    """Broadcast a message deletion event."""
    message_id = data["message_id"]
    emit("delete_message", {"message_id": message_id}, broadcast=True)

@socketio.on("file_chunk")
def handle_file_chunk(data):
    filename = data["filename"]
    filedata = data["chunk"]
    total_chunks = data["total_chunks"]
    chunk_index = data["chunk_index"]

    if filename not in file_parts:
        file_parts[filename] = b""

    file_parts[filename] += filedata

    progress = (chunk_index + 1) / total_chunks * 100
    emit("upload_progress", {"filename": filename, "progress": progress}, broadcast=True)

    if chunk_index + 1 == total_chunks:  # Final chunk received
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        with open(filepath, "wb") as f:
            f.write(file_parts.pop(filename))  # Save file
        file_url = f"http://127.0.0.1:5000/uploads/{filename}"
        emit("file_received", {"filename": filename, "url": file_url}, broadcast=True)


@socketio.on("typing")
def user_typing(data):
    socketio.emit("typing", data)

@socketio.on("stopped_typing")
def user_stopped_typing(data):
    socketio.emit("stopped_typing", data)

@socketio.on("play_music")
def play_music(data):
    """ Broadcast music URL to all users """
    print(f"🔊 Broadcasting song: {data}")  # Debugging
    socketio.emit("play_music", data)

@socketio.on("reaction")
def handle_reaction(data):
    message_id = data["message_id"]
    reaction = data["reaction"]
    user = data["user"]

    # Store reactions
    if message_id not in file_parts:
        file_parts[message_id] = {}

    if reaction in file_parts[message_id]:
        file_parts[message_id][reaction] += 1
    else:
        file_parts[message_id][reaction] = 1

    emit("reaction", {"message_id": message_id, "reactions": file_parts[message_id]}, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
