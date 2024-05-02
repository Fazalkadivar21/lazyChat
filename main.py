from flask import Flask , render_template, request, session , redirect
from flask_socketio import join_room, leave_room, send, SocketIO
import string
import secrets

app = Flask(__name__)
app.config["select_key"] = "akjbfhkabfekh"
socketio = SocketIO(app)

rooms = {}

def generateCode(length=32):
    while True:
        characters = string.ascii_letters + string.digits + string.punctuation
        
        code = ''.join(secrets.choice(characters) for _ in range(length))
        
        if code not in rooms:
            break

    return code

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        if not name:
            return render_template("home.html" , error="please enter a name", code=code,name=name)
        
        if join != False and not code:
            return render_template("home.html", error="please enter a room code", code=code,name=name)

        room = code
        if create != False:
            room = generateCode()
            rooms[room] = {"members": 0, "messages": []}
        elif code not in rooms:
            render_template("home.html",error="Room doesn't exist", code=code,name=name)
           
        session["room"] = room
        session["name"] = name

    return render_template("home.html")

if __name__ == "__main__":
    socketio.run(app, debug=True)
