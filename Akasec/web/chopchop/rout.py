from flask import Flask, jsonify, request, abort,render_template
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

CORS(app, resources={r"/socket.io/*": {"origins": "*"}})


@app.route('/',methods=['GET'])
def mypage():
	return render_template('solve.html')
if __name__ == '__main__':
	socketio.run(app, debug=True)
