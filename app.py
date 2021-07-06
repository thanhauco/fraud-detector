from src.limiter import is_limited
# ... imports
@app.before_request
def limit_check():
    if is_limited(request.remote_addr):
        return jsonify({'error': 'Rate limit'}), 429