from flask import Flask, jsonify, request, abort
from flask_socketio import *
import hmac
import hashlib
import secrets as s
import os

SECRET_KEY = os.getenv('SECRET_KEY') or b's3cr3t'

app = Flask(__name__)
sock = SocketIO(app, cors_allowed_origins="*")

#@sock.on('generate')
#def generate():
    #TODO: complete generate route to return vouchers
    #return jsonify({'voucher': voucher})

@app.route('/debug', methods=['DEBUG'])
def debug():
    debug_info = {
        "App Name": app.name,
        "Debug Mode": app.debug,
        "View Functions": list(app.view_functions.keys()),
        "Request Method": request.method,
        "Request Headers": dict(request.headers),
        "Environment Variables": dict(os.environ)
    }
    return jsonify(debug_info)


@app.route('/verify', methods=['POST'])
def verify():
    if not request.json or not 'voucher' in request.json:
        abort(400)
    voucher = request.json['voucher']
    voucher_id = voucher[:32]
    signature = voucher[32:]
    expected_signature = hmac.new(SECRET_KEY, voucher_id.encode('utf-8'), hashlib.sha256).hexdigest()
    if hmac.compare_digest(expected_signature, signature) == True:
        return jsonify({'verified': True})
    else:
        return jsonify({'verified': False})

if __name__ == '__main__':
    sock.run(app, host='0.0.0.0' ,port=6969)
