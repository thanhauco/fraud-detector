from flask import Flask, request, jsonify
from src.auth import token_required
# ... imports
app = Flask(__name__)
# ... setup
@app.route('/check', methods=['POST'])
@token_required
def check():
    # ... logic
    return jsonify({'fraud': False})
if __name__ == '__main__': app.run()