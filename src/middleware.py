from flask import request
import uuid
def add_request_id(app):
    @app.before_request
    def before():
        request.id = str(uuid.uuid4())