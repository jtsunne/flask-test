from src.config import DI
from flask import Flask


src = Flask(__name__, static_folder="frontend/static")
src.container = DI()

from src.frontend import frontend

API_BASE_URL = "/api/v1"

for blueprint in [frontend]:
    if blueprint.name == "frontend":
        src.register_blueprint(
            blueprint,
            url_prefix="/",
        )
    else:
        src.register_blueprint(
            blueprint,
            url_prefix=f"{API_BASE_URL}/{blueprint.name}",
        )
