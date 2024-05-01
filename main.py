from flask import Flask , render_template, request, session , redirect
from flask_socketio import join_room, leave_room, send, SocketIO
from string import ascii_upercase

app = Flask(__name__)
app.config["select_key"] = "akjbfhkabfekh"
socketio = SocketIO(app)

If if __name__ == "__main__":
    socketio.run(app, debug=True)
