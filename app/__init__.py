from flask import Flask

def create_app():
    app = Flask(__name__)

    # BluePrint 등록
    from .routes.index import index_bp
    from .routes.report import report_bp
    from .routes.keyword import keyword_bp

    app.register_blueprint(index_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(keyword_bp)

    return app
    