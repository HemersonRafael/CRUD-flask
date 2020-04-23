#src/app.py

import flask

from .config import app_config
from .models import db, bcrypt
from .views.UserView import user_api as user_blueprint

def create_app(env_name):
  """
  Create app
  """
  
  # app initiliazation
  app = flask.Flask(__name__)

  app.config.from_object(app_config[env_name])

  # initializing bcrypt
  bcrypt.init_app(app) 

  # initializing SQLAlchemy
  db.init_app(app)

  app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
   
  @app.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """
    return '<h1>Congratulations! Your first endpoint is workin</h1>'

  return app