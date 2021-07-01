from src.validation import validate_json
# ... imports
@app.route('/check', methods=['POST'])
@validate_json
def check():
    # ... rest