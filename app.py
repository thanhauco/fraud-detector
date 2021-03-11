from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
app = Flask(__name__)
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
# ... rest