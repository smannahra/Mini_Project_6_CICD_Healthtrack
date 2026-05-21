"""
HealthTrack API
A patient vitals tracking backend for clinics.
"""

from flask import Flask, jsonify
from .routes import vitals_bp, patients_bp, alerts_bp


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-secret-change-in-prod"
    app.register_blueprint(vitals_bp)
    app.register_blueprint(patients_bp)
    app.register_blueprint(alerts_bp)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    return app
