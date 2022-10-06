from flask import Flask, render_template
from flask_socketio import SocketIO

# Init flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "tmp" # change this!!!!
socket = SocketIO(app)

# Example data to send via sockets
data = [x for x in range(0, 10)]
status = ""

@app.route("/")
def index():
	return render_template("index.html")

@socket.on("message")
def handler(message):
	"""
	Listens for message request then get value of status and send it
	"""
	global status
	
	if message == "start":
		status = message
	socket.send(status)


if __name__ == "__main__":
	socket.run(app, debug=True)