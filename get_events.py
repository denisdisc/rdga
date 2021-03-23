from webapp import create_app
from webapp.main import collectlinks

app = create_app()

with app.app_context():
    collectlinks()
