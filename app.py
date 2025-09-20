from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/health')
def health():
    message = os.environ.get('REPLY_HEALTH_MESSAGE', 'Service is healthy')
    return jsonify({'status': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 
