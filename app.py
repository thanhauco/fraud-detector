import psutil
# ... imports
@app.route('/health')
def health():
    return jsonify({'status': 'OK', 'cpu': psutil.cpu_percent()})