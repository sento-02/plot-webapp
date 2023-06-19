from flask import Flask

def create_app():
    app = Flask(__name__)

    # ルートとなるBlueprintを登録します
    from .views.views import bp as views_bp
    app.register_blueprint(views_bp)

    return app