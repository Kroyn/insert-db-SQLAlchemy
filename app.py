from flask import Flask
from flask_smorest import Api
from db import db
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    
    # Add API title and OpenAPI configuration
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.2"  # Додайте цей рядок
    
    # Initialize SQLAlchemy
    db.init_app(app)
    
    # Initialize Flask-Smorest with API title and OpenAPI version
    api = Api(app, spec_kwargs={
        "title": "Stores REST API",
        "openapi_version": "3.0.2"  # Додайте цей рядок
    })
    
    # Register Blueprints
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)