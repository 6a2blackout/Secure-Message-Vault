from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from hashlib import sha256, md5
import json
import base64
import os

app = Flask(__name__, static_folder='static')
CORS(app)

def pad(data):
    paddingLength = 16 - (len(data) % 16)
    return data + chr(paddingLength) * paddingLength

def unpad(data):
    paddingLength = ord(data[-1])
    return data[:-paddingLength]

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/create-user', methods=['POST'])
def create_user():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        message = data.get('message')
        hash_choice = data.get('hashChoice')  # 'sha256' or 'md5'
        
        if hash_choice == 'sha256':
            key = sha256(password.encode()).digest()
            IV = get_random_bytes(16)
            encryption = AES.new(key, AES.MODE_CBC, IV)
            encryptedMessage = encryption.encrypt(pad(message).encode())
            hashValue = sha256(encryptedMessage).hexdigest()
            hashAlgo = "SHA-256"
        else:  # md5
            key = md5(password.encode()).digest()
            IV = get_random_bytes(16)
            encryption = AES.new(key, AES.MODE_CBC, IV)
            encryptedMessage = encryption.encrypt(pad(message).encode())
            hashValue = md5(encryptedMessage).hexdigest()
            hashAlgo = "MD5"
        
        user = {
            "Username": username,
            "HashAlgo": hashAlgo,
            "IV": base64.b64encode(IV).decode(),
            "encryptedMessage": base64.b64encode(encryptedMessage).decode(),
            "hashValue": hashValue
        }
        
        with open("Users.json", "a") as file:
            file.write(json.dumps(user) + "\n\n\n")
        
        return jsonify({"success": True, "message": "User created and message encrypted successfully!"})
    
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 400

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        
        if not os.path.exists("Users.json"):
            return jsonify({"success": False, "message": "No users found"}), 404
        
        with open("Users.json", "r") as file:
            for line in file:
                if not line.strip():
                    continue
                try:
                    user = json.loads(line)
                except json.JSONDecodeError:
                    continue
                
                if user["Username"] == username:
                    if user["HashAlgo"] == "SHA-256":
                        key = sha256(password.encode()).digest()
                        IV = base64.b64decode(user["IV"])
                        encryptedMessage = base64.b64decode(user["encryptedMessage"])
                        hashValue = user["hashValue"]
                        
                        testHash = sha256(encryptedMessage).hexdigest()
                        if testHash != hashValue:
                            return jsonify({"success": False, "message": "Integrity check failed!"})
                        
                        encryption = AES.new(key, AES.MODE_CBC, IV)
                        message = unpad(encryption.decrypt(encryptedMessage).decode())
                        return jsonify({"success": True, "message": message})
                    
                    elif user["HashAlgo"] == "MD5":
                        key = md5(password.encode()).digest()
                        IV = base64.b64decode(user["IV"])
                        encryptedMessage = base64.b64decode(user["encryptedMessage"])
                        hashValue = user["hashValue"]
                        
                        testHash = md5(encryptedMessage).hexdigest()
                        if testHash != hashValue:
                            return jsonify({"success": False, "message": "Integrity check failed!"})
                        
                        encryption = AES.new(key, AES.MODE_CBC, IV)
                        message = unpad(encryption.decrypt(encryptedMessage).decode())
                        return jsonify({"success": True, "message": message})
        
        return jsonify({"success": False, "message": "Username not found"}), 404
    
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)