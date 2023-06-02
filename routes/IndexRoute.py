from main import app
from models import UserModel
from fastapi.responses import RedirectResponse


@app.get('/')
def index():
    return RedirectResponse('/docs')
