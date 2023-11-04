from flask import Flask, jsonify, request, abort
from flask_socketio import *
import hmac
import hashlib
import secrets as s
import os

SECRET_KEY = b's3cr3t' 
print(SECRET_KEY)

voucher = 'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqdb5552521fa9ebb021a7f3ed687302504a57d2b5d3d448bb43acb4588475c17e'
voucher_id = voucher[:32]
signature = voucher[32:]
expected_signature = hmac.new(SECRET_KEY, voucher_id.encode('utf-8'), hashlib.sha256).hexdigest()
print(expected_signature)
    
if hmac.compare_digest(expected_signature, signature) == True:
    print('ooooooo')
